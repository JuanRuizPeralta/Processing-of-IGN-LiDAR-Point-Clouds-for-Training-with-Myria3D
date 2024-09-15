import os
import laspy
import numpy as np

#Directorios de entrada y salida
Ruta_Input = "D:/2.Myria3d/prueba_IGN/2.transformation/2.Version_las/"
Ruta_Output = "D:/2.Myria3d/prueba_IGN/2.transformation/3.Union_RGB_NIR/"

#Comprueba que exista la ruta de salida, sino la crea
if not os.path.exists(Ruta_Output):
    os.makedirs(Ruta_Output)

#Listado de todas las nubes input
files = os.listdir(Ruta_Input)

#Se filtran las nubes RGB e IRC según nombre
Nubes_RGB = [f for f in files if "RGB" in f]
Nubes_IRC = [f for f in files if "IRC" in f]

#Se crea un diccionario para emparejar nubes RGB e IRC
Nubes_emparejadas = {}
for RGB_file in Nubes_RGB:
    nombre = RGB_file.replace("RGB-las14.las", "")
    IRC_correspondiente = next((irc for irc in Nubes_IRC if nombre in irc), None)
    if IRC_correspondiente:
        Nubes_emparejadas[RGB_file] = IRC_correspondiente

#Se procesa cada par de nubes emparejadas
for RGB_file, IRC_file in Nubes_emparejadas.items():
    RGB_path = os.path.join(Ruta_Input, RGB_file)
    IRC_path = os.path.join(Ruta_Input, IRC_file)
    output_file = os.path.join(Ruta_Output, RGB_file.replace("RGB", "RGB-with-NIR"))

    #Lectura de nube RGB con laspy
    las_rgb = laspy.read(RGB_path)

    #Lectura de nube IRC con laspy
    las_irc = laspy.read(IRC_path)

    #Se comprueba que ambas nubes tengan el mismo número de puntos
    assert len(las_rgb.points) == len(las_irc.points), f"El número de puntos en {RGB_file} y {IRC_file} no coincide."

    #Se añade la dimensión "Infrarred" en la nube RGB
    las_rgb.add_extra_dim(laspy.ExtraBytesParams(name="Infrared", type=np.uint16, description="nir"))

    #Se copia la dimensión "ROJO" de la nube IRC a la RGB, ya que es la que almacena la inforamción de infrarrojo
    las_rgb['Infrared'] = las_irc['red']

    #Escritura de la nube resultante
    with laspy.open(output_file, mode='w', header=las_rgb.header) as writer:
        writer.write_points(las_rgb.points)

    print(f"Output guardado en: {output_file}")
