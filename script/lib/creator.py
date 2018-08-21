import bpy
import bmesh
import json

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        
class Generic:
    def __init__( self, **dict ):
        self.__dict__.update(dict)
        return self

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
            bmesh.ops.create_uvsphere(bm, u_segments= aConfig.u , v_segments= aConfig.v, diameter= aConfig.diameter)
            bm.to_mesh(mesh)
            bm.free()
            
            #bpy.ops.object.modifier_add(type= aConfig.modifier )
            #bpy.ops.object.shade_smooth()
