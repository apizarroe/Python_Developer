print("¡Hola desde mi_modulo.py!")

def hacer_algo():
    print("¡Soy una función y hago algo!")

if __name__ == "__main__":
    print('Ejecutando como programa principal')
    hacer_algo()

print("¡Adiós desde mi_módulo.py!")  # Debajo del condicional pero fuera del mismo

print(__name__)