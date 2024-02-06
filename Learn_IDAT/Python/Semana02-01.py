v = eval(input("Ingrese voltaje: "))
r1 = eval(input("Ingrese R1: "))
r2 = eval(input("Ingrese R2: "))
r3 = eval(input("Ingrese R3: "))

rt = r1+r2+r3
i = v/rt

v1 = i*r1
v2 = i*r2
v3 = i*r3

print("El voltaje en R1 es: ",v1)
print("El voltaje en R2 es: ",v2)
print("El voltaje en R3 es: ",v3)
