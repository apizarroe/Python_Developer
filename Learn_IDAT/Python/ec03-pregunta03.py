import serial,time

i = 0
valor = ""
puerto = serial.Serial('COM3',9600) #Configuramos puerto y velocidad
#time.sleep(2)
f = open("valores.txt","w")
while(i < 50):
    valor = puerto.readline().decode('utf-8').rstrip()
    f.write("Valor Analogico " + str(i) + ": " + str(valor) + "\n")
    i = i+1
f.close()
puerto.close()
