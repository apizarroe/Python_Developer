###################JSON
#Convertir datos de un diccionario Python a una esrtuctura JSON
producto1 = {"nombre":"silla", "color":"blanco", "precio":80}
import json
estructura_json = json.dumps(producto1)
print(estructura_json)
#Muestra error puesto que no es un diccionario, si no un json
#estructura_json["nombre"]
#Es una cadena de texto y se puede acceder a las posiciones
print(estructura_json[0])
print(producto1["nombre"])
type(estructura_json)

#Convertir una estructura JSON en un diccionario en Python
producto2 = json.loads(estructura_json)
print(producto2["precio"])
type(producto2)
