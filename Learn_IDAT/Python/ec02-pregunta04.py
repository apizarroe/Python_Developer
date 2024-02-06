a = eval(input("Ingrese el primer número: "))
b = eval(input("Ingrese el segundo número: "))
c = eval(input("Ingrese el tercer número: "))
d = eval(input("Ingrese el cuarto número: "))
 
# Encontramos el número más grande
if b > a:
    a, b = b, a
if c > a:
    a, c = c, a
if d > a:
    a, d = d, a
# Encontramos el segundo número más grande
if c > b:
    b, c = c, b
if d > b:
    b, d = d, b
# Encontramos el número más pequeño
if d > c:
    c, d = d, c
 
print("Números ordenados de mayor a menor:")
print(a)
print(b)
print(c)
print(d)
