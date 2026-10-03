import os
import json

def buscar_historicos(tematica, directorio="workspace/01_insumos"):
    """
    Escanea el directorio de insumos buscando proyectos históricos relacionados con una temática.
    Simula una búsqueda semántica (RAG) basándose en palabras clave.
    """
    resultados = []
    
    # Validar si el directorio existe
    if not os.path.exists(directorio):
        return f"Error: El directorio {directorio} no existe en el workspace."

    # Escanear archivos en la carpeta
    for nombre_archivo in os.listdir(directorio):
        if nombre_archivo.endswith(".json"):
            ruta_completa = os.path.join(directorio, nombre_archivo)
            
            try:
                with open(ruta_completa, 'r', encoding='utf-8') as archivo:
                    datos = json.load(archivo)
                    
                    # Buscar coincidencia en el título o descripción del proyecto simulado
                    titulo = datos.get("titulo_proyecto", "").lower()
                    descripcion = datos.get("descripcion", "").lower()
                    
                    if tematica.lower() in titulo or tematica.lower() in descripcion:
                        # Extraer solo el resumen para no sobrecargar el prompt del agente
                        resultados.append({
                            "archivo_fuente": nombre_archivo,
                            "titulo": datos.get("titulo_proyecto"),
                            "resumen": datos.get("resumen_ejecutivo", "Sin resumen"),
                            "lecciones_aprendidas": datos.get("lecciones_aprendidas", "N/A")
                        })
            except Exception as e:
                print(f"Error leyendo {nombre_archivo}: {e}")
                
    if not resultados:
        return f"No se encontraron proyectos históricos relacionados con la temática: '{tematica}'."
        
    return json.dumps(resultados, indent=4, ensure_ascii=False)