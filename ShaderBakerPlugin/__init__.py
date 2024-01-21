bl_info = {
  "name": "Shader Baker",
  "blender": (3, 0, 0),
  "author": "@LaurenceTimothyMGarcia on GitHub",
  "description": "Automates the setup for the baking process when working with shader nodes in Blender.",
  "version": (1, 0, 0),
  "location": "Properties -> Render -> Underneath Bake",
  "doc_url": "https://github.com/LaurenceTimothyMGarcia/ShaderBaker",
  "category": "Bake",
}

if "bpy" in locals():
  import importlib
  importlib.reload(ShaderBaker)
else:
  from . import ShaderBaker

def register():
  ShaderBaker.register()

def unregister():
  ShaderBaker.unregister()

if __name__ == "__main__":
  register()