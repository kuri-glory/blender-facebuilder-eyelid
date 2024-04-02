import bpy
from bpy_extras.object_utils import world_to_camera_view
import bmesh
from mathutils import Vector

import os
import math


class ModifyCo:
    def __init__(self) -> None:
        pass
    
    # 選択された頂点を取得
    def get_active_vertices(self, obj):
        return [vert.index for vert in obj.data.vertices if vert.select]
    
    # 指定したインデックスの頂点を選択
    def select_vertex(self, obj, select_index):
        self._select_all_vertex(obj, select_index)

    # 拡大
    def scale_vertex(self, obj, scale_vector=(1,1,1)):
        self._scale_selected_vertices(obj, scale_vector=scale_vector)

    # 平行に押し出し
    def extrude_vertex(self, obj, distance=0.005):
        self._extrude_selected_vertices(obj, distance)

    # Ctrl＋Rして平滑化
    def ctrlR_selected_vertex(self, obj):
        self._ctrlR_selected_vertices(obj)



    # 指定インデックス選択
    def _select_all_vertex(self, obj, vertex_indices):
        # 対象オブジェクトをアクティブに設定
        bpy.context.view_layer.objects.active = obj

        # 編集モードに変更
        bpy.ops.object.mode_set(mode='EDIT')

        # すべての頂点の選択を解除
        bpy.ops.mesh.select_all(action='DESELECT')

        # オブジェクトモードに戻して再度編集モードへ - 頂点データを更新
        bpy.ops.object.mode_set(mode='OBJECT')

        # 指定した頂点を選択
        for v_idx in vertex_indices:
            obj.data.vertices[v_idx].select = True

        # 編集モードに戻す
        bpy.ops.object.mode_set(mode='EDIT')
    

    # 頂点を拡大
    def _scale_selected_vertices(self, obj, scale_vector=(1.0, 1.0, 1.0)):
        bpy.ops.transform.resize(value=scale_vector, orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)

    # Ctrl＋Rして平滑化（左右眼の両方とも実行）
    def _ctrlR_selected_vertices(self,obj):
        # 左眼
        bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":29183, "mesh_select_mode_init":(True, False, False)}, TRANSFORM_OT_edge_slide={"value":0.8, "single_side":False, "use_even":False, "flipped":True, "use_clamp":True, "mirror":True, "snap":False, "snap_elements":{'VERTEX'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "correct_uv":True, "release_confirm":False, "use_accurate":False, "alt_navigation":False})

        # 右眼
        bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":29556, "mesh_select_mode_init":(True, False, False)}, TRANSFORM_OT_edge_slide={"value":0.8, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":True, "snap":False, "snap_elements":{'VERTEX'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "correct_uv":True, "release_confirm":False, "use_accurate":False, "alt_navigation":False})

    # 押し出し
    def _extrude_selected_vertices(self, obj, distance):
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, distance, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, True, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'VERTEX'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "alt_navigation":True, "use_automerge_and_split":False})

    # 平面に蓋をする（scale0）    
    def _extrude_scale0_selected_vertices(self, obj):
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_resize={"value":(0, 0, 0), "mouse_dir_constraint":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "center_override":(0, 0, 0), "release_confirm":False, "use_accurate":False, "alt_navigation":True})