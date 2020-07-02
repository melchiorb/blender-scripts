import bpy

search = ""
replace = ""

prefix = ""
suffix = ""

for key in bpy.context.object.data.shape_keys.key_blocks:
    key.name = prefix + key.name.replace(search, replace) + suffix
