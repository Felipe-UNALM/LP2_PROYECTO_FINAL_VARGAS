import re

def limpiar_texto(texto):
    """
    Elimina ruidos tipográficos, saltos de línea y caracteres especiales,
    pero mantiene letras, números, espacios, comas, puntos y tildes en español.
    """
    if not texto:
        return ""
    
    # 1. Reemplazamos saltos de línea (\n o \r) por un espacio simple
    texto_plano = texto.replace("\n", " ").replace("\r", " ")
    
    # 2. Expresión regular: Borra todo lo que NO sea letras (a-z, A-Z), 
    # números (0-9), tildes, eñes, espacios, puntos o comas.
    texto_limpio = re.sub(r"[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\.,]", "", texto_plano)
    
    # 3. Quitamos espacios dobles o triples que hayan quedado sueltos
    texto_final = " ".join(texto_limpio.split())
    
    return texto_final