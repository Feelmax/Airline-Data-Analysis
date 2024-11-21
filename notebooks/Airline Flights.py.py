# Databricks notebook source
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# COMMAND ----------

# Lendo os dados
caminho_csv = "dbfs:/FileStore/tables/flights.csv"

spark_df = spark.read\
    .format("csv")\
    .option("header", True)\
    .option("sep", ",")\
    .option("inferSchema", True)\
    .load(caminho_csv)

# COMMAND ----------

# Convertendo Spark para Pandas
df = spark_df.toPandas()

# COMMAND ----------

# 1. Volume de voos por meses e dia da semana
voos_por_mes = df.groupby('MONTH').size().reset_index(name='total_voos')
voos_por_dia = df.groupby('DAY_OF_WEEK').size().reset_index(name='to  tal_voos')

# COMMAND ----------

display(voos_por_mes)

# COMMAND ----------

display(voos_por_dia)

# COMMAND ----------

# 2. Análise de atrasos
total_voos = len(df)
voos_atrasados = df[df['DEPARTURE_DELAY'] > 0]
perc_atrasos = (len(voos_atrasados) / total_voos) * 100
tempo_medio_atraso = voos_atrasados['DEPARTURE_DELAY'].mean()

# COMMAND ----------

display(voos_atrasados)
display(tempo_medio_atraso)

# COMMAND ----------

# 3. Atrasos por mes (geral e BOS)
atrasos_mes = df.groupby('MONTH').apply(
    lambda x: (x['DEPARTURE_DELAY'] > 0).mean() * 100
).reset_index(name='perc_atrasos')

atrasos_bos = df[df['ORIGIN_AIRPORT'] == 'BOS'].groupby('MONTH').apply(
    lambda x: (x['DEPARTURE_DELAY'] > 0).mean() * 100
).reset_index(name='perc_atrasos_bos')

# COMMAND ----------

display(atrasos_mes)

# COMMAND ----------

display(atrasos_bos)

# COMMAND ----------

# 4. Analise de cancelamentos
total_cancelados = df['CANCELLED'].sum()
perc_cancelados = (total_cancelados / total_voos) * 100

cancelamentos_motivo = df[df['CANCELLED'] == 1]['CANCELLATION_REASON'].value_counts()

# COMMAND ----------

display(cancelamentos_motivo)

# COMMAND ----------

# 5. Confiabilidade das companhias aéreas
confiabilidade_airlines = df.groupby('AIRLINE').agg({
    'DEPARTURE_DELAY': lambda x: (x <= 0).mean() * 100
}).reset_index()
confiabilidade_airlines.columns = ['AIRLINE', 'PONTUALIDADE']
confiabilidade_airlines = confiabilidade_airlines.sort_values('PONTUALIDADE', ascending=False)

# COMMAND ----------

display(confiabilidade_airlines)

# COMMAND ----------

# Salvando os dados processados para o Power BI
voos_por_mes.to_csv('voos_por_mes.csv', index=False)
voos_por_dia.to_csv('voos_por_dia.csv', index=False)
atrasos_mes.to_csv('atrasos_mensais.csv', index=False)
atrasos_bos.to_csv('atrasos_bos.csv', index=False)
confiabilidade_airlines.to_csv('confiabilidade_airlines.csv', index=False)

