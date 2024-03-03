n = int(input("Ingresa un numero entero positivo: "))
while n<0:
    n = int(input("Ingrese un numero entero positivo: "))
suma = (n * (n+1))/2
print(f"La suma de los primeros {n} numero positivos es: {suma}")