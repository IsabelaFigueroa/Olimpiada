# Interacción con el usuario
print("¡Bienvenido/a al sistema de gestión de estudiantes!")
nombre_usuario = input("¿Cuál es tu nombre?: ")
edad_usuario = int(input("¿Cuál es tu edad?: "))

# Estructuras iniciales
estudiantes = ["Ana", "Luis", "Carlos"]
edades = [18, 20, 22]

# 1
if "Carlos" in estudiantes:
    estudiantes.append("Valentina")

# 2
if 20 in edades:
    edades.append(25)

# 3
if "Laura" not in estudiantes:
    estudiantes.append("Laura")

# 4
if "Luis" in estudiantes:
    estudiantes.remove("Luis")

# 5
if len(estudiantes) > 3:
    estudiantes.pop(0)

# 6
if 22 in edades:
    edades.remove(22)
    edades.append(23)

# 7
grupo1 = estudiantes[:2]

# 8
grupo2 = edades[-2:]

# 9
if "Valentina" in grupo1:
    tupla1 = ("Valentina", 23)

# 10
if sum(grupo2) > 40:
    grupo2.append(30)

# 11
if "Laura" in estudiantes:
    registro = {
        "nombre": "Laura",
        "edad": 20,
        "activo": True
    }

# 12
if 'registro' in locals():
    registro["ciudad"] = "Cali"

# 13
if "Ana" in estudiantes:
    coordinadora = ("Ana", 18)

# 14
print("--- RESULTADOS ---")
print(f"Nombre del usuario: {nombre_usuario}")
print(f"Edad del usuario: {edad_usuario}")
print(f"Estudiantes: {estudiantes}")
print(f"Edades: {edades}")
print(f"Grupo 1: {grupo1}")
print(f"Grupo 2: {grupo2}")

if 'tupla1' in locals():
    print(f"Tupla especial: {tupla1}")

if 'registro' in locals():
    print(f"Diccionario registro: {registro}")

if 'coordinadora' in locals():
    print(f"Tupla coordinadora: {coordinadora}")