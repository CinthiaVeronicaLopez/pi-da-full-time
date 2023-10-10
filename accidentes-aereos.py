
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
print(fatalities_per_decade.head())


# Creamos un nuevo DataFrame con las columnas 'decade' y 'total_accidents'

# accidents_per_decade = df.groupby('decade')['total_fatalities'].count().reset_index()

# Renombramos la columna 'total_fatalities' por 'total_accidents'

# accidents_per_decade.rename(columns={'total_fatalities': 'total_accidents'}, inplace=True)

# Unimos los dos DataFrames en uno solo
# accidents_per_decade = accidents_per_decade.merge(fatalities_per_decade, on='decade')

# Calculamos la tasa de fatalidad de la tripulación
#accidents_per_decade['crew_fatality_rate'] = accidents_per_decade['total_fatalities'] / accidents_per_decade['total_accidents']


# print(fatalities_per_decade)