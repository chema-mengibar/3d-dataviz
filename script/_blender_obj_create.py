import os
import sys
import bpy
import fnmatch


orig = bpy.data.objects['cube']

ob = bpy.context.object
obs = []
scene = bpy.context.scene


foo_objs = [obj for obj in scene.objects if obj.name.startswith("cube.")]

def set_position(frame):
	i = 0
	clear = orig["position"]
	for ob in foo_objs:
		ob.location.x = 0
		ob.location.y = clear * i
		ob.location.z = 0
		i += 1


frame = scene.frame_current
set_position(frame)
