#Autor: Aldo Pizarro
#Codigo: a17202187@idat.edu.pe
#Carrera: Meacatronica Industrial

numero1 = eval(input("Ingrese el primer valor: "))
numero2 = eval(input("Ingrese el segundo valor): "))
numero3 = eval(input("Ingrese el tercer valor): "))

if(numero1 > numero2):
    if(numero1 > numero3):
        print("El valor mas alto es: ",numero1)
        if(numero2 > numero3):
            print("El valor medio es: ",numero2)
            print("El valor mas bajo es: ",numero3)
        if(numero2 <= numero3):
            print("El valor medio es: ",numero3)
            print("El valor mas bajo es: ",numero2)
    if(numero1 <= numero3):
        print("El valor mas alto es: ",numero3)
        print("El valor medio es: ",numero1)
        print("El valor mas bajo es: ",numero2)
if(numero2 > numero1):
    if(numero2 > numero3):
        print("El valor mas alto es: ",numero2)
        if(numero3 > numero1):
            print("El valor medio es: ",numero3)
            print("El valor mas bajo es: ",numero1)
        if(numero3 <= numero1):
            print("El valor medio es: ",numero1)
            print("El valor mas bajo es: ",numero3)
    if(numero2 <= numero3):
        print("El valor mas alto es: ",numero3)
        print("El valor medio es: ",numero2)
        print("El valor mas bajo es: ",numero1)
if(numero2 == numero1):
    if(numero2 > numero3):
        print("El valor mas alto es: ",numero2)
        print("El valor medio es: ",numero1)
        print("El valor mas bajo es: ",numero3)
    if(numero2 <= numero3):
        print("El valor mas alto es: ",numero3)
        print("El valor medio es: ",numero2)
        print("El valor mas bajo es: ",numero1)
