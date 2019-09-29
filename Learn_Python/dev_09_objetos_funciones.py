###################Clases y objetos. POO
#Se crea una clase ClaseSilla, con los atributos color y precio
#Se puede visualizar sus atributos, asi como modificar los mismos
class ClaseSilla:
    color = "blanco"
    precio = 100

objetoSilla1 = ClaseSilla()
objetoSilla1.color
objetoSilla1.precio

objetoSilla2 = ClaseSilla()
objetoSilla2.color = "verde"
objetoSilla2.precio = 120
objetoSilla2.precio

#Se crea una Clase Persona, se utiliza un constructor para definir sus atributos
#ademas se genera un metodo que utiliza sus atributos, en un mensaje de Saludo.
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print("Hola me llamo {} y tengo {} años".format(self.nombre,self.edad))

persona1 = Persona("Juan",37)
persona1.edad
persona1.nombre
persona1.saludar()

###################Funciones
#Funcion simple que nos muestra un saludo
def saludar():
    print("Buenos dias")
saludar()

#Funcion simple que nos muestra un saludo, requiere un parametro
def saludar(nombre):
    print("Buenos dias " +  nombre)
nombre = "Antonio"
saludar(nombre)

#Funcion de suma retornando un valor
def sumar(numero1,numero2):
    suma = numero1 + numero2
    return suma
numero1 = 5;numero2 = 3
resultado = sumar(numero1,numero2)
resultado

#paso de valor por referencia
#En este caso la funcion se utiliza para modificar un arreglo de datos
colores = ["rojo","verde","azul"]

def incluir_color(colores,color):
    colores.append(color)
color = "negro"
incluir_color(colores,color)
colores

###################Funciones Lambda
#Es una funcion pequeña y sin nombre (anonima)
resultado = lambda numero: numero + 30
resultado(10)

resultado2 = lambda numero1, numero2: numero1 + numero2
resultado2(5,8)

