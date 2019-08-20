from mmdet.apis import init_detector, inference_detector, show_result
import mmcv

config_file = '/home/junjie/Code/tianchi/guangdong/mmdetection/configs/cloth/faster_rcnn_r50_caffe_c4_1x.py'
checkpoint_file = '/home/junjie/Code/tianchi/guangdong/mmdetection/work_dirs/cloth_faster_rcnn_r50_caffe_c4_1x/latest.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a single image and show the results
img = '/home/junjie/Code/tianchi/guangdong/guangdong1_round1_train1_20190818/defect_Images/00a6cf1233b1cf170835381106.jpg'  # or img = mmcv.imread(img), which will only load it once
result = inference_detector(model, img)
show_result(img, result, model.CLASSES)

print("fuck_out")