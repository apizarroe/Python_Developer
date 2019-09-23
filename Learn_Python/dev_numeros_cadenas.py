###################Numeros
numero1 = 5
numero1
type(numero1)

numerodecimal = 3.7
numerodecimal
type(numerodecimal)

numero1 = 5
numero2 = 2.3
suma = numero1 + numero2
suma
type(suma)

###################Cadenas
cadena = "Hola mundo"
cadena
# H o l a   m u n d o
# 0 1 2 3 4 5 6 7 8 9
cadena[5] #substring
cadena[-1]
cadena[2:7] #substring
cadena[2:]
#No se puede asignar valores
# cadena[5] = 'p' - Mostrará error.

cadena1 = 'Hola'
cadena2 = 'mundo'
cadena3 = ' '
cadena = cadena1 + cadena3 + cadena2
cadena

###################Funciones cadena
cadena = "Hola mundo"
len(cadena) #longitud de cadena
print(cadena.upper()) #se muestra en mayuscula, pero no se cambia la variable
print(cadena) #aun esta en minuscula
cadena = cadena.upper() #aca recién se modifica la variable
print(cadena) #aca ya se encuentra en mayuscula, pero no se cambia la variable
print(cadena.lower()        ) #se muestra en minuscula
cadena.split() #se muestran las palabras de la cadena
cadena2 = "uva,pera,manzana,naranja"
cadena2.split(',') #se secciona la cadena por un separador especifico para el ejemplo ","

###################Imprimir variables en una cadena
nombre = "Antonio"
print("Buenos dias " + nombre)
#.format
nombre = "Antonio" #Primer argumento.
edad = 18 #Segundo argumento.
ciudad = "Lima"
print("Buenos dias {}, feliz {} cumpleaños.".format(nombre,edad)) #Formato de asignación de variables.

resultado = 10/3
resultado
print("El resultado es {r}".format(r=resultado))
print("El resultado es {r:1.3f}".format(r=resultado))

#f-string
nombre = "Antonio"
edad = 18
print(f"Buenos días {nombre}, feliz {edad} cumpleaños")
