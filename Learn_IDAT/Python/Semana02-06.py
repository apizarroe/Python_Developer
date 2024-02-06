cantidad = eval(input("Ingrese la cantidad de productos adquiridos: "))
prc_unit = 0

if (cantidad>1 and cantidad<=25):
    prc_unit = 27.7
    subtotal = cantidad * prc_unit
if (cantidad>26 and cantidad<=50):
    prc_unit = 25.5
    subtotal = cantidad * prc_unit
if (cantidad>51 and cantidad<=75):
    prc_unit = 23.5
    subtotal = cantidad * prc_unit
if (cantidad>76):
    prc_unit = 21.5
    subtotal = cantidad * prc_unit
    
if(cantidad > 50):
    descuento = subtotal * (0.15)
else:
    descuentp = subtotal * (0.05)

total = subtotal - descuento

print("El importe de la compra es", subtotal)
print("El descuento de la compra es", descuento)
print("El monto a pagar de la compra es", total)
