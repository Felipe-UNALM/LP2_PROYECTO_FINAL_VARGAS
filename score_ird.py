import json
import pandas as pd
import os

# Importamos las funciones que creamos en los pasos anteriores
from limpieza import limpiar_texto
from regex_patterns import analizar_texto_regex

def calcular_pipeline_fase2():
    print("🧠 [Felipe - Motor IRD] Iniciando procesamiento de texto...")
    
    # Las fuentes que tú extrajiste en la Fase 1
    archivos_fuente = ["datos_raw.json", "datos_raw_meneame.json"]
    lista_articulos_procesados = []
    
    for archivo in archivos_fuente:
        # Verificamos si el archivo JSON existe en la carpeta
        if not os.path.exists(archivo):
            print(f"⚠️ Archivo no encontrado: {archivo}. Asegúrate de que esté en esta carpeta.")
            continue
            
        with open(archivo, "r", encoding="utf-8") as f:
            articulos = json.load(f)
            
        for art in articulos:
            # 1. Unimos título y texto principal para analizar todo junto
            texto_completo = art["titulo"] + " " + art["texto_principal"]
            
            # 2. Llamamos al script de limpieza
            texto_limpio = limpiar_texto(texto_completo)
            
            # 3. Llamamos al script de Regex para contar palabras clave
            frases_alarmistas, referencias_cientificas = analizar_texto_regex(texto_limpio)
            
            # 4. Extraemos los comentarios de tus JSON de forma segura
            try:
                comentarios = int(art["metricas_sociales"].get("comentarios", 0))
            except:
                comentarios = 0
                
            # 5. APLICAMOS LA FÓRMULA MATEMÁTICA DEL IRD
            # Alarmismo (+3 por frase), Viralidad (+0.1 por comentario), Ciencia (-2 por referencia)
            score_ird = (frases_alarmistas * 3) + (comentarios * 0.1) - (referencias_cientificas * 2)
            
            # 6. Clasificamos según el puntaje
            if score_ird > 5:
                clasificacion = "ALTO RIESGO"
            elif score_ird >= 1:
                clasificacion = "RIESGO MODERADO"
            else:
                clasificacion = "CONFIABLE"
                
            # Guardamos los resultados ordenados en un diccionario
            lista_articulos_procesados.append({
                "Titulo": art["titulo"],
                "Autor": art["autor"],
                "Frases_Alarmistas": frases_alarmistas,
                "Referencias_Cientificas": referencias_cientificas,
                "Comentarios": comentarios,
                "Puntaje_IRD": round(score_ird, 2),
                "Clasificacion": clasificacion
            })

    # Convertimos toda la lista a un DataFrame de Pandas y lo exportamos a CSV
    if lista_articulos_procesados:
        df = pd.DataFrame(lista_articulos_procesados)
        df.to_csv("resultados_analisis.csv", index=False, encoding="utf-8-sig")
        print("\n✅ ¡Fase 2 terminada con éxito!")
        print("📁 Archivo generado: 'resultados_analisis.csv'")
        print(df[["Titulo", "Puntaje_IRD", "Clasificacion"]])
    else:
        print("❌ No se pudo procesar ningún dato. Revisa tus archivos JSON.")

if __name__ == "__main__":
    calcular_pipeline_fase2()