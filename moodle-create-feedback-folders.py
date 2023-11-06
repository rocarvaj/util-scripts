import pandas as pd
import os

lista = pd.read_csv("Calificaciones-3767-V-MGT350-5-2-2023-Archivo original Prueba 1-384983.csv")

print(lista[['Identificador', 'Nombre completo']])


parent_dir = "/Users/rocarvaj/Downloads/feedback-files"


for i in range(len(lista)):
    id_number = lista.loc[i, 'Identificador'].split("Participante")[1]
    name = lista.loc[i, 'Nombre completo']
    directory = f"{name}_{id_number}_assignsubmission_file_"

    path = os.path.join(parent_dir, directory)

    print(path)
    os.mkdir(path)
