import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

# Configuración estética de la ventana web
st.set_page_config(page_title="Monitor de Desinformación", page_icon="📊", layout="wide")

DB_NAME = "monitor_desinformacion.db"

st.title("📊 Monitor de Desinformación Científica en Salud")
st.markdown("**Fase 3: Visualización de Resultados e Interfaz Analítica (Rol: Isaac)**")
st.text("Proyecto Final - Visualización de Datos desde Motor SQLite Embebido")
st.divider()  # <-- CORREGIDO AQUÍ

# REQUISITO EXIGIDO: Consumir la data directamente de la Base de Datos SQLite
try:
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM articulos", conn)
    conn.close()
except Exception as e:
    st.error(f"❌ Error de conexión a la base de datos: {e}")
    df = pd.DataFrame()

if df.empty:
    st.warning("⚠️ La base de datos SQLite está vacía o no ha sido inicializada. Ejecuta 'python database.py' primero.")
else:
    # 📈 Sección de Métricas Clave (KPIs)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Artículos Auditados", value=len(df))
    with col2:
        alertas = len(df[df["clasificacion"] == "ALTO RIESGO"])
        st.metric(label="Alertas de Alto Riesgo 🚨", value=alertas, delta=f"{alertas} críticas", delta_color="inverse")
    with col3:
        st.metric(label="Promedio de Riesgo Global (IRD)", value=round(df["puntaje_ird"].mean(), 2))
        
    st.divider()  # <-- CORREGIDO AQUÍ
    
    # 📊 Gráficos Estadísticos con Plotly
    col_izq, col_der = st.columns(2)
    with col_izq:
        st.subheader("📈 Índice de Riesgo (IRD) por Publicación")
        fig_bar = px.bar(
            df, x="titulo", y="puntaje_ird", color="clasificacion",
            labels={"titulo": "Artículo", "puntaje_ird": "Puntaje IRD"},
            title="Escáner Estadístico de Riesgo",
            color_discrete_map={"ALTO RIESGO": "#e53e3e", "CONFIABLE": "#38a169", "RIESGO MODERADO": "#dd6b20"}
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        
    with col_der:
        st.subheader("📊 Distribución del Contenido Analizado")
        fig_pie = px.pie(
            df, names="clasificacion", title="Porcentaje de Contenido por Categoría",
            color="clasificacion",
            color_discrete_map={"ALTO RIESGO": "#e53e3e", "CONFIABLE": "#38a169", "RIESGO MODERADO": "#dd6b20"}
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        
    st.divider()  # <-- CORREGIDO AQUÍ
    
    # 🗄️ Tabla Relacional desde SQLite
    st.subheader("🗄️ Datos Extraídos del Motor Relacional Local (`monitor_desinformacion.db`)")
    st.dataframe(df.style.background_gradient(cmap="YlOrRd", subset=["puntaje_ird"]), use_container_width=True)