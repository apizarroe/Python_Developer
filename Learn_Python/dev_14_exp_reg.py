###################Expresiones regulares (search, findall, split, sub)
#search
texto = "Hola, mi nombre es Antonio"

import re
#En caso de encontrar la cadena, devuelve: <re.Match object; span=(9, 15), match='nombre'>
re.search("nombre",texto)
#En caso de no encontrar la cadena, no devulve nada
re.search("adios",texto)

#Una pequeña forma de usar el metodo search
resultado = re.search("nombre",texto)
if(resultado):
    print("Cadena encontrada")
else:
    print("Cadena no encontrada")

#Busca si hay una linea que termine en Antonio
re.search("Antonio$",texto)
#Busca si hay una linea que inicie en Hola
re.search("^Hola",texto)
#Busca una cadena que inicie en mi y termine en es, sim importar los caracteres dentro
re.search("mi.*es",texto)

#findall
texto = """
El coche de Luis es rojo,
el coche de Antonio es blanco,
y el coche de Maria es rojo
"""
re.findall("coche.*rojo",texto)
re.search("coche.*rojo",texto)

#split
texto = "La silla es blanca y vale 80"
re.split("\s",texto)

#sub
texto =  "La silla es blanca y vale 80"
re.sub("blanca","roja",texto)
