import os


image_dir = "/home/junjie/Code/tianchi/guangdong/guangdong1_round1_train1_20190809/Label/JPEGImages"
out_dir = "/home/junjie/Code/tianchi/guangdong/guangdong1_round1_train1_20190809/Label/ImageSets/Main/"
train_name = 'train.txt'
val_name = 'val.txt'
train_val_name = 'train_val.txt'

images = os.listdir(image_dir)

train_ratio = 0.9
val_ration = 1 - train_ratio

pic_nums = len(images)
train_num = int(train_ratio * pic_nums)

train = open(out_dir+train_name, 'a') 
val = open(out_dir + val_name, 'a') 
tarin_val = open(out_dir +train_val_name, 'a') 

train.write(images[0][:-4])
tarin_val.write(images[0][:-4])

for i in range(1, train_num):
    train.write('\n'+images[i][:-4])
    tarin_val.write('\n'+images[i][:-4])

val.write(images[train_num][:-4])
tarin_val.write('\n'+images[train_num][:-4])
for i in range(train_num+1, pic_nums):
    val.write('\n'+images[i][:-4])
    tarin_val.write('\n'+images[i][:-4])


                

    