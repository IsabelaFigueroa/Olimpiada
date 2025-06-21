print("Verificador de palindromos simples")
palabra = input("Escribe una palabra de tres letras: ").lower()

if len(palabra) != 3:
    print("La palabra no tiene tres letras.")
elif palabra == palabra[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
