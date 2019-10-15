###################try ...except ...else ...finally
numero1 = 5
numero2 = 0
division = numero1 / numero2

#Esta es la forma de caprturar un error en general
try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except:
    print("Ha habido un error")

#Esta es la forma de capturar un error específico
try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print("Error, división entre cero")
except:
    print("Ha habido un error")

#También se puede usar else para el manejo de errores
try:
    numero1 = 5
    numero2 = 2
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print("Error, división entre cero")
except:
    print("Ha habido un error")
else:
    print("La división funcionó correctamente")

#Este es el modo de manejo de finally
try:
    numero1 = 5
    numero2 = 2
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print("Error, división entre cero")
except:
    print("Ha habido un error")
else:
    print("La división funcionó correctamente")
#Este bloque de codigo siempre se ejecutará caiga en una excepción o no
finally:
    print("La prueba del try se ha acabado!")

