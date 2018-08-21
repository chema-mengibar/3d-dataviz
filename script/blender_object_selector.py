import bpy
import bmesh
import fnmatch

'''
orig = bpy.data.objects['cube']
ob = bpy.context.object
obs = []

'''

scene = bpy.context.scene

#clear = orig["position"]
# ob.location.x = 0
'''
for ob in foo_objs:
	ob.select = True

def selectByMaterial_test( partMaterial ):
    obj_list = []
    for o in bpy.data.objects:
        for m in o.material_slots:
            if "text" in m.name:
                obj_list.append(o)
    return obj_list
'''

# https://blender.stackexchange.com/questions/34319/how-to-add-object-to-a-specific-layer-with-python

def removeSelectedObjects( ):
    bpy.ops.object.delete()

def selectByName( partName ):
    foo_objs = [obj for obj in scene.objects if obj.name.startswith( partName )]
    for ob in foo_objs:
        ob.select = True

def selectByMaterial( partName, partMaterial, intLayer ):
    foo_objs = [obj for obj in scene.objects if obj.name.startswith( partName )]
    for ob in foo_objs:
        for m in ob.material_slots:
            if partMaterial in m.name:
                ob.select = True
                #ob.layers[ intLayer ] = True


selectByMaterial( "Basic_Sphere", "yellow", 1 )
