class Coche:
    def __init__(self,marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
    
    def mostrar_caracteristicas(self):
        print("Este coche es de la marca {} de color {} de {} y una cilindrada de {}".format(self.marca,self.color,self.combustible,self.cilindrada))

media = lambda nota1,nota2,nota3: (nota1 + nota2 + nota3)/3