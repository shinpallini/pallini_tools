import bpy

bl_info = {
    "name": "",
    "author": "ぱりーに(pallini)",
    "version": (0, 1),
    "blender": (2, 81, 1),
    "location": "3Dビューポート > Pallini_Tools",
    "description": "ぱりーにが作ったアドオンたちです",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

class PalliniTools_OT_SetResolutionFromBG(bpy.types.Operator):

    bl_idname = "pallinitools.setresolutionfrombg"
    bl_label = "SetResolutionFromBG"
    bl_description = "下絵のピクセル数に合わせて解像度を設定する"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        cam_name = context.scene.camera.name
        active_cam = bpy.data.cameras[cam_name]
        images = active_cam.background_images.values()
        
        if images:
            bg_image = images[0].image

            bpy.context.scene.render.resolution_x = bg_image.size[0] + bg_image.size[0]%2
            bpy.context.scene.render.resolution_y = bg_image.size[1] + bg_image.size[1]%2

            print("Script Executed")
        else:
            bpy.context.scene.render.resolution_x = 1920
            bpy.context.scene.render.resolution_y = 1080
        return {'FINISHED'}

class PalliniTools_PT_CustomPanel(bpy.types.Panel):

    bl_label = "Pallini_ToolList"         # パネルのヘッダに表示される文字列
    bl_space_type = 'VIEW_3D'           # パネルを登録するスペース
    bl_region_type = 'UI'               # パネルを登録するリージョン
    bl_category = "Pallini_Tools "        # パネルを登録するタブ名
    bl_context = "objectmode"           # パネルを表示するコンテキスト

    # 本クラスの処理が実行可能かを判定する
    @classmethod
    def poll(cls, context):
        # オブジェクトが選択されているときのみメニューを表示させる
        for o in bpy.data.objects:
            if o.select_get():
                return True
        return False
    
    # ヘッダーのカスタマイズ
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='PLUGIN')

    # メニューの描画処理
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # ボタンを追加
        layout.label(text="解像度を下絵にフィット:")
        layout.operator(PalliniTools_OT_SetResolutionFromBG.bl_idname, text="実行")

classes = [
    PalliniTools_OT_SetResolutionFromBG,
    PalliniTools_PT_CustomPanel,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()