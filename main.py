import os
import subprocess
import database

def ejecutar_pipeline():
    print("--- 🚀 Iniciando Proyecto: Monitor de Desinformación ---")
    
    # 1. Ejecutar scrapers
    print("--- 1. Extrayendo datos...")
    subprocess.run(["python", "scraper_fuente1.py"])
    subprocess.run(["python", "scraper_fuente2.py"])
    
    # 2. Limpieza (si `limpieza.py` requiere ejecución directa)
    print("--- 2. Limpiando datos...")
    subprocess.run(["python", "limpieza.py"])
    
    # 3. Cargar a Base de Datos
    print("--- 3. Creando Base de Datos...")
    database.crear_base_de_datos()
    database.integrar_csv_a_sqlite()
    
    print("--- ✅ Pipeline completado exitosamente. ---")
    print("--- Lanzando Dashboard... ---")
    
    # 4. Lanzar Streamlit
    subprocess.run(["python", "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    ejecutar_pipeline()
