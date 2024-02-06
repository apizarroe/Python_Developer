x = eval(input("Ingresar horas: "))
y = eval(input("Ingresar minutos: "))
z = eval(input("Ingresar segundos: "))
a = eval(input("Ingresar horas salida: "))
b = eval(input("Ingresar minutos salida: "))
c = eval(input("Ingresar segundos salida: "))

segundos_ingreso = x*3600+y*60+z
segundos_salida = a*3600+b*60+c

segundos_totales = segundos_salida - segundos_ingreso
minutos_totales = segundos_totales/60

print("HORA DE INGRESO: ",x,": ",y,": ",z)
print("HORA DE SALIDA: ",a,": ",b,": ",c)
print ("total de minutos: ",minutos_totales)
if 0<=minutos_totales<=60:
    p = minutos_totales*0.54
if 60<minutos_totales<=200:
    p = minutos_totales*0.50
if 200<minutos_totales<=400:
    p = minutos_totales*0.48
if 400<minutos_totales:
    p = minutos_totales*0.45
if 220<minutos_totales:
    d = 0.13*p
else:
    d = 0.07*p
n = p-d
print("Importe de compra: ",p)
print("Importe de descuento: ",d)
print("Importe a pagar: ",n)

f = open("venta.txt","w")
f.write("Importe de compra: " + str(p) + "\n")
f.write("Importe de descuento: " + str(d) + "\n")
f.write("Importe a pagar: " + str(n))
f.close()

