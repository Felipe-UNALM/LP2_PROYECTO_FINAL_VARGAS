import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

# Configuración de la interfaz gráfica del Dashboard
st.set_page_config(page_title="Monitor de Desinformación", page_icon="📊", layout="wide")

DB_NAME = "monitor_desinformacion.db"

# Cabecera principal del entorno web
st.title("📊 Monitor de Desinformación Científica en Salud")
st.markdown("**Panel Analítico Interactiva de Control Sanitario**")
st.text("Visualización en tiempo real desde el motor relacional SQLite")
st.divider()

# Extracción y lectura de datos desde SQLite
try:
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM articulos", conn)
    conn.close()
except Exception as e:
    st.error(f"❌ Error de conexión a la base de datos: {e}")
    df = pd.DataFrame()

# Validación de consistencia de datos antes de renderizar componentes
if df.empty:
    st.warning("⚠️ La base de datos SQLite está vacía o no ha sido inicializada. Ejecute 'database.py' primero.")
else:
    # Bloque de Métricas Clave de Control (KPIs)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Artículos Auditados", value=len(df))
    with col2:
        alertas = len(df[df["clasificacion"] == "ALTO RIESGO"])
        st.metric(label="Alertas de Alto Riesgo 🚨", value=alertas, delta=f"{alertas} críticas", delta_color="inverse")
    with col3:
        st.metric(label="Promedio de Riesgo Global (IRD)", value=round(df["puntaje_ird"].mean(), 2))
        
    st.divider()
    
    # Renderizado de gráficos estadísticos mediante Plotly Express
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
        
    st.divider()
    
    # Visualización de la matriz de datos con formato condicional semafórico
    st.subheader("🗄️ Datos Extraídos del Motor Relacional Local (`monitor_desinformacion.db`)")
    st.dataframe(df.style.background_gradient(cmap="YlOrRd", subset=["puntaje_ird"]), use_container_width=True)