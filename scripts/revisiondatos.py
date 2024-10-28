import pandas as pd
from tabulate import tabulate

def revision_datos(df_resultado):
    try:
        df = pd.read_csv(df_resultado, delimiter=',', encoding='utf-8', on_bad_lines='skip')
        
        num_filas = int(df.shape[0])
        num_columnas = int(df.shape[1])
        
        promedio_costo = float(df["Cost of living, 2017"].mean())
        
        if "Countries" in df.columns and "Cost of living, 2017" in df.columns:
            costo_max = df["Cost of living, 2017"].idxmax()
            costo_min = df["Cost of living, 2017"].idxmin()
            
            pais_caro = df.loc[costo_max, "Countries"]
            costo_vida_alto = df.loc[costo_max, "Cost of living, 2017"]
            
            pais_barato = df.loc[costo_min, "Countries"]
            costo_vida_bajo = df.loc[costo_min, "Cost of living, 2017"]
            
            costo_peru = df[df["Countries"] == "Peru"]["Cost of living, 2017"].values[0] if not df[df["Countries"] == "Peru"]["Cost of living, 2017"].empty else "No disponible"
            ranking_peru = df[df["Countries"] == "Peru"]["Global rank"].values[0] if not df[df["Countries"] == "Peru"]["Global rank"].empty else "No disponible"
            
            resumen_resultados = pd.DataFrame({
                'Descripción': ["Número de Filas", "Número de Columnas", "Costo de vida promedio", 
                                "País con costo de vida más alto", "País con costo de vida más bajo", 
                                "Costo de vida en Perú", "Ranking Perú"],
                'Resultado': [num_filas, num_columnas, round(promedio_costo, 2), 
                              pais_caro, pais_barato, costo_peru, ranking_peru]
            })
            
     
            print("\nTabla de Resultados:")
            print(tabulate(resumen_resultados, headers='keys', tablefmt='fancy_grid', showindex=False))
            
            return resumen_resultados

    except FileNotFoundError:
        print("El archivo no se encuentra. Por favor, verifica la ruta.")
        return None
    except pd.errors.EmptyDataError:
        print("El archivo está vacío.")
        return None
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return None

df_resultado = "./data/dataset_living.csv"
