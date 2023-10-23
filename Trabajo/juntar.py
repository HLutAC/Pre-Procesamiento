import pandas as pd
import glob

ruta_archivos = r'C:\Users\hansl\Data_Mining\Trabajo\*.csv'

archivos = glob.glob(ruta_archivos)

combinados = pd.DataFrame()

columnas = ['TARIFA', 'FASE', 'CODIGO_CIU', 'POTENCIA_CONTRATADA','UBIGEO', 'DEPARTAMENTO', 'PROVINCIA', 'DISTRITO', 'LOCALIDAD']

for archivo in archivos:
    datos_mes = pd.read_csv(archivo, sep=';', encoding='ISO-8859-1')
    
    if 'PERIODO_FACTURACION' in datos_mes.columns:
        mes_y_anio = str(datos_mes['PERIODO_FACTURACION'].iloc[0])

        datos_mes = datos_mes.drop_duplicates(subset='UUID')
        
        combinados = pd.concat([combinados, datos_mes.set_index('UUID')[['CONSUMO_KW', 'MONTO_SOLES']].add_suffix('_' + mes_y_anio)], axis=1)

columnas_df = datos_mes[['UUID'] + columnas].drop_duplicates(subset='UUID').set_index('UUID')
combinados = pd.concat([combinados, columnas_df], axis=1)

# Reinicia el índice para que 'UUID' vuelva a ser una columna
combinados = combinados.reset_index()

ruta_salida = r'C:\Users\hansl\Data_Mining\Trabajo\combinados.csv'
combinados.to_csv(ruta_salida, index=False, sep=';')

print('Listo')

