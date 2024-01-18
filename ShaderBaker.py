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
        
        # Drop down menu to select image texture
        layout.label(text="Select Image Texture:")
        layout.prop(context.scene, "selected_image_texture")
        
        # Button to add all selected image texture to all nodes
#        layout.operator()
    

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
        
            self.report({'INFO'}, 'Deleted all Image Texture Nodes')
            return {'FINISHED'}
        

class SelectImageTexture(bpy.types.Operator):
    '''
    Apply selected image texture to the image textures that were added
    '''


def register():
    '''
    Adds all UI elements
    '''
    
    bpy.utils.register_class(ShaderBakerPanel)
    bpy.utils.register_class(AddImageTextures)
    bpy.utils.register_class(SelectImageTextures)
    bpy.utils.register_class(DeleteImageTextures)
    
def unregister():
    '''
    removes all UI elements
    '''
    
    bpy.utils.unregister_class(ShaderBakerPanel)
    bpy.utils.unregister_class(AddImageTextures)
    bpy.utils.unregister_class(SelectImageTextures)
    bpy.utils.unregister_class(DeleteImageTextures)
        
def main():
    '''
    Main entry point to run code
    '''
    register()
    
if __name__ == "__main__":
    main()