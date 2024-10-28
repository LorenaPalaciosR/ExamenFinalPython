import pandas as pd
import matplotlib.pyplot as plt
import os

def revision_datos(df_resultado):
    try:
        df = pd.read_csv(df_resultado, delimiter=',', encoding='utf-8', on_bad_lines='skip')
        
        num_filas = df.shape[0]
        num_columnas = df.shape[1]
        
        promedio_costo = df["Cost of living, 2017"].mean()
        
        resultados = {}
        if "Countries" in df.columns and "Cost of living, 2017" in df.columns:
            costo_max = df["Cost of living, 2017"].idxmax()
            costo_min = df["Cost of living, 2017"].idxmin()
            
            pais_caro = df.loc[costo_max, "Countries"]
            costo_vida_alto = df.loc[costo_max, "Cost of living, 2017"]
            
            pais_barato = df.loc[costo_min, "Countries"]
            costo_vida_bajo = df.loc[costo_min, "Cost of living, 2017"]

            costo_peru = df[df["Countries"] == "Peru"]["Cost of living, 2017"].values[0] if not df[df["Countries"] == "Peru"]["Cost of living, 2017"].empty else "No disponible"
            
            if "Global rank" in df.columns:
                ranking_peru = df[df["Countries"] == "Peru"]["Global rank"].values[0] if not df[df["Countries"] == "Peru"]["Global rank"].empty else "No disponible"
            else:
                ranking_peru = "No disponible"
            
            resultados = {
                "Número de Filas": num_filas,
                "Número de Columnas": num_columnas,
                "Costo de vida promedio": round(promedio_costo, 2),
                "País con costo de vida más alto": pais_caro,
                "País con costo de vida más bajo": pais_barato,
                "Costo de vida en Perú": costo_peru,
                "Ranking Perú": ranking_peru
            }
        
        return resultados

    except FileNotFoundError:
        print("El archivo no se encuentra. Por favor, verifica la ruta.")
        return None
    except pd.errors.EmptyDataError:
        print("El archivo está vacío.")
        return None
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return None

def crear_tabla_grafica(datos, nombre_archivo='tabla_grafica.png', carpeta_resultados='./results'):
    # Crear DataFrame de resultados, asegurando que todo sea de tipo string
    df = pd.DataFrame(list(datos.items()), columns=['Descripción', 'Resultado'])
    df['Resultado'] = df['Resultado'].apply(lambda x: str(x).split('dtype')[0].strip())

    ruta_archivo = os.path.join(carpeta_resultados, nombre_archivo)
    
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_frame_on(False)

    tabla = ax.table(
        cellText=df.values, 
        colLabels=df.columns,
        cellLoc='center', 
        loc='center',
        colColours=['#b3cde3', '#b3cde3']
    )

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1.2, 1.2)

    for (i, j), cell in tabla.get_celld().items():
        cell.set_edgecolor('#cccccc')
        cell.set_text_props(ha='center', va='center')
        if i == 0:
            cell.set_fontsize(12)
            cell.set_text_props(weight='bold', color='black')
    
    # Guardar la imagen de la tabla
    plt.savefig(ruta_archivo, bbox_inches='tight', dpi=300)
    plt.show()
    plt.close()

    print(f"Tabla guardada como '{ruta_archivo}'")
