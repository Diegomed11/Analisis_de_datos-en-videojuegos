# Análisis Exploratorio de Datos (EDA) - Ventas de Videojuegos (1980-2020)

## 📖 Descripción del Proyecto

Este proyecto realiza un análisis exploratorio de datos sobre un conjunto de datos que contiene las ventas de más de 16,500 videojuegos. El objetivo es descubrir tendencias y patrones históricos en la industria de los videojuegos, respondiendo a preguntas clave sobre la popularidad de géneros, plataformas y compañías (publishers).

---

## 💾 Dataset

El conjunto de datos utilizado es el **"Video Game Sales"** obtenido de Kaggle. Contiene información detallada sobre videojuegos lanzados entre 1980 y 2020.

- **Fuente:** [Kaggle - Video Game Sales Dataset](https://www.kaggle.com/datasets/gregorut/videogamesales)

---

## ❓ Preguntas Clave del Análisis

El análisis se centró en responder las siguientes preguntas de negocio:

1.  **¿Cuáles son los géneros de videojuegos más vendidos de todos los tiempos?**
2.  **¿Cómo ha evolucionado la popularidad de los géneros más importantes a lo largo de los años?**
3.  **¿Cuáles han sido las plataformas (consolas) más exitosas en términos de ventas de software?**
4.  **¿Qué compañías (publishers) dominan el mercado de los videojuegos?**

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python
- **Librerías:**
  - **Pandas:** Para la carga, limpieza y manipulación de datos.
  - **Matplotlib y Seaborn:** Para la creación de visualizaciones de datos.
- **Entorno:** Jupyter Notebook

---

## 📊 Hallazgos y Visualizaciones

A continuación se presentan los principales hallazgos del análisis:

### 1. Géneros más Populares
El análisis revela que el género de **Acción** es el líder indiscutible en ventas globales, seguido por **Deportes** y **Shooter**.

![Gráfico de Ventas por Género](https://github.com/Diegomed11/Analisis_de_datos-en-videojuegos/blob/main/images/ventasporgenero.png?raw=true)

### 2. Evolución de los Géneros
Se observa un pico masivo en las ventas de videojuegos entre 2008 y 2011, con el género de **Acción** mostrando un crecimiento exponencial durante la era de la PS3 y Xbox 360.

![Gráfico de Evolución de Géneros](https://github.com/Diegomed11/Analisis_de_datos-en-videojuegos/blob/main/images/evoluciongenero.png?raw=true)

### 3. Plataformas más Exitosas
La **PlayStation 2** y la **Xbox 360** se posicionan como las consolas con mayor venta de software en la historia, destacando la "era dorada" de los videojuegos.

![Gráfico de Ventas por Plataforma](RUTA/A/TU/IMAGEN/plataformas.png)

### 4. Publishers Dominantes
**Nintendo** lidera el mercado de manera abrumadora, beneficiándose de ser un desarrollador first-party para sus exitosas consolas. Le siguen gigantes como **Electronic Arts** y **Activision**.

![Gráfico de Ventas por Publisher](https://github.com/Diegomed11/Analisis_de_datos-en-videojuegos/blob/main/images/toppublisher.png?raw=true)

---

## 🚀 Cómo Ejecutar
Para replicar este análisis:
1. Clona el repositorio.
2. Asegúrate de tener el archivo `vgsales.csv` en la misma carpeta.
3. Ejecuta el Jupyter Notebook `Analisis_Videojuegos.ipynb`.
