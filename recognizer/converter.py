from math import sqrt

import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
import numpy as np


def part_of_img (img, tl):
    # print(tl)
    pts1   = np.float32([
        [tl['x0'], tl['y0']], [tl['x1'], tl['y1']],
        [tl['x2'], tl['y2']], [tl['x3'], tl['y3']]
    ])
    width  = sqrt((tl['x1']-tl['x0'])**2 + (tl['y1']-tl['y0'])**2)
    height = sqrt((tl['x3']-tl['x0'])**2 + (tl['y3']-tl['y0'])**2)
    pts2   = np.float32([
        [0, 0], [width, 0], [width, height], [0, height]
    ])
    print(pts1)
    print(pts2)
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (int(width), int(height)))
    # cv2.imshow("img", img)
    # print(cv2.waitKey(0))
    # cv2.imshow("img", dst)
    # print(cv2.waitKey(0))
    return dst
