#Se ejecuta (En windows) python dev_21_doctest.py -v

###################Doctest - generar pruebas dentro de la documentacion
def sumar(numero1,numero2):
    """
    Esto es la documentación de esta funcion
    Recibe dos números como parámetros y devuelve su suma

    >>> sumar(4,3) #Esta linea es un test del metodo sumar, nos devolvera el resultado
    7 #Este es el resultado esperado del test, se evaluara contra el resultado obtenido

    >>> sumar(5,4)
    9

    >>> sumar(1,3)
    4
    """
    return numero1 + numero2

resultado = sumar(2,4) #Se realiza la ejecucion del metodo sumar con dos parametros
print(resultado)

import doctest #Se importa el metodo doctest
doctest.testmod()
