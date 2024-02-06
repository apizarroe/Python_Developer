import cv2
import numpy as np

cap = cv2.VideoCapture("http://192.168.1.103:4747/video")

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(width,height)