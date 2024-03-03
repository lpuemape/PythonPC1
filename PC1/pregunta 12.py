def obtener_tipo_mime(nombre_archivo):
  extensiones = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip",
  }
  nombre_archivo = nombre_archivo.lower()
  extension = nombre_archivo.split(".")[-1]
  if extension in extensiones:
    return extensiones[extension]
  else:
    return "application/octet-stream"
nombre_archivo = input("Introduce el nombre del archivo: ")
tipo_mime = obtener_tipo_mime(nombre_archivo)
print(f"El tipo MIME del archivo es: {tipo_mime}")
