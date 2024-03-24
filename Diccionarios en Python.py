# Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "Juan Vasquez",
    "edad": 78,
    "ciudad": "Joya de los Sachas",
    "profesion": "Agricultor"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Joya de los Sachas"

# Agregar una nueva clave-valor al diccionario
informacion_personal["profesion"] = "Agricultor"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0986671089"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
