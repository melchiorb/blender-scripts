import bpy

if len(bpy.context.selected_objects) == 2:
	source = bpy.context.selected_objects[1]
	dest = bpy.context.active_object

	for v in bpy.context.selected_objects:
		if v is not dest:
			source = v
			break
	
	print("Source: ", source.name)
	print("Destination: ", dest.name)
	
	if source.data.shape_keys is None:
		print("Source object does not have shape keys!") 
	else:
		for idx in range(1, len(source.data.shape_keys.key_blocks)):
			shape_key = source.active_shape_key
			print("Copying shape key: ", shape_key.name)

			source.active_shape_key_index = idx
			bpy.ops.object.shape_key_transfer()
else:
	print("Select source object first, destination object last!")
