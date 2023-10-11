
# %matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import scipy
from scipy import stats
from scipy.stats import skew
from math import sqrt
from numpy import mean, var
import copy 
from sklearn import preprocessing
import json
import psycopg2
from sqlalchemy import create_engine

# Cargamos el dataset
df=pd.read_csv('accidentes-aviones-procesado.csv')
df.head()

# Creamos una nueva columna 'decade' y extraemos la década de la fecha
df['decade'] = df['year'].apply(lambda x: x//10*10)
# Reemplazamos los valores no numericos de la columna 'total_fatalities' por 0
df['total_fatalities'] = pd.to_numeric(df['total_fatalities'], errors='coerce').fillna(0).astype(int)
# Creamos un nuevo DataFrame con las columnas 'decade' y 'total_fatalities'
fatalities_per_decade = df.groupby('decade')['total_fatalities'].sum().reset_index()

# Creamos un nuevo DataFrame con las columnas 'decade' y 'total_accidents'

accidents_per_decade = df.groupby('decade')['total_fatalities'].count().reset_index()

# Renombramos la columna 'total_fatalities' por 'total_accidents'

accidents_per_decade.rename(columns={'total_fatalities': 'total_accidents'}, inplace=True)

# Unimos los dos DataFrames en uno solo
accidents_per_decade = accidents_per_decade.merge(fatalities_per_decade, on='decade')

# Calculamos la tasa de fatalidad de la tripulación
accidents_per_decade['crew_fatality_rate'] = (accidents_per_decade['total_fatalities'] / accidents_per_decade['total_accidents'])/100

# Recorremos todas las décadas y calculamos la disminución de la tasa de fatalidad de la tripulación en los últimos 10 años
for i in range(len(accidents_per_decade)-1):
    # Calculamos la tasa de fatalidad de la tripulación en la década actual
    current_decade = accidents_per_decade.loc[i, 'crew_fatality_rate']
    # Calculamos la tasa de fatalidad de la tripulación en la década anterior
    previous_decade = accidents_per_decade.loc[i+1, 'crew_fatality_rate']
    # Calculamos la disminución de la tasa de fatalidad de la tripulación en los últimos 10 años
    decrease = (previous_decade - current_decade) / previous_decade
    # Guardamos el resultado en el dataset
    accidents_per_decade.loc[i, 'decrease'] = decrease

# Imprimimos el resultado
print(f'La disminución de la tasa de fatalidad de la tripulación en los últimos 10 años fue de {decrease:.2%}')

# # Creamos el gráfico de barras utilizando Seaborn

# plt.figure(figsize=(10, 6))
# sns.barplot(x='decade', y='crew_fatality_rate', data=accidents_per_decade, palette='viridis')
# plt.title('Crew fatality rate by decade')
# plt.xlabel('Decade')
# plt.ylabel('Fatality rate')
# plt.xticks(rotation=45)
# plt.show()

#Crear grafico tipo kpi con la disminución de la tasa de fatalidad de la tripulación por decada
plt.figure(figsize=(10, 6))
sns.barplot(x='decade', y='decrease', data=accidents_per_decade, palette='viridis')
plt.title('Crew fatality rate decrease by decade')
plt.xlabel('Decade')
plt.ylabel('Decrease')
plt.xticks(rotation=45)
plt.show()


accidents_per_decade.to_csv('accidentes-por-decada.csv', index=False)

# Observamos los valores
accidents_per_decade
# print(fatalities_per_decade)