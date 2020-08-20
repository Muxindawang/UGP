#-*-coding:utf-8-*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

imgs_path = 'images/'
save_path = 'erase/'
labels_path = 'labels/'
img_names = os.listdir(imgs_path)

probability=1.0
sl, sh = 0.02, 0.3    # 矩形面积上下阈值
r1 = 0.3  # 最小高宽比



for img_name in img_names:
    img_path = imgs_path + img_name

    src1 = cv2.imread(img_path)
    # cv2.namedWindow('img_orig', cv2.WINDOW_NORMAL)
    # cv2.imshow('img_orig', src1)
    res = np.uint8(np.clip((2 * (np.int16(src1) - 60) + 50), 0, 255))
    tmp = np.hstack((src1, res))  # 两张图片横向合并显示
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', tmp)
    cv2.waitKey(0)






#
# h, w, c = src1.shape
# dst = np.zeros((h, w, 3), np.int64)
# # cv2.imshow('dst', dst)
# alpha = 1
# print(src1.shape)
# dst[900:920, 600: 690] = 0
# # beta = 0
# #
# # for i in range(h):
# #     for j in range(w):
# #         b, g, r = src1[i, j]
# #         # print(b, g, r)
# #         # print(dst[i][j])
# #         dst[i, j][0] = int(b*alpha + beta)
# #         dst[i, j][1] = int(g*alpha + beta)
# #         dst[i, j][2] = int(r*alpha + beta)
# cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()