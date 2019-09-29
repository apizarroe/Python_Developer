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
#Este operador nos indica si las variables son identicas
#Para el ejemplo frutas 3 y frutas 1 son identicas
frutas3 is frutas1
frutas3.append("naranja")
frutas3
frutas1
#Este operador nos indica si las variables no son identicas
#Para el ejemplo frutas 3 y frutas 2 no son identicas
frutas3 is not frutas2

###################Operadores de pertenencia (in, not in)
frutas1 = ["manzana","pera","naranja"]
frutas2 = "pera"
#Este operador nos indica si la variable frutas1 pertenece a frutas2
frutas2 in frutas1
#Este operador nos indica si la variable frutas1 no pertenece a frutas2
frutas2 not in frutas1
frutas3 = "melocoton"
frutas3 not in frutas1
