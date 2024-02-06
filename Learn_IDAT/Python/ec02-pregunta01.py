fec_nac = input("Ingresar fecha de nacimiento (AAAA-MM-DD): ")
anio = int(fec_nac[0:4])
mes = int(fec_nac[5:7])
dia = int(fec_nac[8:10])
mensaje = ""
signo = ""
 
if (anio > 2023):
    mensaje = "ERROR: La fecha es mayor al dia de hoy"
if (anio == 2023):
    if (mes > 11):
        mensaje = "ERROR: La fecha es mayor al dia de hoy"
if (anio == 2023 and mes== 11):
    if(dia > 2):
        mensaje = "ERROR: La fecha es mayor al dia de hoy"
if (mes > 12):
    mensaje = "ERROR: La fecha es invalida"
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    if(dia > 31):
        mensaje = "ERROR: La fecha es invalida"
if (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if(dia > 30):
        mensaje = "ERROR: La fecha es invalida"
if (anio % 4 == 0):
    if(mes == 2):
        if(dia > 29):
            mensaje = "ERROR: La fecha es invalida"
else:
    if(mes == 2):
        if(dia > 28):
            mensaje = "ERROR: La fecha es invalida"
if(mensaje == ""):
    mensaje = "La fecha ingresada es valida"
 
if (mes == 1):
    if(dia<=19):
        signo = "Tu signo zodiacal es Capricornio"
    else:
        signo = "Tu signo zodiacal es Acuario"
if (mes == 2):
    if(dia<=18):
        signo = "Tu signo zodiacal es Acuario"
    else:
        signo = "Tu signo zodiacal es Piscis"
if (mes == 3):
    if(dia<=20):
        signo = "Tu signo zodiacal es Piscis"
    else:
        signo = "Tu signo zodiacal es Aries"
if (mes == 4):
    if(dia<=19):
        signo = "Tu signo zodiacal es Aries"
    else:
        signo = "Tu signo zodiacal es Tauro"
if (mes == 5):
    if(dia<=20):
        signo = "Tu signo zodiacal es Tauro"
    else:
        signo = "Tu signo zodiacal es Géminis"
if (mes == 6):
    if(dia<=20):
        signo = "Tu signo zodiacal es Géminis"
    else:
        signo = "Tu signo zodiacal es Cáncer"
if (mes == 7):
    if(dia<=22):
        signo = "Tu signo zodiacal es Cáncer"
    else:
        signo = "Tu signo zodiacal es Leo"
if (mes == 8):
    if(dia<=22):
        signo = "Tu signo zodiacal es Leo"
    else:
        signo = "Tu signo zodiacal es Virgo"
if (mes == 9):
    if(dia<=22):
        signo = "Tu signo zodiacal es Virgo"
    else:
        signo = "Tu signo zodiacal es Libra"
if (mes == 10):
    if(dia<=22):
        signo = "Tu signo zodiacal es Libra"
    else:
        signo = "Tu signo zodiacal es Escorpio"
if (mes == 11):
    if(dia<=21):
        signo = "Tu signo zodiacal es Escorpio"
    else:
        signo = "Tu signo zodiacal es Sagitario"
if (mes == 12):
    if(dia<=21):
        signo = "Tu signo zodiacal es Sagitario"
    else:
        signo = "Tu signo zodiacal es Capricornio"
 
if(anio % 12 == 0):
    signochino = "Tu signo Chino es Mono"
if(anio % 12 == 1):
    signochino = "Tu signo Chino es Gallo"
if(anio % 12 == 2):
    signochino = "Tu signo Chino es Perro"
if(anio % 12 == 3):
    signochino = "Tu signo Chino es Cerdo"
if(anio % 12 == 4):
    signochino = "Tu signo Chino es Rata"
if(anio % 12 == 5):
    signochino = "Tu signo Chino es Buey"
if(anio % 12 == 6):
    signochino = "Tu signo Chino es Tigre"
if(anio % 12 == 7):
    signochino = "Tu signo Chino es Conejo"
if(anio % 12 == 8):
    signochino = "Tu signo Chino es Dragón"
if(anio % 12 == 9):
    signochino = "Tu signo Chino es Serpiente"
if(anio % 12 == 10):
    signochino = "Tu signo Chino es Caballo"
if(anio % 12 == 11):
    signochino = "Tu signo Chino es Cabra"

if(mensaje == "La fecha ingresada es valida"):
    print(mensaje)
    print(signo)
    print(signochino)
else:
    print(mensaje)
