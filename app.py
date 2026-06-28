import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

conn = sqlite3.connect("monitor_desinformacion.db")
df = pd.read_sql_query("SELECT * FROM articulos", conn)
conn.close()

st.title("📊 Monitor de Desinformación Científica")

# Métricas
col1, col2, col3 = st.columns(3)
col1.metric("Total Artículos", len(df))
# Aquí buscamos "ALTO RIESGO" en mayúsculas como pediste
alertas = len(df[df["clasificacion"] == "ALTO RIESGO"])
col2.metric("Alertas de Alto Riesgo 🚨", alertas)
col3.metric("Promedio IRD", round(df["puntaje_ird"].mean(), 2))

# Gráfico
fig = px.bar(df, x="titulo", y="puntaje_ird", color="clasificacion")
st.plotly_chart(fig)
