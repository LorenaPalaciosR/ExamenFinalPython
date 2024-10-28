
from scripts.revisiondatos import revision_datos
from scripts.costo_mas_alto import costo_mas_alto
from scripts.costo_mas_bajo import costo_mas_bajo
from scripts.costo_paises_america import costo_vida_america
import pandas as pd

def main():
    
    archivo = "./data/dataset_living.csv"    
    output_path = "./results/10_paises_costo_vida_mas_alto.png"    
    output_path_bajo = "./results/10_paises_costo_vida_mas_bajo.png"
    output_path_america = "./results/costo_vida_paises_america.png"
    
  
    resultados = revision_datos(archivo)
   
    if resultados is not None:
        print(resultados)  
    else:
        print("No se pudieron obtener los resultados.")
        
        
    resultado_costo_mas_alto = costo_mas_alto(archivo, output_path)
    
    if resultado_costo_mas_alto is not None:
        print("Top 10 países con el costo de vida más alto:")
        print(resultado_costo_mas_alto)
    else:
        print("No se pudo obtener la información de los 10 países con el costo de vida más alto.")
        
    resultado_costo_bajo = costo_mas_bajo(archivo, output_path_bajo)
      
    if resultado_costo_bajo is not None:
        print("Top 10 países con el costo de vida más bajo:")
        print(resultado_costo_bajo)
    else:
        print("No se pudo obtener la información de los 10 países con el costo de vida más bajo.")
        
        
    resultado_america = costo_vida_america(archivo, output_path_america)
    
    if resultado_america is not None:
        print("Países de América y su costo de vida:")
        print(resultado_america)
    else:
        print("No se pudo obtener la información de los países de América.")



if __name__ == "__main__":
    main()