import requests
import io
import zipfile
def get_rnc():
    # URL del archivo ZIP
    url = "https://www.dgii.gov.do/app/WebApps/Consultas/RNC/DGII_RNC.zip"

    # Hacer una solicitud GET para obtener el archivo ZIP
    print("steps")
    response = requests.get(url, verify=False)
    text = ''
    print("Step 1")
    # Verificar que la solicitud fue exitosa
    if response.status_code == 200:
        print("Step 2")
        # Convertir el contenido en un archivo en memoria
        file_bytes = io.BytesIO(response.content)
        print("Step 3")
        # Abrir el archivo ZIP desde la memoria
        with zipfile.ZipFile(file_bytes, 'r') as zip_ref:
            # Listar los archivos en el ZIP
            print(zip_ref.namelist())

            # Leer un archivo específico dentro del ZIP
            print("Step 5")
            with zip_ref.open('TMP/DGII_RNC.TXT') as file:
                contenido = file.read()
#                print(contenido.decode('latin-1'))  # Decodificación en latin-1
                text = contenido.decode('latin-1')
                return text.split("\n")
    else:
        print("No se pudo descargar el archivo ZIP")
