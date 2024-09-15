import laspy
import numpy as np

#Directorios de entrada y salida
Ruta_Input = "D:/2.Myria3d/prueba_IGN/3.output/PNOA_2016_MAD_416-4508_ORT-CLA-RGB-with-NIR-las14.las"
Ruta_Output = "D:/2.Myria3d/prueba_IGN/3.output/PNOA_2016_MAD_416-4508_ORT-CLA-RGB-with-NIR-las14_Inferencia.las"

#Lectura de nube con laspy
las = laspy.read(Ruta_Input)

#Modificacion de la nube eliminando los puntos de solape
clases = las.classification
mask = clases != 12
clases_filtradas = clases[mask]
points = las.points[mask]

#Conversión a array de NumPy
clases_filtradas = np.array(clases_filtradas)

#Union de las clases de vegetacion en una única, la 5
clases_filtradas[np.isin(clases_filtradas, [3, 4])] = 5

#Union de todos los puntos que no sean terreno (2), vegetación (5) o edificios (6) en la clase sin clasificar (1)
clases_invariantes = [2, 5, 6]
clases_filtradas[~np.isin(clases_filtradas, clases_invariantes)] = 1


#Asignación de la nueva clasificación 
points['classification'] = clases_filtradas

#Creación de una nueva nube
header = las.header
output = laspy.create(point_format=las.point_format, file_version=las.header.version)
output.points = points
output.header = header

#Guardado de la nube
output.write(Ruta_Output)
print(f"Nube de puntos procesada en {Ruta_Output}")