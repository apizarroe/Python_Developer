###################Operadores lógicos (and, or, not)
numero1 = 10
numero2 = 5
numero3 = 7
numero4 = 8
numero1 > numero2;numero3 < numero4;numero1 < numero2;numero3 > numero4
(numero1 > numero2) and (numero3 < numero4)
(numero1 > numero2) and (numero3 > numero4)
(numero1 > numero2) or (numero3 < numero4)
(numero1 < numero2) or (numero3 > numero4)
not(numero1 > numero2)

###################Operadores de identidad (is, is not)
frutas1 = ["manzana","pera"]
frutas2 = ["manzana","pera"]
frutas3 = frutas1

frutas3 is frutas1
frutas3.append("naranja")
frutas3
frutas1
frutas3 is not frutas2

###################Operadores de pertenencia (in, not in)
frutas1 = ["manzana","pera","naranja"]
frutas2 = "pera"
frutas2 in frutas1
frutas2 not in frutas1
frutas3 = "melocoton"
frutas3 not in frutas1
