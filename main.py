import subprocess
import database
import convertidor  # <- Añade esta importación

def ejecutar_pipeline():
    print("🚀 Iniciando extracción...")
    subprocess.run(["python", "scraper_fuente1.py"])
    subprocess.run(["python", "scraper_fuente2.py"])
    
    print("🚀 Convirtiendo datos a formato compatible...")
    convertidor.convertir_json_a_csv() # <- Nueva línea
    
    print("🚀 Cargando a Base de Datos...")
    database.crear_base_de_datos()
    database.integrar_csv_a_sqlite()
    
    print("✅ Pipeline completado. Lanzando Dashboard...")
    subprocess.run(["python", "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    ejecutar_pipeline()
