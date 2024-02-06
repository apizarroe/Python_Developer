import cv2 #libreria de imagenes

#cap = cv2.VideoCapture(0) #busca las webcam disponibles
#cap = cv2.VideoCapture("http://192.168.1.101:4747/video") #DroidCam
cap = cv2.VideoCapture("C:/Users/Aldo Pizarro/Desktop/Idat_Clases/CicloV/ProcesamientoImg/VID_20160617_211751985.mp4") #Archivo Video

while True: #Bucle infinito
    ret, frame = cap.read() #Leer camara
    cv2.imshow('video', frame) #Mostramos camara
    k = cv2.waitKey(1) #Espera 1 seg
    
    if k == 27: #Si tecla 'esc'
        break
    if k == ord('s'): #Si tecla 's'
        cv2.imwrite("C:/Users/Aldo Pizarro/Desktop/Idat_Clases/CicloV/ProcesamientoImg/cap1.jpg", frame) #Toma captura
    
cap.release() #Apaga la camara
cv2.destroyAllWindows() #Destruye las ventanas