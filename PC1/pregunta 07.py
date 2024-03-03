numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
print("Elige una opción:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
opcion = int(input("Introduce tu opción: "))
if opcion == 1:
    resultado = numero1 + numero2
    print(f"La suma de los números es: {resultado}")
elif opcion == 2:
    resultado = numero1 - numero2
    print(f"La resta de los números es: {resultado}")
elif opcion == 3:
    resultado = numero1 * numero2
    print(f"El producto de los números es: {resultado}")
else:
    print("Opción no válida.")