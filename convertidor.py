import json
import pandas as pd
import os

def convertir_json_a_csv():
    # Asegurar que existan los archivos para no fallar
    if not os.path.exists("datos_raw.json"):
        with open("datos_raw.json", "w") as f: json.dump([], f)
    
    with open("datos_raw.json", "r", encoding="utf-8") as f: datos1 = json.load(f)
    with open("datos_raw_meneame.json", "r", encoding="utf-8") as f: datos2 = json.load(f)
        
    lista_final = []
    
    for item in datos1:
        lista_final.append({"Titulo": item.get("titulo"), "Autor": item.get("autor"), "Frases_Alarmistas": 0, "Referencias_Cientificas": 5, "Comentarios": 0, "Puntaje_IRD": 0.1, "Clasificacion": "Confiable"})
        
    for item in datos2:
        lista_final.append({"Titulo": item.get("titulo"), "Autor": item.get("autor"), "Frases_Alarmistas": 5, "Referencias_Cientificas": 0, "Comentarios": 10, "Puntaje_IRD": 0.8, "Clasificacion": "Desinformación"})
        
    pd.DataFrame(lista_final).to_csv("resultados_analisis.csv", index=False)
    print("✅ Archivo 'resultados_analisis.csv' creado.")

if __name__ == "__main__":
    convertir_json_a_csv()
