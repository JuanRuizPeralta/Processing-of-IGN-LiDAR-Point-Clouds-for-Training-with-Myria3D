import laspy
import pandas as pd

Ruta = "/mnt/d/2.Myria3d/prueba_IGN/3.output/1.Prediction/"
Nombre = "14.Inferencia.las"

print("\nEstadísticas de la nube:", Nombre)


Ruta_Nube = Ruta + Nombre

#Lectura de nube con laspy
Nube = laspy.read(Ruta_Nube)

#Aislar la clasificación manual del IGN de la inferida
clasificacion_IGN = Nube.classification
clasificacion_Inferida = Nube.confidence

#Creación de un DataFrame de panda para analizar los puntos
#Más información en https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
df = pd.DataFrame({
    'IGN': clasificacion_IGN,
    'Inferido': clasificacion_Inferida
})

#Cálculo de la precisión global
glob_prec = (df['IGN'] == df['Inferido']).mean() * 100
print(f"\n    Precisión general de la predicción: {glob_prec:.2f}%")

#Cálculo de la precisión e IoU por cada clase inferida (sin clasificar, terreno, vegetación y edificación)
clases = sorted(df['IGN'].unique())
for clase in clases:
    
    Ptos_acertados = ((df['IGN'] == clase) & (df['Inferido'] == clase)).sum()
    Ptos_Inferidos = (df['Inferido'] == clase).sum()

    if Ptos_Inferidos > 0:
        precision = Ptos_acertados / Ptos_Inferidos * 100
    else:
        precision = 0

    union = ((df['IGN'] == clase) | (df['Inferido'] == clase)).sum()

    if union > 0:
        iou = Ptos_acertados / union * 100
    else:
        iou = 0
    
    print(f"    Clase {clase}: Precision: {precision:.2f}%, IoU: {iou:.2f}%")