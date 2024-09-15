import os

def listar_archivos(directorio):
    try:
        #Se crea una Lista con los archivos en la ruta especificada
        contenido = os.listdir(directorio)
        print(f"Archivos en el directorio '{directorio}':")
        for item in contenido:
            print(item)
    except Exception as e:
        print(f"Error al listar los archivos: {e}")

#Directorio que almacena las nubes de puntos tratadas
directorio = 'D:\\2.Myria3d\\prueba_IGN\\2.transformation\\3.Union_RGB_NIR'
listar_archivos(directorio)
