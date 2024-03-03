def eliminar_elementos(lista, posiciones):
  nueva_lista = []
  for i, elemento in enumerate(lista):
    if i not in posiciones:
      nueva_lista.append(elemento)
  return nueva_lista
lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
posiciones = [0, 4, 5]
lista_filtrada = eliminar_elementos(lista, posiciones)
print(f"Lista original: {lista}")
print(f"Posiciones eliminadas: {posiciones}")
print(f"Lista filtrada: {lista_filtrada}")
