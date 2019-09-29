###################Condiciones (if, elif, else)
a = 8;b = 4;c = 2;d = 6
a > b
a < b

if (a>b):
    print("a es mayor que b")

if (a<b):
    print("a es mayor que b")

#usando operadores logicos en condicional
if (a>c) and (b<d):
    print("la primera expresion es correcta")

#usando else
if (a>c) and (b>d):
    print("la primera expresion es correcta")
else:
    print("la primera expresion no es correcta")

#condicion elif
a=8;b=10
if (a>b):
    print("a es mayor que b")
elif (a==b):
    print("a es igual a b")
else:
    print("Ninguna expresion anterior es correcta")

###################for
#bucle para recorrer lista
colores = ["rojo","verde","azul"]
for color in colores:
    print(color)

#bucle para recorrer caracteres de una cadena
cadena = "Hola mundo"
for caracter in cadena:
    print (caracter)

range(8) #Lista de numeros de 0 a 7
#bucle para recorrer lista de numeros
for numero in range(8):
    print(numero)

#bucle para recorrer lista de numeros, con un valor de inicio
for numero in range(3,8):
    print(numero)

#bucle para recorrer lista de numeros, con un valor de inicio y con saltos de 2
for numero in range(3,8,2):
    print(numero)

#break
for numero in range(10):
    if numero == 5:
        break
    print(numero)

#continue
for numero in range(10):
    if numero == 6:
        continue
    print(numero)

#for doble
for numero1 in range(4):
    for numero2 in range(3):
        print(numero1,numero2)

###################while
valor = 1
fin = 10
while (valor < fin):
    print(valor)
    valor = valor + 1

#break
valor = 1
fin = 10
while (valor < fin):
    print(valor)
    valor = valor + 1
    if (valor == 5):
        break

#continue
valor = 1
fin = 10
while (valor < fin):
    valor = valor + 1
    if (valor == 6):
        continue
    print(valor)

