import sqlite3
import pandas as pd

def crear_base_de_datos():
    conn = sqlite3.connect("monitor_desinformacion.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS articulos")
    cursor.execute("""
        CREATE TABLE articulos (
            titulo TEXT, autor TEXT, frases_alarmistas INTEGER, 
            referencias_cientificas INTEGER, comentarios INTEGER, 
            puntaje_ird REAL, clasificacion TEXT
        )
    """)
    conn.commit()
    conn.close()

def integrar_csv_a_sqlite():
    df = pd.read_csv("resultados_analisis.csv")
    conn = sqlite3.connect("monitor_desinformacion.db")
    df.to_sql("articulos", conn, if_exists="replace", index=False)
    conn.close()
    print("✅ Base de datos cargada correctamente.")
