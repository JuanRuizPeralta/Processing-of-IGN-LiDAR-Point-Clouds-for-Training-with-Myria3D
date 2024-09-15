Este código adjuntado supone una adecuación aplicable a nubes de puntos descargadas desde el 
Instituto Geográfico Nacional para su funcionalidad en la red neuronal Myria3D.

Se explica el funcionamiento completo en el documento "Memoria_Ruiz_Peralta_Juan.pdf"

Para ello, los 4 scripts destacados a continuación satisfacen el manejo de los datos previo a 
su uso en Myria3D:

  1.Laz_to_Las.py 
  2.Version_las_14.py 
  3.Combine_las_files.py 
  4.List_files_in_directory.py 

Por otro lado, se han elaborado 2 scripts para la evaluación de los resultados de las 
predicciones inferidas en las nubes de puntos. 

  5.Treatment_Inference.py 
  6.Statistics.py



Los datos del Instituto Geográfico Nacional han sido descargados desde el Centro de descargas del CNIG:
  https://centrodedescargas.cnig.es/CentroDescargas/index.jsp

Por otro lado, la red neuronal mencionada, Myria3D, ha sido desarrollada por el Institut national 
de l’information géographique et forestière, facilitando el código completo en el siguiente repositorio:
  https://github.com/IGNF/myria3d

A su vez, este organismo facilita documentación online sobre su funcionamiento:
  https://ignf.github.io/myria3d/index.html#
