
# PROYECTO : ANÁLISIS EXPLORATORIO DE DATOS (EDA) - VENTAS DE VIDEOJUEGOS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar el estilo de las gráficas
sns.set_style('whitegrid')
plt.style.use('seaborn-v0_8-pastel')


print("Cargando el dataset...")

df = pd.read_csv('vgsales.csv')

print("--- Primeras 5 filas del dataset ---")
print(df.head())

print("\n--- Información general del DataFrame ---")
df.info()

print("\n--- Conteo de valores nulos por columna ---")
print(df.isnull().sum())


# LIMPIEZA DE DATOS --
print("\nIniciando limpieza de datos...")

df.dropna(inplace=True)

# Corregir el tipo de dato de la columna 'Year'
df['Year'] = df['Year'].astype(int)

print("Datos limpios. No hay valores nulos.")
print("Tipo de dato de 'Year' corregido a entero.")


# ANÁLISIS POR GÉNERO ---
print("\n--- Realizando análisis por Género ---")
# Agrupar por género y sumar las ventas globales
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

# Crear la visualización de Géneros
plt.figure(figsize=(12, 7))
sns.barplot(x=genre_sales.index, y=genre_sales.values, palette="viridis")
plt.title('Ventas Globales Totales por Género de Videojuego', fontsize=16)
plt.xlabel('Género', fontsize=12)
plt.ylabel('Ventas Globales (en millones)', fontsize=12)
plt.xticks(rotation=45)
plt.show()


# EVOLUCIÓN DE GÉNEROS A TRAVÉS DEL TIEMPO ---
print("\n--- Realizando análisis de tendencias de Géneros por Año ---")
# Identificar los 5 géneros más vendidos
top_5_genres = genre_sales.index[:5]
df_top_genres = df[df['Genre'].isin(top_5_genres)]

# Crear una tabla pivote para el análisis de tendencias
genre_trends = df_top_genres.pivot_table(index='Year', columns='Genre', values='Global_Sales', aggfunc='sum').fillna(0)

# Crear la visualización de Tendencias
plt.figure(figsize=(15, 8))
sns.lineplot(data=genre_trends)
plt.title('Evolución de Ventas de los 5 Géneros Principales (1980-2017)', fontsize=18)
plt.xlabel('Año de Lanzamiento', fontsize=12)
plt.ylabel('Ventas Globales (en millones)', fontsize=12)
plt.legend(title='Género')
plt.show()


# -ANÁLISIS POR PLATAFORMA---
print("\n--- Realizando análisis por Plataforma ---")
# Agrupar por plataforma y sumar las ventas globales (Top 10)
platform_sales = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)

# Crear la visualización de Plataformas
plt.figure(figsize=(12, 8))
sns.barplot(x=platform_sales.values, y=platform_sales.index, palette="mako")
plt.title('Top 10 Plataformas por Ventas Globales de Software', fontsize=16)
plt.xlabel('Ventas Globales (en millones)', fontsize=12)
plt.ylabel('Plataforma', fontsize=12)
plt.show()


# ANÁLISIS POR COMPAÑÍA---
print("\n--- Realizando análisis por Publisher ---")
# Agrupar por compañía y sumar las ventas globales (Top 10)
publisher_sales = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10)

# Crear la visualización de Publishers
plt.figure(figsize=(12, 8))
sns.barplot(x=publisher_sales.values, y=publisher_sales.index, palette="rocket")
plt.title('Top 10 Publishers por Ventas Globales de Software', fontsize=16)
plt.xlabel('Ventas Globales (en millones)', fontsize=12)
plt.ylabel('Publisher', fontsize=12)
plt.show()

print("\n¡Análisis completado!")