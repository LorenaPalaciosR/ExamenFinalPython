import pandas as pd
import matplotlib.pyplot as plt

def costo_mas_bajo(df_resultado, output_path_bajo='top_10_costo_vida_bajo.png'):
    try:
       
        df = pd.read_csv(df_resultado, delimiter=',', encoding='utf-8', on_bad_lines='skip')

      
        if "Countries" in df.columns and "Cost of living, 2017" in df.columns:
           
            top_10_countries = df.nsmallest(10, "Cost of living, 2017")[["Countries", "Cost of living, 2017"]]
            
            
            plt.figure(figsize=(10, 6))
            plt.barh(top_10_countries["Countries"], top_10_countries["Cost of living, 2017"], color='orange')
            plt.xlabel("Costo de vida (2017)")
            plt.ylabel("Países")
            plt.title("Top 10 países con el costo de vida más bajo (2017)")
            plt.gca().invert_yaxis() 
            
        
            plt.savefig(output_path_bajo)
            plt.show()
            plt.close()
            
            print("El gráfico se ha exportado correctamente como 'top_10_costo_vida.png'.")
            return top_10_countries
        else:
            print("Las columnas necesarias no existen en el DataFrame.")
            return None

    except FileNotFoundError:
        print("El archivo no se encuentra. Por favor, verifica la ruta.")
        return None
    except pd.errors.EmptyDataError:
        print("El archivo está vacío.")
        return None
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return None

