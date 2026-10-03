import os
import json

def extraer_dato_exacto(nombre_archivo, campo_solicitado, directorio="workspace/01_insumos"):
    """
    Abre un documento específico y extrae un campo o nodo exacto.
    Ideal para responder preguntas puntuales sobre proyectos pasados.
    """
    ruta_completa = os.path.join(directorio, nombre_archivo)
    
    # Validar que el archivo exista
    if not os.path.exists(ruta_completa):
        return f"Error: El archivo {nombre_archivo} no se encuentra en el repositorio histórico."
        
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            
            # Buscar el campo solicitado (ej. "presupuesto", "arquitectura", "metodologia")
            # Se convierte a minúsculas para evitar errores de tipeo
            campo_limpio = campo_solicitado.lower().strip()
            
            if campo_limpio in datos:
                return json.dumps({
                    "archivo": nombre_archivo,
                    "campo": campo_solicitado,
                    "valor": datos[campo_limpio]
                }, indent=4, ensure_ascii=False)
            else:
                return f"El campo '{campo_solicitado}' no existe dentro del documento {nombre_archivo}."
                
    except json.JSONDecodeError:
        return f"Error: El archivo {nombre_archivo} no tiene un formato estructurado válido."
    except Exception as e:
        return f"Error inesperado al leer el documento: {str(e)}"