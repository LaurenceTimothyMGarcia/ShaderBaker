import bpy as blend

class ShaderBaker:
    '''
    Primary class for the shader baker tool
    '''
    
    def __init__(self, scene):
        self.scene = scene
        
def main():
    '''
    Main entry point to run code
    '''
    
    shader_baker = ShaderBaker(blend.context.scene)
    
    print("Shader Baker Tool")
    
if __name__ == "__main__":
    main()