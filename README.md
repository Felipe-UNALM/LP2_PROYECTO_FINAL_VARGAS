# 📊 Monitor IRD: Pipeline de Auditoría de Desinformación en Salud

Este repositorio contiene el código funcional y la arquitectura modular del **Monitor IRD**, un sistema automatizado diseñado para extraer, normalizar, calificar y visualizar el riesgo de desinformación en artículos de salud digital. El proyecto toma como fuentes de análisis la plataforma oficial **MedlinePlus** y el foro de agregación de contenido **Menéame**.

---

## 👥 Integrantes del Grupo
* **Felipe Farro Ochoa, con usuario Felipe-unalm**
* **Isaac Humberto Alvarez Caja, con usuario IsaacAlvarezCaja2026**
* **Sergio Mendoza Chavez, con usuario 290803S**

---

## 🛠️ Arquitectura Modular del Sistema

El proyecto se diseñó bajo una arquitectura desacoplada en 5 capas consecutivas (Pipeline Secuencial de Datos):

1. **Capa Ética (`robots_checker.py`):** Consulta nativa mediante `urllib.robotparser` para verificar las directivas del archivo `robots.txt` de cada web antes de iniciar la extracción.
2. **Capa de Extracción (`scraper_fuente1.py` / `scraper_fuente2.py`):** Consumo de URLs por lotes mediante peticiones concurrentes con la librería `requests` y parseo del árbol HTML con `BeautifulSoup`.
3. **Capa de Normalización y Orquestación (`limpieza.py`):** Script central que limpia el texto (remoción de etiquetas, caracteres especiales y normalización de minúsculas) y coordina el flujo de los datos.
4. **Capa Analítica (`regex_patterns.py` y `score_ird.py`):** Motor de cálculo del Índice IRD. Aplica penalizaciones estrictas mediante Expresiones Regulares: un peso macro de **+3.0** por cada interacción/enlace de propagación externo y un peso micro acumulativo de **+0.1** por densidad lingüística de términos alarmistas.
5. **Capa de Persistencia Relacional y UI (`database.py` & `app.py`):** Almacenamiento indexado en una base de datos relacional SQLite mediante inyección SQL, la cual sirve de fuente directa para el Dashboard interactivo desarrollado en **Streamlit** con gráficos dinámicos de **Plotly**.

---

## 🚀 Guía de Instalación y Ejecución Paso a Paso

Estimada profesora, para evaluar el correcto funcionamiento del proyecto en su máquina local, por favor abra su terminal de comandos (Consola, Terminal o Git Bash) y siga estrictamente el orden de los siguientes pasos:

### Paso 1: Clonar el repositorio y acceder al proyecto
Primero, descargue el código de este repositorio ejecutando el siguiente comando:
```bash
git clone [https://github.com/Felipe-UNALM/LP2_PROYECTO_FINAL_VARGAS.git](https://github.com/Felipe-UNALM/LP2_PROYECTO_FINAL_VARGAS.git)
cd LP2_PROYECTO_FINAL_VARGAS
```

### Paso 2: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar pipeline de procesamiento
```bash
python limpieza.py
```

### Paso 4: Iniciar la aplicación
```bash
streamlit run app.py
```

