import bpy
import bmesh
import json
from mathutils import Vector

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

class Generic:
    def __init__( self, **dict ):
        self.__dict__.update(dict)
        return self

_layers = (True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

class Creator( object ):
    def __init__(self, pConfig ):
        bpyscene = bpy.context.scene

        aConfig = Struct(**pConfig)

        configMaterial = bpy.data.materials.get( aConfig.material )

        if 'position' in pConfig:
          aConfig.position = Struct( **pConfig['position'] )

        # if 'verts' in pConfig:
        #   aConfig.verts = Struct( **pConfig['verts'] )

        if( aConfig.type == 'sphere' ):
            # Create an empty mesh and the object.
            mesh = bpy.data.meshes.new( aConfig.mesh )
            basic_sphere = bpy.data.objects.new( aConfig.mesh, mesh)

            # Add the object into the scene.
            bpyscene.objects.link(basic_sphere)
            bpyscene.objects.active = basic_sphere
            basic_sphere.select = True

            basic_sphere.location.x = aConfig.position.x
            basic_sphere.location.y = aConfig.position.y
            basic_sphere.location.z = aConfig.position.z

            if basic_sphere.data.materials:
                # assign to 1st material slot
                basic_sphere.data.materials[0] = configMaterial
            else:
                # no slots
                basic_sphere.data.materials.append( configMaterial )

            # Construct the bmesh cube and assign it to the blender mesh.
            bm = bmesh.new()
            # https://docs.blender.org/api/blender_python_api_2_77_3/bmesh.ops.html?highlight=bisect%20edges
            bmesh.ops.create_uvsphere(bm, u_segments= aConfig.u , v_segments= aConfig.v, diameter= aConfig.diameter)
            bm.to_mesh(mesh)
            bm.free()

            #bpy.ops.object.modifier_add(type= aConfig.modifier )
            #bpy.ops.object.shade_smooth()

        elif( aConfig.type == 'plane' ):
            _location = ( aConfig.position.x, aConfig.position.y, aConfig.position.z )
            bpy.ops.mesh.primitive_plane_add(radius= aConfig.diameter , enter_editmode=True, location= _location, layers=_layers)
            myVec = Vector(( 0.0, 0.0, aConfig.h ))

            ob = bpy.context.active_object
            ob.data.materials.append( configMaterial )

            bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region=None, TRANSFORM_OT_translate={"value":myVec})
            bpy.ops.object.mode_set(mode='OBJECT')

        elif( aConfig.type == 'path' ):
            #bpy.ops.object.mode_set(mode='OBJECT')
            if 'pointA' in pConfig:
              pointA = Struct( **pConfig['pointA'] )

            if 'pointB' in pConfig:
              pointB = Struct( **pConfig['pointB'] )

            _xRelation = ''
            _yRelation = ''
            _zRelation = ''
            _difX = 0
            _difY = 0
            _difZ = 0

            if pointA.x < pointB.x:
                _xRelation = 'aB'
                difX = float( ( pointB.x - pointA.x ) / 2 )
            elif pointA.x == pointB.x:
                _xRelation = 'ab'
                difX = 0
            else:
                _xRelation = 'Ab'
                difX = -float( ( pointA.x - pointB.x ) / 2 )


            if pointA.y < pointB.y:
                _yRelation = 'aB'
                difY = float( ( pointB.y - pointA.y ) / 2 )
            elif pointA.y == pointB.y:
                _yRelation = 'ab'
                difY = 0
            else:
                _yRelation = 'Ab'
                difY = float( ( pointB.y - pointA.y ) / 2 )


            if pointA.z < pointB.z:
                _zRelation = 'aB'
                difZ = float( ( pointB.z - pointA.z ) / 2 )
            elif pointA.z == pointB.z:
                _zRelation = 'ab'
                difZ = 0
            else:
                _zRelation = 'Ab'
                difZ = -float( ( pointA.z - pointB.z ) / 2 )


            print( difX, difY, difZ )

            createdPath = bpy.ops.curve.primitive_nurbs_path_add(radius= aConfig.radius, view_align=False, enter_editmode=False, location= (0.0,0.0,0.0), rotation=(0.0, 0.0, 0.0), layers=_layers)
            _spline =  bpy.context.active_object.data.splines[0]

            #bevel_depth
            bpy.context.active_object.data.bevel_depth =  aConfig.radius #/ 10
            bpy.context.active_object.data.bevel_resolution =  3
            bpy.context.active_object.data.fill_mode =  'FULL'
            bpy.context.active_object.data.materials.append( configMaterial )
            #print( _spline.bevel_depth  )

            _wEdges = 1.0
            _wResolution = 1.0

            force =  aConfig.force

            if aConfig.weight == 'a':
                forceY = difY - (difY * force)
                forceZ = difZ - (difZ * force)
            elif  aConfig.weight == 'b':
                forceY = difY + (difY * force)
                forceZ = difZ + (difZ * force)
            else:
                forceY = difY
                forceZ = difZ

            _spline.points[0].co = Vector((pointA.x, pointA.y, pointA.z, _wEdges)) # x, y, z, weight
            _spline.points[1].co = Vector(( pointA.x, (pointA.y + difY) , (pointA.z + difZ), _wResolution))

            _spline.points[2].co = Vector(( (pointA.x + difX), (pointA.y + forceY) , (pointA.z + forceZ), _wResolution))

            _spline.points[3].co = Vector(( pointB.x, (pointB.y - difY) ,  (pointB.z - difZ), _wResolution))
            _spline.points[4].co = Vector((pointB.x, pointB.y, pointB.z, _wEdges)) # x, y, z, weight

        elif( aConfig.type == 'triangle' ):

            # verts1 = ((0, 3),(2.5, 0.5),(5, 1),(4.5, 3.5),(10.5, 2),(8, 10),(7, 4.5),(2, 6))
            # print( verts1 )
            verts = tuple(tuple(x) for x in aConfig.verts )
            # print( verts )
            bm = bmesh.new()
            for v in verts:
                bm.verts.new((v[0], v[1], v[2]))
            bm.faces.new( bm.verts )

            bm.normal_update()

            me = bpy.data.meshes.new("a")
            bm.to_mesh(me)

            ob = bpy.data.objects.new( aConfig.name , me)
            ob.data.materials.append( configMaterial )
            bpy.context.scene.objects.link(ob)
            bpy.context.scene.update()
