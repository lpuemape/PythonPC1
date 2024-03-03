def es_hora_de_comer(hora):
  hora_en_float = float(hora.replace(":", "."))

  if 7 <= hora_en_float <= 8:
    return "Es hora de desayunar."
  elif 12 <= hora_en_float <= 13:
    return "Es hora de almorzar."
  elif 18 <= hora_en_float <= 19:
    return "Es hora de cenar."
  else:
    return None
hora = input("Introduce la hora actual (formato 24 horas): ")
mensaje = es_hora_de_comer(hora)
if mensaje is not None:
  print(mensaje)


