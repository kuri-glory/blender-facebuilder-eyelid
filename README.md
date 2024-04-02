# FaceBuilderの瞼の裏を生成

## Introduction
FaceBuidlerで作成した顔の瞼の裏側を作成します。<br>
<img src="https://github.com/kuri-glory/blender-facebuilder-eyelid/assets/165764811/4d8538a6-69e1-4693-984f-b9d745814ac3" width="600">

## 使い方
* check_eyelid_control_panel.pyをBlenderのスクリプトで実行
* 表示されるコントロールパネルの'left_eye'と'right_eye'をクリック
* 瞼の裏側にすり鉢状の面ができている

※ この後にCtrl＋Rして平滑化する

## 制約条件
* FaceBuilderのHighpolyで作られたメッシュであること
* 'check_eyelid_control_panel.py'にハードコードされたインデックス番号と目の外周のインデックスが同じであること
* うまく生成されない場合は手動で作成する
