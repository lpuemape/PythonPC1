cant_shows = int(input("¿Cuantos shows musicales viste en el ultimo año?: "))
while not isinstance(cant_shows, int):
    try:
        cant_shows = int(input("¿Cuantos shows musicales viste en el ultimo año?: "))
    except ValueError:
        print("Por favor, ingresa un numero entero.")
vio_mas_de_3 = cant_shows > 3
print(f"¿Viste mas de 3 shows? {vio_mas_de_3}")