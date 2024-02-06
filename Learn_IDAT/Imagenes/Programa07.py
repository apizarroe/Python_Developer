import cv2
import numpy as np

cap = cv2.VideoCapture("http://192.168.1.103:4747/video")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.rectangle(frame,(119,93),(370,415),(0,0,255),3)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Nombre: Aldo",(425,20),font,0.65,(0,0,255),1,cv2.LINE_AA)
    cv2.putText(frame, "Apellido: Pizarro",(425,40),font,0.65,(0,0,255),1,cv2.LINE_AA)
    cv2.putText(frame, "Edad: 37",(425,60),font,0.65,(0,0,255),1,cv2.LINE_AA)
    cv2.putText(frame, "Codigo: A17202187",(425,80),font,0.65,(0,0,255),1,cv2.LINE_AA)
    
    cv2.imshow('camara',frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()