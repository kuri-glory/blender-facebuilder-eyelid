import bpy
from bpy.props import *

# 自作モジュールを使用可能にする
import sys, os
# スクリプトのファイルパスを取得
script_filepath = bpy.context.space_data.text.filepath
print(f'module path: {os.path.dirname(os.path.abspath(script_filepath))}')
sys.path.append(os.path.dirname(script_filepath))
print(sys.path)

from utilities.modify_coord import ModifyCo


object_name = 'FBHead'
left_eye_index = [4327,4359,4372,4360,4399,4329,4357,4332,4375,4356,4345,4392,4347,4398,
4326,4405,4377,4352,4275,4348,4340,
4370,4338,4403,4337,4362,4368,4380,4336,4366,4371,4364,4373,4361,4386,4330,4383,4384,4323,
4397,4374,4363,4346,4341,4335,4367,4325,4354,]

right_eye_index = [4276,4385,4410,4328,4412,4331,4381,4387,4400,4395,4339,4394,4415,4376,4344,4391,4369,4353,4414,4401,4324,4411,4342,4378,4393,4358,4379,
4334,4322,4382,4402,4408,4343,4396,4351,4365,4407,4333,4350,4388,4413,4406,4409,4390,4404,4389,4349,4355,]

# 頂点から瞼の裏を生成するクラス
co = ModifyCo()

#
# OT_Select_Vertex_Button
#
class OT_Select_Vertex_Button(bpy.types.Operator):
    bl_idname = "ctrl_r.id"
    bl_label = "Ctrl+R"
    bl_options = {'REGISTER', 'UNDO'}

    #パラメータ用のプロパティ
    size: IntProperty(default=0, min=0, max=100, options={'HIDDEN'})
    #パラメータ用のプロパティ
    location: StringProperty(default='center', options={'HIDDEN'})

    def execute(self, context):        
        # オブジェクト名からオブジェクトを取得
        obj = bpy.data.objects.get(object_name)

        # 左右眼の頂点に対してCtrl＋Rする
        co.ctrlR_selected_vertex(obj)

        return{'FINISHED'}


#
# OT_left_eyelid_Button
#
class OT_left_eyelid_Button(bpy.types.Operator):
    bl_idname = "left_eyelid.id"
    bl_label = "left_eye"
    bl_options = {'REGISTER', 'UNDO'}

    #パラメータ用のプロパティ
    size: IntProperty(default=0, min=0, max=100, options={'HIDDEN'})
    #パラメータ用のプロパティ
    location: StringProperty(default='center', options={'HIDDEN'})

    def execute(self, context):        
        # オブジェクト名からオブジェクトを取得
        obj = bpy.data.objects.get(object_name)

        # 指定したインデックス全てを選択
        co.select_vertex(obj, left_eye_index)

        # 押し出して拡大
        co.extrude_vertex(obj, 0.007)
        co.scale_vertex(obj, (1.2, 1, 2.25))
        # 平行に押し出し
        co.extrude_vertex(obj, 0.005)
        # s0で背面に蓋をする
        co.extrude_vertex(obj, 0.0000001)
        co.scale_vertex(obj, (0, 0, 0))

        return{'FINISHED'}

#
# OT_right_eyelid_Button
#
class OT_right_eyelid_Button(bpy.types.Operator):
    bl_idname = "right_eyelid.id"
    bl_label = "right_eye"
    bl_options = {'REGISTER', 'UNDO'}

    #パラメータ用のプロパティ
    size: IntProperty(default=0, min=0, max=100, options={'HIDDEN'})
    #パラメータ用のプロパティ
    location: StringProperty(default='center', options={'HIDDEN'})

    def execute(self, context):        
        # オブジェクト名からオブジェクトを取得
        obj = bpy.data.objects.get(object_name)

        # 指定したインデックス全てを選択
        co._ctrlR_selected_vertices(obj)

        # 指定したインデックス全てを選択
        co.select_vertex(obj, right_eye_index)

        # 押し出して拡大
        co.extrude_vertex(obj, 0.007)
        co.scale_vertex(obj, (1.2, 1, 2.25))
        # 平行に押し出し
        co.extrude_vertex(obj, 0.005)
        # s0で背面に蓋をする
        co.extrude_vertex(obj, 0.0000001)
        co.scale_vertex(obj, (0, 0, 0))

        return{'FINISHED'}
    


#
# UI_Panel
#
class EYELID_PT_UI(bpy.types.Panel):
  bl_label = "Eye lid"
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "CheckEyelid"
  
  def draw(self, context):
    self.layout.operator("left_eyelid.id")
    self.layout.operator("right_eyelid.id")
    # self.layout.operator("ctrl_r.id")

#
# register classs
#
classs = [
  EYELID_PT_UI,
  OT_Select_Vertex_Button,
  OT_left_eyelid_Button,
  OT_right_eyelid_Button,
]

#
# register
#
def register():
  for c in classs:
    bpy.utils.register_class(c)
    
  bpy.types.Scene.tutorial_comment = StringProperty(default = "")

#
# unregister()
#    
def unregister():
  for c in classs:
    bpy.utils.register_class(c)
    
  del bpy.types.Scene.tutorial_comment

#
# script entry
#    
if __name__ == "__main__":
  register()