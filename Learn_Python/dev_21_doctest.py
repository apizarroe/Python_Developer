#Se ejecuta (En windows) python dev_21_doctest.py -v

###################Doctest - generar pruebas dentro de la documentacion
def sumar(numero1,numero2):
    """
    Esto es la documentación de esta funcion
    Recibe dos números como parámetros y devuelve su suma

    >>> sumar(4,3)
    7

    >>> sumar(5,4)
    9

    >>> sumar(1,3)
    7
    """
    return numero1 + numero2

resultado = sumar(2,4)
print(resultado)

import doctest
doctest.testmod()
