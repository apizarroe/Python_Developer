import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) #dibujar fondo negro de 512 x 512
#linea(imagen,inicio,fin,color(B,G,R),grosor)
img1 = cv2.line(img,(0,0),(512,512),(255,0,0),3) #dibujar linea1
img2 = cv2.line(img,(100,0),(302,400),(0,255,0),5) #dibujar linea2
cv2.imshow('linea',img1)
cv2.imshow('linea',img2)
cv2.waitKey()
