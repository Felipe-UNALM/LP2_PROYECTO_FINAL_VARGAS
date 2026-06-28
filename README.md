# 📊 Monitor IRD: Pipeline de Auditoría de Desinformación en Salud

Este repositorio contiene el código funcional y la arquitectura modular del **Monitor IRD**, un sistema automatizado diseñado para extraer, normalizar, calificar y visualizar el riesgo de desinformación en artículos de salud digital. El proyecto toma como fuentes de análisis la plataforma oficial **MedlinePlus** y el foro de agregación de contenido **Menéame**.

---

## 👥 Integrantes del Grupo
* **Felipe Farro Ochoa, con usuario Felipe-unalm**
* **Isaac Humberto Alvarez Caja, con usuario IsaacAlvarezCaja2026**
* **Sergio Mendoza Chavez, con usuario 290803S**

---

## 🛠️ Arquitectura Modular del Sistema
El proyecto se diseñó bajo una arquitectura desacoplada en 4 capas para garantizar la integridad, trazabilidad y consistencia de los datos analizados:

1. **Capa de Extracción:** Implementación de *scrapers* autónomos para la recolección de datos desde fuentes institucionales (MedlinePlus) y plataformas de agregación social (Menéame).
2. **Capa de Procesamiento (`convertidor.py`):** Componente encargado de la normalización, limpieza de texto, cálculo del **Índice de Riesgo de Desinformación (IRD)** y estructuración de la muestra de auditoría controlada (5 artículos).
3. **Capa de Persistencia (`database.py`):** Gestión de almacenamiento mediante una base de datos relacional **SQLite**, que actúa como fuente única de verdad para la coherencia entre el análisis de riesgos y la visualización.
4. **Capa de Visualización (`app.py`):** Dashboard interactivo desarrollado con **Streamlit** y **Plotly**, que permite la identificación visual inmediata de alertas críticas y la navegación por el dataset auditado.
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

### Paso 3: Ejecutar pipeline de procesamiento y base de datos
```bash
python main.py
```

### Paso 4: Iniciar la interfaz del Dashboard
```bash
streamlit run app.py
```

