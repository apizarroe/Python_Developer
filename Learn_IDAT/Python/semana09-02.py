import serial,time

puerto = serial.Serial('COM3',9600) #Configuramos puerto y velocidad
time.sleep(2)
while True:
    valor = input("Ingresa un caracter: ")
    if(valor == 'a' or valor == 'b'):
        puerto.write(str.encode(valor)) #enviamos la letra ingresada por tecla
    if(valor == 'c'):
        puerto.close() #Cerramos puerto
        break
print("Fin del programa")