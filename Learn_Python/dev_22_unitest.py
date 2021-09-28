###################Doctest - Sirve para generar pruebas dentro del propio codigo
def multiplicar(numero1,numero2):
    return numero1 * numero2

resultado = multiplicar(2,4)
print(resultado)

import unittest #Se importa el metodo unittest

class pruebas(unittest.TestCase):

    def test(self):
        self.assertEqual(multiplicar(2,4),8)
        # Test que genera error en la ejecucion
        # self.assertEqual(multiplicar(2,4),9)

if __name__ == '__main__':
    unittest.main()