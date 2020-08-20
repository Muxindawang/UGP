#-*-coding:utf-8-*-
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


images_path = 'images/'
labels_path = 'labels/'
save_path = 'flip/'

images_name = os.listdir(images_path)

for image_name in images_name:
    # 先对图片进行反转  然后对标签进行反转
    img_path = images_path + image_name  # 这个是图片的路径
    img = cv2.imread(img_path)

    img = cv2.flip(img, 1)

    # 处理标签
    if image_name.endswith('jpg'):
        label_name = image_name.replace('jpg', 'txt')
    else:
        label_name = image_name.replace('JPG', 'txt')
    label_path = labels_path + label_name
    with open(label_path, 'r') as f:
        labels = [(x.split()) for x in f.read().splitlines()]

    # 保存的路径
    if image_name.endswith("jpg"):
        image_name = image_name.split(".")[0] + "flip" + '.jpg'
        bel_name = image_name.replace('jpg', 'txt')
    else:
        image_name = image_name.split(".")[0] + "flip" + '.JPG'
        bel_name = image_name.replace('JPG', 'txt')

    img_name = save_path + image_name
    label_new = 'flip_label' + os.sep + bel_name
    cv2.imwrite(img_name, img)

    for label in labels:
        label[1] = 1 - float(label[1])
        label[1] = round(label[1], 6)
        file = open(label_new, 'a')
        for i, b in enumerate(label):
            file.write(str(b) + ' ')
            if i != 0 and i % 4 == 0: file.write('\n')



