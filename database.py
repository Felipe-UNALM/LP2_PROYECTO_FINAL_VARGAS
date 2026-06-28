import sqlite3
import os
import pandas as pd

DB_NAME = "monitor_desinformacion.db"
CSV_NAME = "resultados_analisis.csv"

def crear_base_de_datos():
    """Diseña la estructura relacional en SQLite."""
    print("🗄️ [Isaac - DB] Conectando a SQLite y creando tablas...")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Creación de la tabla con restricciones de integridad de datos
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
    print("✅ Base de datos 'monitor_desinformacion.db' estructurada con éxito.")

def integrar_csv_a_sqlite():
    """Migra los datos del CSV de Sergio (Fase 2) hacia las tuplas de SQLite."""
    if not os.path.exists(CSV_NAME):
        print(f"⚠️ Error: No se encontró '{CSV_NAME}'. Ejecuta primero la Fase 2 de Sergio.")
        return
        
    print(f"🔄 [Isaac - ETL] Insertando registros de {CSV_NAME} en SQLite...")
    df_csv = pd.read_csv(CSV_NAME)
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Limpiamos la tabla para evitar registros duplicados en la simulación
    cursor.execute("DELETE FROM articulos")
    
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
    print("✅ Inyección de datos completada. Tuplas listas en el motor relacional.")

if __name__ == "__main__":
    crear_base_de_datos()
    integrar_csv_a_sqlite()