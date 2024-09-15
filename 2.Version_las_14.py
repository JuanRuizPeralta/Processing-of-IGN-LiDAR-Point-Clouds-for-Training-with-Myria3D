import os
import laspy
import glob
from laspy.header import Version

#Directorio con las nubes de puntos descomprimidas
Ruta_Input = 'D:\\2.Myria3d\\prueba_IGN\\2.transformation\\1.Descompresion'
#Directorio con las nubes de puntos resultantes
Ruta_Output = 'D:\\2.Myria3d\\prueba_IGN\\2.transformation\\2.Version_las'

#Comprueba que exista la ruta de salida, sino la crea
if not os.path.exists(Ruta_Output):
    os.makedirs(Ruta_Output)

#Busca todas las nubes .las en la carpeta de entrada
input_nubes = glob.glob(os.path.join(Ruta_Input, '*.las'))

for nube in input_nubes:
    #Lee la nube original
    with laspy.open(nube) as las:
        header = las.header

        #Crea una nueva nube con la versión LAS 1.4 editando su nombre
        nombre = os.path.basename(nube)
        output = os.path.join(Ruta_Output, nombre.replace('.las', '-las14.las'))
        header.version = Version(1, 4) 
        #Reescribe metadatos que de no transferir, se perderían
        with laspy.open(output, mode='w', header=header) as writer:
            writer.header.system_identifier = header.system_identifier
            writer.header.generating_software = header.generating_software
            writer.header.date = header.date
            writer.header.offsets = header.offsets
            writer.header.scales = header.scales
            writer.header.min = header.min
            writer.header.max = header.max

            #Copia todos los puntos de la nube original
            for points in las.chunk_iterator(1_000_000):
                writer.write_points(points)
    print(nombre,"convertido correctamente a versión 1.4.")
