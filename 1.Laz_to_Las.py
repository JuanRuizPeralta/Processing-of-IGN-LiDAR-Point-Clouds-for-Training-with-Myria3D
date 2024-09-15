import laspy
import os
import shutil 



#Para la correcta ejecución del programa se debe introducir la dirección donde se va a trabajar
#En este directorio se debe introducir la nube de puntos a tratar
Ruta_Input = 'D:\\2.Myria3d\\prueba_IGN\\1.input'

#En este directorio se obtendrán las nube de puntos en formato .las
Ruta_Output = 'D:\\2.Myria3d\\prueba_IGN\\2.transformation\\1.Descompresion'


###############################################################################################
#Pensado para listar en jupyter y verificar formatos
###############################################################################################

#Listado de los archivos que hay en la carpeta de trabajo
Datos_Partida = os.listdir(Ruta_Input)
print("Archivos en la carpeta:")
print(Datos_Partida)

#Obtener las extensiones de los archivos (solo debería estar la nube en formato .las o .laz)
Nombres = [os.path.splitext(archivo)[0] for archivo in Datos_Partida]

#Verificar los nombres de los archivos
print("\nNombre de los archivos en la carpeta:")
print(Nombres)

#Obtener las extensiones de los archivos (solo debería estar la nube en formato .las o .laz)
Extensiones = [os.path.splitext(archivo)[1] for archivo in Datos_Partida]

#Verificar la extensión del archivo
print("\nExtensiones de los archivos en la carpeta:")
print(Extensiones)

###############################################################################################



for archivo in Datos_Partida:
    nombre_archivo, extension = os.path.splitext(archivo)

    if extension == '.laz':
        #Ruta de descompresión de la nube de puntos a formato las
        Ruta_Nube_las = os.path.join(Ruta_Output,nombre_archivo) + '.las'

        #Lectura del archivo
        Nube_bruta = laspy.read(os.path.join(Ruta_Input,nombre_archivo)+extension)

        #Descompresión
        Nube_las = laspy.convert(Nube_bruta)
        Nube_las.write(Ruta_Nube_las)
        print('Nube de puntos ',archivo,' descomprimida correctamente')
    elif extension == '.las':
        #Se va a duplicar la nube de puntos al directorio de Descomprimir, para continuar con la ejecución del programa
        Ruta_Nube_las = shutil.copy(archivo, Ruta_Output)
        print('Nube de puntos ',archivo,' copiada correctamente')
    else:
        print('El formato de la Nube de Puntos ',archivo,' introducida no es correcto, porfavor introducela en formato .las o .laz')

