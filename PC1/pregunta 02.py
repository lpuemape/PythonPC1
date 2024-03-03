c_comida = float(input("¿Cuanto fue el costo total de su comida?: "))
p_propina = float(input("¿Que porcentaje de propina desea dejar?: "))
propina = c_comida * (p_propina / 100)
print(f"La cantidad de dinero a dejar como propina es de: {propina: .2f}")