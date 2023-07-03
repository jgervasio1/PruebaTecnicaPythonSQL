
import pandas as pd
import numpy as np

df = pd.read_csv("datos_arts.csv")
df['fecha'] = pd.to_datetime(df['fecha'],dayfirst=True)

#punto 2

#Primero agrupo por fecha para asi tener los dias separados, luego hago un aggregate con la canitdad de articulos y la suma de todos los importes y por ultimo renombro las columnas

cantidadArticulosImporte = df.groupby('fecha').agg({'articulo' : 'size', 'importe' : 'sum'}).rename(columns={'articulo': 'cantidadArtículos', 'importe': 'importeTotal'}).reset_index()

print(cantidadArticulosImporte)



#punto 3

#Primero creo una lista de condiciones booleanas y luego una lista de opciones. Despues, con la libreria numpy hago un where donde si se cumple tal condicion se toma en cuenta tal opcion


condiciones=[(df['grupo'] == '15 LIMPIEZA DEL HOGAR') | (df['grupo'] == '18 PERFUMERIA'),(df['grupo'] == '4 LACTEOS') | (df['grupo'] == '9 FIAMBRERIA' )]

opciones= ['No Comestibles','Perecederos']

df['Sector'] = np.where(condiciones[0],opciones[0],np.where(condiciones[1],opciones[1],df['grupo']))

print(df)



#punto 4
#Primero creo una pivot table y uso la funcion dt.strftime para agruparlos por mes y que tenga la estructura de (ago-20)
#luego de asignar la columna y los valores hago un aggfunc para calcular el promedio y la suma
#despues hago un for dentro de un for para conseguir el nombre de la columna que queria y lo ordeno con el sortindex y finalmente le saco el nombre del index
#para que quede el resultado como se solicito

resultado = df.pivot_table(index=df['fecha'].dt.strftime('%b %y'), columns='Sector', values=['precio', 'importe'], aggfunc={'precio': 'mean', 'importe': 'sum'} )
resultado.columns = [f"{sector} {tipo}" for tipo in ['sumaImporte', 'promedioPrecio'] for sector in resultado.columns.levels[1]]
resultado = resultado.sort_index(axis=1)
resultado.index.name = None



print(resultado)









# %%
