import cv2

img = cv2.imread('C:/Users/Aldo Pizarro/Desktop/Idat_Clases/CicloV/ProcesamientoImg/frutas.jpg')
#Forma Basica
#img1 = cv2.line(img,(580,155),(780,155),(255,0,0),3) #dibujar linea1
#img1 = cv2.line(img,(780,155),(780,360),(255,0,0),3) #dibujar linea2
#img1 = cv2.line(img,(780,360),(580,360),(255,0,0),3) #dibujar linea3
#img1 = cv2.line(img,(580,360),(580,155),(255,0,0),3) #dibujar linea4
#Con rectangulo
img = cv2.rectangle(img,(580,155),(780,360),(0,0,255),3)
font = cv2.FONT_HERSHEY_COMPLEX #tipo de letra
cv2.putText(img,"Naranja",(580,120),font,1,(255,0,0),1,cv2.LINE_AA) #dibujar texto
cv2.imshow('linea',img)
#texto(imagen, texto, posicion, tipo de letra, tamaño, color, grosor, modelo)
cv2.waitKey()
