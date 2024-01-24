#1. IMPORTAR EL PAQUETE O PAQUETES CON LOS QUE VOY ANALIZAR LA INFORMARCION

import pandas as pd 

def analizarCanastaBasica():
#2. SIN IMPORTAR LA FUENTE (SQL,XLS,JSON, CSV....)
#CREAR  UNA TABLA TABULADA QUE SE LLAMA DATAFRAME 

    tabla=pd.read_csv('./data/bdcanasta.csv')

    #print(tabla)

#3. Aplico filtros para filtrar o seleccionar datos 
    
    #print(tabla.head(20)) #primeros N registros 

    #print(tabla.tail(10))
    print(tabla.describe())