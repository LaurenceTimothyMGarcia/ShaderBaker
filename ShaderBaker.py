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
        
        layout.operator("add_image_textures.execute", text="Add Image Textures")
        layout.operator("select_image_textures.execute", text="Select All Image Texture Nodes")
        
        # If obj selected get materials
        if bpy.context.active_object:
            layout.prop_search(bpy.context.active_object, "active_material", bpy.data, "materials", text="Select Material")
            
            
    

class AddImageTextures(bpy.types.Operator):
    '''
    Adding image textures
    '''
    bl_idname = "add_image_textures.execute"
    bl_label = "Add Image Textures"
    
    def execute(self, context):
        self.report({'INFO'}, 'Add Image Textures Executed')
        return {'FINISHED'}

class SelectImageTextures(bpy.types.Operator):
    '''
    Selecting image texture nodes in an object
    '''
    bl_idname = "select_image_textures.execute"
    bl_label = "Select All Image Texture Nodes"
    
    def execute(self, context):
        self.report({'INFO'}, 'Selected all Image Texture Nodes')
        return {'FINISHED'}
        

def register():
    '''
    Adds all UI elements
    '''
    
    bpy.utils.register_class(ShaderBakerPanel)
    bpy.utils.register_class(AddImageTextures)
    bpy.utils.register_class(SelectImageTextures)
    
def unregister():
    '''
    removes all UI elements
    '''
    
    bpy.utils.unregister_class(ShaderBakerPanel)
    bpy.utils.unregister_class(AddImageTextures)
    bpy.utils.unregister_class(SelectImageTextures)
        
def main():
    '''
    Main entry point to run code
    '''
    
    register()
    
#    shader_baker = ShaderBaker(blend.context.scene)
    
#    print("Shader Baker Tool")
    
if __name__ == "__main__":
    main()