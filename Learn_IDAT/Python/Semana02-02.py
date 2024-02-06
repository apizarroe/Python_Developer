monto = eval(input("Ingrese monto: "))

bil_200 = monto // 200
monto = monto - (bil_200*200)
bil_100 = monto // 100
monto = monto - (bil_100*100)
bil_50 = monto // 50
monto = monto - (bil_50*50)
bil_20 = monto // 20
monto = monto - (bil_20*20)
bil_10 = monto // 10
monto = monto - (bil_10*10)

print("La cantidad de billetes de 200 es ",bil_200)
print("La cantidad de billetes de 100 es ",bil_100)
print("La cantidad de billetes de 50 es ",bil_50)
print("La cantidad de billetes de 20 es ",bil_20)
print("La cantidad de billetes de 10 es ",bil_10)


