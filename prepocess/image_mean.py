import os
import cv2
import numpy

image_dir = "/home/junjie/Code/tianchi/guangdong/mmdetection/data/cloth/JPEGImages"

images = os.listdir(image_dir)
mean = [0,0,0]
std = [0,0,0]

R = 0
G = 0
B = 0


for i,img_name in enumerate(images):
    img = cv2.imread(os.path.join(image_dir, img_name))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    for j in range(3):
        mean[j] = mean[j] + img[:, :, j].mean()
        std[j] = std[j] + img[:, :, j].std()

    print(i)

length = len(images)
print("fuck_out:{},{}".format(numpy.array(mean)/length, numpy.array(std)/length))
    
# 90.88209569740208, 89.29711736905227, 95.5343708279186