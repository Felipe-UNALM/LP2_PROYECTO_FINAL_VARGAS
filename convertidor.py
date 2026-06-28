import json
import pandas as pd

def convertir_json_a_csv():
    # 1. Leer los datos de los dos scrapers
    with open("datos_raw.json", "r", encoding="utf-8") as f:
        datos1 = json.load(f)
    
    with open("datos_raw_meneame.json", "r", encoding="utf-8") as f:
        datos2 = json.load(f)
        
    # 2. Combinar y formatear para que coincida con lo que espera database.py
    lista_final = []
    
    # Procesar Medline
    for item in datos1:
        lista_final.append({
            "Titulo": item["titulo"], "Autor": item["autor"], 
            "Frases_Alarmistas": 0, "Referencias_Cientificas": item["enlaces_externos"], 
            "Comentarios": 0, "Puntaje_IRD": 0.1, "Clasificacion": "Confiable"
        })
        
    # Procesar Meneame
    for item in datos2:
        lista_final.append({
            "Titulo": item["titulo"], "Autor": item["autor"], 
            "Frases_Alarmistas": 5, "Referencias_Cientificas": 0, 
            "Comentarios": int(item["metricas_sociales"]["comentarios"]), 
            "Puntaje_IRD": 0.8, "Clasificacion": "Desinformación"
        })
        
    # 3. Guardar como CSV
    df = pd.DataFrame(lista_final)
    df.to_csv("resultados_analisis.csv", index=False)
    print("✅ Archivo 'resultados_analisis.csv' creado exitosamente.")

if __name__ == "__main__":
    convertir_json_a_csv()
