dia_ingresado = input("Ingrese una fecha (DD-MM): ")
dia = int(dia_ingresado[0:2])
mes = int(dia_ingresado[3:5])

dia_hoy = 2
mes_hoy = 11
dias_termino_mes = 28
dias_inicio_mes = 2
dias_enero = 31
dias_febrero = 28
dias_marzo = 31
dias_abril = 30
dias_mayo = 31
dias_junio = 30
dias_julio = 31
dias_agosto = 31
dias_septiembre = 30
dias_octubre= 31
dias_noviembre = 30
dias_diciembre = 31

mensaje=""

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    if(dia <= 31):
        mensaje = "Fecha valida"
else:
    if (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if(dia <= 30):
            mensaje = "Fecha valida"
    else:
        if (mes == 2):
            if(dia <= 28):
                mensaje = "Fecha valida"
        else:
            mensaje = "ERROR: La fecha es invalida"

print(mensaje)
        
if (mensaje == "Fecha valida"):
    if (mes == 12):
        total_dias = dia + dias_termino_mes
    if (mes == 11):
        if(dia_hoy>dia):
            total_dias = dia_hoy - dia
        if(dia_hoy<dia):
            total_dias = dia - dia_hoy
        if(dia_hoy == dia):
            total_dias = 0
    if (mes == 10):
        total_dias = dias_inicio_mes + (dias_octubre - dia)
    if (mes == 9):
        total_dias = dias_inicio_mes + dias_octubre + (dias_septiembre - dia)
    if (mes == 8):
        total_dias = dias_inicio_mes + dias_octubre + dias_septiembre + (dias_agosto - dia)
    if (mes == 7):
        total_dias = dias_inicio_mes + dias_octubre + dias_septiembre + dias_agosto + (dias_julio - dia)
    if (mes == 6):
        total_dias = dias_inicio_mes + dias_octubre + dias_septiembre + dias_agosto + dias_julio + (dias_junio - dia)
    if (mes == 5):
        total_dias = dias_inicio_mes + dias_octubre + dias_septiembre + dias_agosto + dias_julio + dias_junio + (dias_mayo - dia)
    if (mes == 4):
        total_dias = dias_inicio_mes + dias_octubre + dias_septiembre + dias_agosto + dias_julio + dias_junio + dias_mayo + (dias_abril - dia)
    if (mes == 3):
        total_dias = dias_inicio_mes + dias_octubre + dias_septiembre + dias_agosto + dias_julio + dias_junio + dias_mayo + dias_abril + (dias_marzo - dia)
    if (mes == 2):
        total_dias = dias_inicio_mes + dias_octubre + dias_septiembre + dias_agosto + dias_julio + dias_junio + dias_mayo + dias_abril + dias_marzo + (dias_febrero - dia)
    if (mes == 1):
        total_dias = dias_inicio_mes + dias_octubre + dias_septiembre + dias_agosto + dias_julio + dias_junio + dias_mayo + dias_abril + dias_marzo + dias_febrero + (dias_enero - dia)
        
    
    if(mes > mes_hoy):
        print("Los dias faltantes para el ", dia, " de ", mes, " desde el dia de hoy son: ", total_dias)
    if(mes < mes_hoy):
        print("Los dias transcurridos desde el ", dia, " de ", mes, " al dia de hoy son: ", total_dias)
    if(mes == mes_hoy):
        if(dia > dia_hoy):
            print("Los dias faltantes para el ", dia, " de ", mes, " desde el dia de hoy son: ", total_dias)
        if(dia < dia_hoy):
            print("Los dias transcurridos desde el ", dia, " de ", mes, " al dia de hoy son: ", total_dias)



