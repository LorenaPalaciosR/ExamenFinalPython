import pandas as pd
import matplotlib.pyplot as plt

def costo_vida_america(df_resultado, output_path_america='costo_vida_paises_america.png'):
    try:
     
        df = pd.read_csv(df_resultado, delimiter=',', encoding='utf-8', on_bad_lines='skip')

        
        if "Countries" in df.columns and "Continent" in df.columns and "Cost of living, 2017" in df.columns:
         
            america_df = df[df["Continent"].str.contains("America", case=False, na=False)]
                 
         
          
            plt.figure(figsize=(12, 8))
            plt.barh(america_df["Countries"], america_df["Cost of living, 2017"], color='lightblue')
            plt.xlabel("Costo de vida (2017)")
            plt.ylabel("Países")
            plt.title("Costo de vida en los países de América (2017)")
            plt.gca().invert_yaxis()  
            
     
            plt.savefig(output_path_america)
            plt.show()
            plt.close()
            
            print(f"El gráfico se ha exportado correctamente como 'costo_vida_paises_america.png'.")
            return america_df[["Countries", "Cost of living, 2017"]]
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