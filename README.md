<p align='center'>
<img src ="https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png">
<p>

<h1 align='center'>
 <b>PROYECTO INDIVIDUAL Nº2</b>
</h1>
 
# <h1 align="center">**`Accidentes Aereos`**</h1>

El proyecto tiene como objetivo mejorar la comprensión y el análisis de los accidentes aéreos a través de un proceso de Data Analytics. Para lograr esto, se seguirán una serie de pasos que permitirán trabajar con el dataset de accidentes aéreos y crear un Dashboard Interactivo utilizando Power BI.
<p align='center'>
<img src="./avion.jpg"  height=300>
<p>

## **Descripción 🚀 -**

### **Contexto**

Los accidentes aéreos son eventos trágicos que tienen un impacto significativo en la seguridad de la aviación civil. Estos accidentes pueden ser causados por una variedad de factores, como errores humanos, fallas en los equipos, condiciones meteorológicas adversas y problemas de mantenimiento. Además de las pérdidas humanas, los accidentes aéreos también pueden resultar en daños económicos significativos.

Para mejorar la seguridad en la aviación civil, es crucial analizar los datos históricos de accidentes aéreos. Este análisis puede ayudar a identificar patrones, tendencias y factores contribuyentes que pueden ser abordados para prevenir futuros accidentes. Al comprender las causas subyacentes de los accidentes, se pueden implementar medidas preventivas efectivas 



## **Propòsito-**
La información se centra en vuelos que han sufrido un siniestro a lo largo de todo el mundo desde 1908 hasta 2021. El mismo cuenta con 5008 filas (representando cada fila un accidente aéreo) y 18 columnas (atributos de cada vuelo).

Con estos datos analizaremos las características de vuelos siniestrados a los efectos de analizar los siguientes KPI's propuestos:

🚀Evaluar la disminución del 10% en la tasa de fatalidad de la tripulación en los últimos 10 años(Suma total de fallecidos en el período de tiempo / Suma total de accidentes en el período de tiempo), en comparación con la década anterior.

🚀Estimar el Aumento en la tasa anual de supervivencia (personas sobrevivientes / personas a bordo) para aerolíneas con gran cantidad de accidentes históricos.


## ***Analisis exploratorio de datos***
A los efectos de poder entender los datos presentados, se realizaron una serie de análisis y estudios sobre las variables a los efectos de poder encontrar relaciones entre los datos y comprender la relevancia de los mismos. Dentro de los análisis efectuados se encuentran:

**Nubes de palabras para identificar causas comunes en las descripciones de los accidentes;

**Análisis de accidentes, tasa de mortalidad, tasa de supervivencia y seguridad en vuelos por: país y aerolínea;

**Distribuciones de frecuencias y estadísticas de las variables numéricas;

**Identificación de variables categóricas y sus valores;
Análisis de accidentes por: país, aerolínea, aeronave y categoría de vuelo;

**Análisis temporales por año
## ***Exportacion a base de datos***

Una vez finalizadas las transformaciones necesarias sobre el archivo csv, se procedió a ingestar el dataframe resultante en una base de datos postgresql a través de python estableciendo la conexión correspondiente con la librería.

## ***Dashboard***
Se presentarán visualizaciones que permitirán analizar la distribución de los accidentes aéreos a lo largo del tiempo. Esto será de gran ayuda para identificar patrones, tendencias y cambios en la frecuencia de los accidentes. Algunas de las problemáticas a desarrollar y las posibles soluciones podrían incluir:

Identificación de áreas de mayor riesgo: Mediante la visualización de los accidentes en un mapa geográfico, se podrán identificar las áreas con mayor concentración de accidentes. Esto permitirá tomar medidas preventivas y mejorar la seguridad en esas zonas.

Análisis de factores contribuyentes: Al analizar los accidentes en función de diferentes variables, como el tipo de aeronave, se podrán identificar los factores que contribuyen a la ocurrencia de accidentes. Esto permitirá implementar medidas correctivas y mejorar los protocolos de seguridad.

Seguimiento de tendencias: Al visualizar la evolución de los accidentes a lo largo del tiempo, se podrán identificar tendencias y cambios en la frecuencia de los accidentes. Esto permitirá evaluar la efectividad de las medidas implementadas y realizar ajustes en los protocolos de seguridad.

Comparación de categorías de accidentes: Mediante la visualización de los accidentes según su categoría, como accidentes no militar o militares,y se podrán identificar diferencias en la frecuencia y gravedad de los accidentes. Esto permitirá enfocar los esfuerzos de mejora en las áreas más críticas.
## Fuente de datos
**Obligatorio:**

- Dataset principal, incluido en el repositorio del proyecto.

**Complementario:**
- [National Transportation Safety Board](https://www.ntsb.gov/safety/data/Pages/Data_Stats.aspx)
- [Aviation Safety Network](https://aviation-safety.net/database/)
- [Federal Aviation Administration](https://www.faa.gov/data_research/accident_incident)
- Cualquier dataset de búsqueda propia que complemente y mejore el análisis.









  
 