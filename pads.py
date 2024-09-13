import pandas as pd
import requests
import zipfile
import io

# URL del archivo ZIP remoto
url = "https://www.dgii.gov.do/app/WebApps/Consultas/RNC/DGII_RNC.zip"

# Descargar el archivo ZIP en memoria (sin guardar en disco)
response = requests.get(url, verify=False)

# Abre el archivo ZIP en memoria
with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
    # Listar los archivos dentro del ZIP
    print(zip_file.namelist())  # Verifica los archivos dentro del ZIP
    
    # Abrir el archivo TXT dentro del ZIP
    with zip_file.open('TMP/DGII_RNC.TXT') as txt_file:
        # Leer el archivo TXT (ajusta el delimitador según el formato)
        df = pd.read_csv(txt_file, delimiter='|', encoding='latin1', header=None)  # Ejemplo para un archivo TSV (delimitado por tabulaciones
        
# Mostrar las primeras filas del DataFrame
print(df.head())
