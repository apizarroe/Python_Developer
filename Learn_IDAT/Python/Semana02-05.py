try:
    temp = eval(input("Ingrese el valor de la temperatura: "))

    if (temp<=0):
        print("La temperatura esta por debajo de los limites soportados!")
    elif (temp>0 and temp<=30):
        print("La temperatura es baja")
    elif (temp>30 and temp<=75):
        print("La temperatura es media")
    elif (temp>75 and temp<=100):
        print("La temperatura es alta")
    elif (temp>100):
        print("La temperatura esta por arriba de los limites soportados!")

except NameError:
    print("El valor ingresado no es numerico!!")