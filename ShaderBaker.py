import bpy

class ShaderBakerPanel(bpy.types.Panel):
    '''
    User Interface for the ShaderBaker tool
    '''
    bl_label = "Shader Baker"
    bl_idname = "PT_ShaderBakerPanel"
    
    # Defines where we place this panel
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"
    
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Shader Baker Panel")
        
        # Buttons for adding, selecting, and deleting image textures
        layout.operator("add_image_textures.execute", text="Add Image Textures Nodes")
        layout.operator("select_image_textures.execute", text="Select All Image Texture Nodes")
        layout.operator("delete_image_textures.execute", text="Delete All Image Texture Nodes")    
        
        # Dropdown menu for selecting an image
        layout.label(text="Select Image")
        row = layout.row()
        row.operator("refresh_image_menu.execute", text="Refresh")
        row.prop(context.scene, "selected_image", text="")

        # Button to apply selected image texture to all nodes
        layout.operator("apply_image_texture.execute", text="Apply Selected Image Texture")
    

class AddImageTextures(bpy.types.Operator):
    '''
    Adding image textures
    '''
    bl_idname = "add_image_textures.execute"
    bl_label = "Add Image Textures"
    
    def execute(self, context):
        # Check if object is selected
        if bpy.context.active_object:
            # Get each maerial in the object
            for mat_slot in bpy.context.active_object.material_slots:
                material = mat_slot.material
                
                if material:
                    # Create image texture node
                    image_texture_node = material.node_tree.nodes.new(type='ShaderNodeTexImage')
                    image_texture_node.location.x = 200  # Adjust the x-coordinate for node spacing
                    image_texture_node.location.y = 0
                    image_texture_node.label = f"Image Texture Bake"
                else:
                    self.report({'ERROR'}, 'No material found')
                    return {'CANCELLED'}
            
            self.report({'INFO'}, 'Image Texture Nodes Added')
            return {'FINISHED'}
        
        else:
            self.report({'ERROR'}, 'No active object selected')
            return {'CANCELLED'}
    

class SelectImageTextures(bpy.types.Operator):
    '''
    Selecting image texture nodes in an object
    '''
    bl_idname = "select_image_textures.execute"
    bl_label = "Select All Image Texture Nodes"
    
    def execute(self, context):
        
        # Check if object is selected
        if bpy.context.active_object:
            
            # Look at each material in active obj
            for mat_slot in bpy.context.active_object.material_slots:
                material = mat_slot.material
                
                if material:
                    # Deselect all nodes but img texture node
                    node_tree = material.node_tree
                    
                    for node in node_tree.nodes:
                        if node.type == 'TEX_IMAGE' and node.label == 'Image Texture Bake':
                            node.select = True
                        else:
                            node.select = False
                else:
                    self.report({'ERROR'}, 'No material found')
                    return {'CANCELLED'}
        
            self.report({'INFO'}, 'Selected all Image Texture Nodes')
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'No active object selected')
            return {'CANCELLED'}

class DeleteImageTextures(bpy.types.Operator):
    '''
    Delete all image texture nodes
    '''
    bl_idname = "delete_image_textures.execute"
    bl_label = "Delete All Image Texture Nodes"
    
    def execute(self, context):
        if bpy.context.active_object:
            for mat_slot in bpy.context.active_object.material_slots:
                material = mat_slot.material
                
                if material:
                    node_tree = material.node_tree
                    
                    # ID node with Image Texture Bake Name and delete
                    for node in node_tree.nodes:
                        if node.type == 'TEX_IMAGE' and node.label == 'Image Texture Bake':
                            node_tree.nodes.remove(node)
                else:
                    self.report({'ERROR'}, 'No material found')
                    return {'CANCELLED'}
        
            self.report({'INFO'}, 'Deleted all Image Texture Nodes')
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'No active object selected')
            return {'CANCELLED'}
        

class ApplySelectedImageTexture(bpy.types.Operator):
    '''
    Apply selected image texture to the image textures that were added
    '''
    bl_idname = "apply_image_texture.execute"
    bl_label = "Apply Selected Image Texture to Image Texture Nodes"

    def execute(self, context):
        selected_image = context.scene.selected_image

        if bpy.context.active_object:
            for mat_slot in bpy.context.active_object.material_slots:
                material = mat_slot.material
                
                if material:
                    node_tree = material.node_tree
                    
                    # Convert the selected_image to an integer
                    selected_index = int(selected_image)

                    # Iterate over nodes to find the image texture nodes
                    for node in node_tree.nodes:
                        if node.type == 'TEX_IMAGE' and node.label == 'Image Texture Bake':
                            # Apply the selected image texture to the node
                            node.image = bpy.data.images[selected_index]
                else:
                    self.report({'ERROR'}, 'No material found')
                    return {'CANCELLED'}
        
            self.report({'INFO'}, 'Applied selected Image Texture to Image Texture Nodes')
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'No active object selected')
            return {'CANCELLED'}


class RefreshImageMenu(bpy.types.Operator):
    '''
    Refresh the image menu
    '''
    bl_idname = "refresh_image_menu.execute"
    bl_label = "Refresh Image Menu"

    def execute(self, context):
        bpy.types.Scene.selected_image_items = bpy.props.EnumProperty(
            items=[(str(i), img.name, "") for i, img in enumerate(bpy.data.images)],
            description="Select Image",
            update=update_image_items
        )
        self.report({'INFO'}, 'Refreshed Image List')
        return {'FINISHED'}

def update_image_items(self, context):
    if context.scene.refresh_image_menu_toggle:
        self.items = [(str(i), img.name, "") for i, img in enumerate(bpy.data.images)]
        

def register():
    '''
    Adds all UI elements
    '''
    bpy.types.Scene.selected_image = bpy.props.EnumProperty(
        items=[(str(i), img.name, "") for i, img in enumerate(bpy.data.images)],
        description="Select Image",
        update=update_image_items
    )
    
    bpy.utils.register_class(ShaderBakerPanel)
    bpy.utils.register_class(AddImageTextures)
    bpy.utils.register_class(SelectImageTextures)
    bpy.utils.register_class(DeleteImageTextures)
    bpy.utils.register_class(ApplySelectedImageTexture)
    bpy.utils.register_class(RefreshImageMenu)
    
def unregister():
    '''
    removes all UI elements
    '''
    del bpy.types.Scene.selected_image
    
    bpy.utils.unregister_class(ShaderBakerPanel)
    bpy.utils.unregister_class(AddImageTextures)
    bpy.utils.unregister_class(SelectImageTextures)
    bpy.utils.unregister_class(DeleteImageTextures)
    bpy.utils.unregister_class(ApplySelectedImageTexture)
    bpy.utils.unregister_class(RefreshImageMenu)
        
def main():
    '''
    Main entry point to run code
    '''
    register()
    
if __name__ == "__main__":
    main()