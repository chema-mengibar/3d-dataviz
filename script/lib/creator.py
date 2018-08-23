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

            # https://docs.blender.org/api/blender_python_api_2_63_7/bpy.ops.mesh.html
            bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region=None, TRANSFORM_OT_translate={"value":myVec})
            bpy.ops.object.mode_set(mode='OBJECT')
