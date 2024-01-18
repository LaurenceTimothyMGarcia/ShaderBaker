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
        
        layout.operator("shader_baker.execute", text="Add Image Textures")
        
        # If obj selected get materials
        if bpy.context.active_object:
            layout.prop_search(bpy.context.active_object, "active_material", bpy.data, "materials", text="Select Material")
            
            
    

class ShaderBaker(bpy.types.Operator):
    '''
    Primary class for the shader baker tool
    '''
    bl_idname = "shader_baker.execute"
    bl_label = "Bake Shader"
    
    def execute(self, context):
        self.report({'INFO'}, 'Shader Baking Executed')
        return {'FINISHED'}
        
        

def register():
    bpy.utils.register_class(ShaderBakerPanel)
    bpy.utils.register_class(ShaderBaker)
    
def unregister():
    bpy.utils.unregister_class(ShaderBakerPanel)
    bpy.utils.unregister_class(ShaderBaker)
        
def main():
    '''
    Main entry point to run code
    '''
    
    register()
    
#    shader_baker = ShaderBaker(blend.context.scene)
    
#    print("Shader Baker Tool")
    
if __name__ == "__main__":
    main()