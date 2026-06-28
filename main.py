import subprocess
import database
import convertidor

def ejecutar_pipeline():
    print("--- 🚀 Iniciando Sistema ---")
    subprocess.run(["python", "scraper_fuente1.py"])
    subprocess.run(["python", "scraper_fuente2.py"])
    convertidor.convertir_json_a_csv()
    database.crear_base_de_datos()
    database.integrar_csv_a_sqlite()
    print("--- ✅ Pipeline completo. Iniciando Dashboard ---")
    subprocess.run(["python", "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    ejecutar_pipeline()
