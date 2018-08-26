import bpy
import bmesh
import fnmatch

class Selector( object ):
    def __init__( self ):
        print( "selector init" )
        self.scene = bpy.context.scene

    def removeSelectedObjects( self ):
        bpy.ops.object.delete()

    def selectByName( self, partName ):
        foo_objs = [obj for obj in self.scene.objects if obj.name.startswith( partName )]
        for ob in foo_objs:
            ob.select = True

    def selectByMaterial( self, partName, partMaterial, intLayer ):
        foo_objs = [obj for obj in self.scene.objects if obj.name.startswith( partName )]
        for ob in foo_objs:
            for m in ob.material_slots:
                if partMaterial in m.name:
                    ob.select = True
                    #ob.layers[ intLayer ] = True

    def locationSelectedObjects( self ):
        listItems = {}
        selectedObjects = bpy.context.selected_objects
        for item in selectedObjects:
            print( item.name )
            itemData = {
                'name': item.name,
                'location': item.location
            }
            listItems[ item.name ]= itemData 
        return listItems
