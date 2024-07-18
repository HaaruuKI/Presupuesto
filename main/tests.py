# Ejemplo de una lista de tuplas
lista_tuplas = [("Juan", 30), ("María", 25), ("Pedro", 40)]

# Diccionario para almacenar datos
datos = {}

# Recorremos la lista y guardamos en el diccionario
for i, tupla in enumerate(lista_tuplas):
  nombre = tupla[0]
  edad = tupla[1]
  datos[f"nombre_{i+1}"] = nombre
  datos[f"edad_{i+1}"] = edad

# Impresión de los datos del diccionario
for key, value in datos.items():
  print(f"{key}: {value}")

print(datos)