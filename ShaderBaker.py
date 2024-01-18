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
    

class ShaderBaker:
    '''
    Primary class for the shader baker tool
    '''
    
    def __init__(self, scene):
        self.scene = scene
        
def register():
    bpy.utils.register_class(ShaderBakerPanel)
    
def unregister():
    bpy.utils.unregister_class(ShaderBakerPanel)
        
def main():
    '''
    Main entry point to run code
    '''
    
    register()
    
#    shader_baker = ShaderBaker(blend.context.scene)
    
#    print("Shader Baker Tool")
    
if __name__ == "__main__":
    main()