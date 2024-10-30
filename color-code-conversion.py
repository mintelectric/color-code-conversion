import bpy

bl_info = {
    "name": "Color Code Conversion",
    "author": "Mintelectric",
    "description": "The add-on for RGB to HEX color code conversion.",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar",
    "category": "User Interface",
}

def color_code(r, g, b):
    r = hex(r)[2:].zfill(2)
    g = hex(g)[2:].zfill(2)
    b = hex(b)[2:].zfill(2)
    return f"#{r}{g}{b}"

class OBJECT_PT_color_panel(bpy.types.Panel):
    bl_label = "Color Code"
    bl_idname = "OBJECT_PT_color_panel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Color'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "red")
        layout.prop(scene, "green")
        layout.prop(scene, "blue")

        color = color_code(scene.red, scene.green, scene.blue)
        layout.label(text=f"HEX: {color}")

def register():
    bpy.utils.register_class(OBJECT_PT_color_panel)
    bpy.types.Scene.red = bpy.props.IntProperty(name="Red", default=0, min=0, max=255)
    bpy.types.Scene.green = bpy.props.IntProperty(name="Green", default=0, min=0, max=255)
    bpy.types.Scene.blue = bpy.props.IntProperty(name="Blue", default=0, min=0, max=255)

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_color_panel)
    del bpy.types.Scene.red
    del bpy.types.Scene.green
    del bpy.types.Scene.blue

if __name__ == "__main__":
    register()
