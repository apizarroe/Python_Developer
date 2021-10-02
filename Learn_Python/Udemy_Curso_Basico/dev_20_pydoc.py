#Se ejecuta el pydoc (En windows) python -m pydoc /ruta/completa/archivopy.py (Por consola)
#Se ejecuta el pydoc (En windows) python -m pydoc -w /ruta/completa/archivopy.py (Archivo html)

class Saludos:
    """
    Esta clase tendrá dos funciones buenos_dias y adios
    Ambas funciones recibirán como parametro un nombre
    """
    def buenos_dias(self,nombre):
        """ Esta función sirve para decir buenos dias a una persona """
        print("Buenos dias {}".format(nombre))
    def adios(self,nombre):
        """ Esta funcion dice adios a una persona """
        print("Adios {}".format(nombre))