#-*-coding:utf-8-*-
import random
import cv2
import torch
from torchvision import transforms
import os
import shutil
from PIL import Image
import random
import math
import numpy as np
import torch
# 读取整个文件夹图片 对其进行随机擦除
imgs_path = 'images/'
save_path = 'erase/'
labels_path = 'labels/'
img_names = os.listdir(imgs_path)

probability=1.0
sl, sh = 0.02, 0.3    # 矩形面积上下阈值
r1 = 0.3  # 最小高宽比



for img_name in img_names:
    img_path = imgs_path + img_name
    print(img_path)
    img = cv2.imread(img_path)
    h, w, c = img.shape
    # 要设置剪切在矩形框内
    if img_path.endswith("jpg"):
        label_files = labels_path + img_name.replace('jpg', 'txt')
    elif img_path.endswith("JPG"):
        label_files = labels_path + img_name.replace('JPG', 'txt')

    with open(label_files, 'r') as f:
        labels = [x.split() for x in f.read().splitlines()]
    # s是图片中目标的类别 中心 高宽

    for i, label in enumerate(labels):

        x, y, w_label, h_label = label[1:]
        x, y, w_label, h_label = float(x), float(y), float(w_label), float(h_label)

        h_label *= h
        w_label *= w
        x *= w
        y *= h

        x1, x2 = int(x - w_label / 2), int(x + w_label/ 2)
        y1, y2 = int(y - h_label / 2), int(y + h_label/ 2)

        # 开始擦除
        area = h_label * w_label
        target_area = random.uniform(sl, sh) * area

        aspect_ratio = random.uniform(r1, 1/r1)

        h_erase = int(round(math.sqrt(target_area * aspect_ratio)))
        w_erase = int(round(math.sqrt(target_area / aspect_ratio)))
        # 擦除矩形的 高宽
        if w_erase < w_label and h_erase < h_label:
            x_ = random.randint(0, int(w_label - w_erase))
            y_ = random.randint(0, int(h_label - h_erase))
            # x_, y_ 是放在的位置
            print("\nlabel的位置是： x1 = ", x1, '\ty1 = ', y1, "\tx2 = ", x2, '\ty2= ', y2,'\tw = ', w_label, '\th = ', h_label)
            print('擦除的大小是： ', w_erase,'\t', h_erase, '\n')
            print("擦除的位置为： x1 =", x1+x_ , '\ty1=', y1+y_, "\tx2=", x1+x_+w_erase,"\ty2=", y1+y_+h_erase)
            img[y1+y_:y1+y_+h_erase , x1+x_:x1+x_+w_erase] = 125
    if img_name.endswith("jpg"):
        img_name = img_name.split(".")[0] + "earse" + '.jpg'
        label_name = img_name.replace('jpg', 'txt')
    else:
        img_name = img_name.split(".")[0] + "earse" + '.JPG'
        label_name = img_name.replace('JPG', 'txt')
    name_new = "erase" + os.sep + img_name
    label_new = 'erase_label' + os.sep + label_name
    cv2.imwrite(name_new, img)
    shutil.copyfile(label_files, label_new)

    # cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    # cv2.imshow('img',img)
    # cv2.waitKey(0)

    # cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    # cv2.imshow('img',img)
    # cv2.waitKey(0)



