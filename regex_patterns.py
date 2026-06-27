import re

# Patrones para detectar lenguaje sensacionalista, alarmista o conspirativo
# El (?i) al inicio significa "Ignore case" (le da igual si está en mayúsculas o minúsculas)
PATRONES_ALARMISTAS = [
    r"(?i)\bel alarmante peligro\b",
    r"(?i)\bel peligro oculto\b",
    r"(?i)\bla ciencia ignora\b",
    r"(?i)\bestudio alternativo\b",
    r"(?i)\bsilencio institucional\b",
    r"(?i)\blo que no quieren que sepas\b",
    r"(?i)\bsecreto revelado\b"
]

# Patrones para detectar validación o respaldo científico real
PATRONES_CIENTIFICOS = [
    r"(?i)\bcientíficos de la universidad de\b",
    r"(?i)\buniversidad de harvard\b",
    r"(?i)\bmanipulación genética controlada\b",
    r"(?i)\blaboratorios oficiales\b",
    r"(?i)\bbiblioteca nacional de medicina\b",
    r"(?i)\bpublicado en la revista\b"
]

def analizar_texto_regex(texto):
    """Cuenta cuántas frases alarmistas y cuántas científicas hay en el texto."""
    conteo_alarmista = 0
    conteo_cientifico = 0
    
    # Buscamos coincidencias de alarmismo
    for patron in PATRONES_ALARMISTAS:
        if re.search(patron, texto):
            conteo_alarmista += 1
            
    # Buscamos coincidencias científicas
    for patron in PATRONES_CIENTIFICOS:
        if re.search(patron, texto):
            conteo_cientifico += 1
            
    return conteo_alarmista, conteo_cientifico