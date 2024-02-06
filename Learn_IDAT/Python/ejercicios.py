dia_ingresado = input("Ingrese una fecha (DD-MM): ")
dia = int(dia_ingresado[0:2])
mes = int(dia_ingresado[3:5])

dia_hoy = 27
mes_hoy = 10
dias_termino_mes = 19
dias_inicio_mes = 11
dias_enero = 31
dias_febrero = 28
dias_marzo = 31
dias_abril = 30
dias_mayo = 31
dias_junio = 30
dias_julio = 31
dias_agosto = 31
dias_septiembre = 30
dias_octubre = 31
dias_noviembre = 30
dias_diciembre = 31

if (dia >= 1 and dia <= 31):
    if (mes >= 1 and mes <= 12):
        if (mes == 12):
            total_dias = dia + dias_noviembre + dias_termino_mes
        if (mes == 11):
            total_dias = dia + dias_termino_mes
        if (mes == 10):
            if(dia_hoy>dia):
                total_dias = dia_hoy - dia
            if(dia_hoy<dia):
                total_dias = dia - dia_hoy
            if(dia_hoy == dia):
                total_dias = 0
        if (mes == 9):
            total_dias = dias_inicio_mes + (dias_septiembre - dia)
        if (mes == 8):
            total_dias = dias_inicio_mes + dias_septiembre + (dias_agosto - dia)
        if (mes == 7):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + (dias_julio - dia)
        if (mes == 6):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + dias_julio + (dias_junio - dia)
        if (mes == 5):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + dias_julio + dias_junio + (dias_mayo - dia)
        if (mes == 4):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + dias_julio + dias_junio + dias_mayo + (dias_abril - dia)
        if (mes == 3):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + dias_julio + dias_junio + dias_mayo + dias_abril + (dias_marzo - dia)
        if (mes == 2):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + dias_julio + dias_junio + dias_mayo + dias_abril + dias_marzo + (dias_febrero - dia)
        if (mes == 1):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + dias_julio + dias_junio + dias_mayo + dias_abril + dias_marzo + dias_febrero + (dias_enero - dia)
        
        if(mes > mes_hoy):
            print("Los dias faltantes para el ", dia, " de ", mes, " desde el dia de hoy son: ", total_dias)
        if(mes < mes_hoy):
            print("Los dias transcurridos desde el ", dia, " de ", mes, " al dia de hoy son: ", total_dias)
        if(mes == mes_hoy):
            if(dia > dia_hoy):
                print("Los dias faltantes para el ", dia, " de ", mes, " desde el dia de hoy son: ", total_dias)
            if(dia < dia_hoy):
                print("Los dias transcurridos desde el ", dia, " de ", mes, " al dia de hoy son: ", total_dias)

    if(mes < 1 or mes > 12):
        print("ERROR: El valor del mes es incorrecto")
if(dia < 1 or dia > 31):
    print("ERROR: El valor del dia es incorrecto")