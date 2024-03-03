def eliminar_duplicados(lista):
  conjunto = set(lista)
  lista_sin_duplicados = list(conjunto)
  return lista_sin_duplicados
lista = [1, 1, 2, 3, 4, 4, 5, 1]
lista_sin_duplicados = eliminar_duplicados(lista)
print(f"Lista original: {lista}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")
