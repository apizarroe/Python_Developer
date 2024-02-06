#Autor: Aldo Pizarro
#Codigo: a17202187@idat.edu.pe
#Carrera: Meacatronica Industrial

dia_ingresado = eval(input("Ingrese un dia del mes (en numero): "))
mes_ingresado = eval(input("Ingrese un mes del año (en numero): "))
dia_hoy = 12
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

if (dia_ingresado >= 1 and dia_ingresado <= 31):
    if (mes_ingresado >= 1 and mes_ingresado <= 12):
        if (mes_ingresado == 12):
            total_dias = dia_ingresado + dias_noviembre + dias_termino_mes
        if (mes_ingresado == 11):
            total_dias = dia_ingresado + dias_termino_mes
        if (mes_ingresado == 10):
            if(dia_hoy>dia_ingresado):
                total_dias = dia_hoy - dia_ingresado
            if(dia_hoy<dia_ingresado):
                total_dias = dia_ingresado - dia_hoy
            if(dia_hoy == dia_ingresado):
                total_dias = 0
        if (mes_ingresado == 9):
            total_dias = dias_inicio_mes + (dias_septiembre - dia_ingresado)
        if (mes_ingresado == 8):
            total_dias = dias_inicio_mes + dias_septiembre + (dias_agosto - dia_ingresado)
        if (mes_ingresado == 7):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + (dias_julio - dia_ingresado)
        if (mes_ingresado == 6):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + dias_julio + (dias_junio - dia_ingresado)
        if (mes_ingresado == 5):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + dias_julio + dias_junio + (dias_mayo - dia_ingresado)
        if (mes_ingresado == 4):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + dias_julio + dias_junio + dias_mayo + (dias_abril - dia_ingresado)
        if (mes_ingresado == 3):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + dias_julio + dias_junio + dias_mayo + dias_abril + (dias_marzo - dia_ingresado)
        if (mes_ingresado == 2):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + dias_julio + dias_junio + dias_mayo + dias_abril + dias_marzo + (dias_febrero - dia_ingresado)
        if (mes_ingresado == 1):
            total_dias = dias_inicio_mes + dias_septiembre + dias_agosto + dias_julio + dias_junio + dias_mayo + dias_abril + dias_marzo + dias_febrero + (dias_enero - dia_ingresado)
        
        if(mes_ingresado > mes_hoy):
            print("Los dias faltantes para el ", dia_ingresado, " de ", mes_ingresado, " desde el dia de hoy son: ", total_dias)
        if(mes_ingresado < mes_hoy):
            print("Los dias transcurridos desde el ", dia_ingresado, " de ", mes_ingresado, " al dia de hoy son: ", total_dias)
        if(mes_ingresado == mes_hoy):
            if(dia_ingresado > dia_hoy):
                print("Los dias faltantes para el ", dia_ingresado, " de ", mes_ingresado, " desde el dia de hoy son: ", total_dias)
            if(dia_ingresado < dia_hoy):
                print("Los dias transcurridos desde el ", dia_ingresado, " de ", mes_ingresado, " al dia de hoy son: ", total_dias)

    if(mes_ingresado < 1 or mes_ingresado > 12):
        print("ERROR: El valor del mes es incorrecto")
if(dia_ingresado < 1 or dia_ingresado > 31):
    print("ERROR: El valor del dia es incorrecto")
    



