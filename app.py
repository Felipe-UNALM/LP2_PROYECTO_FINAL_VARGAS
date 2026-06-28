import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# 1. Conexión y extracción de datos desde el motor relacional (SQLite)
conn = sqlite3.connect("monitor_desinformacion.db")
df = pd.read_sql_query("SELECT * FROM articulos", conn)
conn.close()

# 2. Configuración de la cabecera principal de la interfaz web
st.title("📊 Monitor de Desinformación Científica")

# 3. Construcción de Métricas (KPIs)
col1, col2, col3 = st.columns(3)

col1.metric("Total Artículos", len(df)) # KPI 1

# Conteo de alertas críticas (Filtro por clasificación condicional)
alertas = len(df[df["clasificacion"] == "ALTO RIESGO"])
col2.metric("Alertas de Alto Riesgo 🚨", alertas) #KPI 2
col3.metric("Promedio IRD", round(df["puntaje_ird"].mean(), 2)) # KPI 3

# 4. Gráfico de barras para el Dashboard
fig = px.bar(
    df, 
    x="titulo", 
    y="puntaje_ird", 
    color="clasificacion"
)
st.plotly_chart(fig)
