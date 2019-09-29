#Trabajando con modulos, se importa solo la función despedirse del modulo1
#from dev_09_modulo1 import despedirse

#Trabajando con modulos, la funcion despedirse con un alias "adios"
from dev_09_modulo1 import despedirse as adios

minombre = "Antonio"
#despedirse(minombre)
adios(minombre)
