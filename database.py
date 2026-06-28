import sqlite3
import os
import pandas as pd

DB_NAME = "monitor_desinformacion.db"
CSV_NAME = "resultados_analisis.csv"

def crear_base_de_datos():
    """Diseña e inicializa la estructura relacional en el motor SQLite."""
    print("🗄️ Inicializando conexión con SQLite y estructurando tablas...")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Definición de esquema con restricciones de integridad de datos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articulos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT,
            frases_alarmistas INTEGER,
            referencias_cientificas INTEGER,
            comentarios INTEGER,
            puntaje_ird REAL,
            clasificacion TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("✅ Base de datos 'monitor_desinformacion.db' estructurada correctamente.")

def integrar_csv_a_sqlite():
    """Ejecuta el proceso ETL para migrar y persistir los datos del CSV en la base de datos."""
    if not os.path.exists(CSV_NAME):
        print(f"⚠️ Error de consistencia: No se encontró el archivo '{CSV_NAME}'.")
        return
        
    print(f"🔄 Procesando e inyectando registros desde '{CSV_NAME}' hacia SQLite...")
    df_csv = pd.read_csv(CSV_NAME)
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Limpieza preventiva de la tabla para evitar redundancia o duplicados en ejecuciones sucesivas
    cursor.execute("DELETE FROM articulos")
    
    # Iteración e inserción parametrizada de tuplas para mitigar inyecciones
    for _, fila in df_csv.iterrows():
        cursor.execute("""
            INSERT INTO articulos (titulo, autor, frases_alarmistas, referencias_cientificas, comentarios, puntaje_ird, clasificacion)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            fila["Titulo"], 
            fila["Autor"], 
            int(fila["Frases_Alarmistas"]), 
            int(fila["Referencias_Cientificas"]), 
            int(fila["Comentarios"]), 
            float(fila["Puntaje_IRD"]), 
            fila["Clasificacion"]
        ))
        
    conn.commit()
    conn.close()
    print("✅ Proceso de inyección finalizado. Tuplas disponibles para consumo del Dashboard.")

if __name__ == "__main__":
    crear_base_de_datos()
    integrar_csv_a_sqlite()