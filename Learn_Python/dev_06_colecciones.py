###################Listas
colores = ["rojo","amarillo","verde"]
colores
colores[0]
colores[1]
colores[1] = "azul"
colores
#muestra la longitud de la lista
len(colores)
#agregamos un objeto a la lista
colores.append("naranja")
colores
#removemos un objeto a la lista
colores.remove("rojo")
colores
#recorremos las lita imprimiendo cada valor
for color in colores:
    print(color)
colores.clear

###################Tuplas (Coleccion de elementos ordenada no alterable)
tupla_colores = ("rojo","verde","amarillo")
tupla_colores
for color in tupla_colores:
    print(color)
tupla_colores[2]
len(tupla_colores)

###################Conjuntos (Coleccion de elementos sin indice)
conjunto_colores = {"rojo","verde","azul"}
conjunto_colores
for color in conjunto_colores:
    print(color)
#conjunto_colores[0] Mostrará error, no tiene indice
conjunto_colores
len(conjunto_colores)
conjunto_colores.add("negro")
print(conjunto_colores)
conjunto_colores.remove("verde")
print(conjunto_colores)

###################Diccionarios (Coleccion de elementos indexados, no ordenados y modificables)
diccionario_colores = {"red":"rojo", "blue":"azul", "yellow":"amarillo"}
diccionario_colores
diccionario_colores["red"]
valor = diccionario_colores["yellow"]
valor
#Agregamos un valor al diccionario
diccionario_colores["black"] = "negro"
diccionario_colores
#Removemos un valor al diccionario, mostrando el valor eliminado
diccionario_colores.pop("yellow")
diccionario_colores
#Removemos un valor al diccionario, sin mostrar el valor eliminado
del(diccionario_colores["black"])
diccionario_colores
print (diccionario_colores)
for color in diccionario_colores:
    print(color)
#recorremos las lita imprimiendo cada par de valores
for clave,valor in diccionario_colores.items():
    print(clave,valor)
