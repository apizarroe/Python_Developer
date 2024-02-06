#Autor: Aldo Pizarro
#Codigo: a17202187@idat.edu.pe
#Carrera: Meacatronica Industrial

horas_trabajadas = eval(input("Ingrese la cantidad de horas trabajadas por el obrero: "))
dia_trabajado = input("Ingrese el dia trabajado por el obrero: ")
total_pago = 0
horas_extras = 0
precio_horan = 10

if(horas_trabajadas >= 0 and (dia_trabajado == 'L' or dia_trabajado == 'M' or 
                              dia_trabajado == 'W' or dia_trabajado == 'J' or 
                              dia_trabajado == 'V' or dia_trabajado == 'S')):
    if (horas_trabajadas<=8):
        total_horasn = horas_trabajadas * precio_horan
        total_horase = 0
    if (horas_trabajadas>8):
        total_horasn = 8 * precio_horan
        horas_extras = horas_trabajadas - 8
        if (dia_trabajado == 'L' or dia_trabajado == 'W' or dia_trabajado == 'V'):
            total_horase = 15 * horas_extras
        if (dia_trabajado == 'M' or dia_trabajado == 'J' or dia_trabajado == 'S'):
            total_horase = 20 * horas_extras
    total_pago = total_horasn + total_horase
    print("El pago total al obrero es ", total_pago)

if(horas_trabajadas < 0):
    print("ERROR: Las horas ingresadas son incorrectas")

if(dia_trabajado != 'L' and dia_trabajado != 'W' and dia_trabajado != 'V' and
   dia_trabajado != 'M' and dia_trabajado != 'J' and dia_trabajado != 'S'):
    print("ERROR: El dia ingresado es incorrecto")

