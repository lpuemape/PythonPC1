def invertir_lista(lista):
  lista_invertida = lista[::-1]
  return lista_invertida
lista = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = invertir_lista(lista)
print(f"Lista original: {lista}")
print(f"Lista invertida: {lista_invertida}")
