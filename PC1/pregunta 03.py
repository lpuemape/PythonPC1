peso_del_payaso = 112
peso_de_la_muñeca = 75
cant_payasos = int(input("¿Cuantos payasos se han vendido?: "))
cant_muñecas = int(input("¿Cuantas muñecas se han vendido?: "))
peso_total = (cant_payasos * peso_del_payaso) + (cant_muñecas * peso_de_la_muñeca)
print(f"El peso total del paquete es: {peso_total} gr")