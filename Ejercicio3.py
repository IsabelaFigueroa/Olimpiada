#Ejercicio 3. Estructura de datos y condicionales.
estudiantes= ["Ana","Luis","Carlos"]
edades= [18, 20, 22]
if "Carlos" in estudiantes:
    estudiantes.append("Valentina")
if 20 in edades:
    edades[edades.index(20)]=25
if "Laura" not in estudiantes:
    estudiantes.append("Laura")
if "Luis" in estudiantes:
    estudiantes.remove("Luis")
if len (estudiantes) > 3:
    estudiantes.pop(0)