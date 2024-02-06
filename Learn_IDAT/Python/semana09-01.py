import serial,time

puerto = serial.Serial('COM3',9600) #Configuramos puerto y velocidad
time.sleep(2)
puerto.write(b"a") #enviamos la letra 'a'
puerto.close() #Cerramos puerto


