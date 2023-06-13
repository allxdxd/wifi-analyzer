from NetworksAPI import Networks
from datetime import datetime

print('Realizando captura de redes...')
# initialize class
nt = Networks()

print('Convirtiendo en Dataframe...\n\n')
# create a dataframe
netDataframe = nt.convert_Dataframe()

print('Mostrando resultados\n\n')
# showing
date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(date)
print(netDataframe[['SSID','BSSID','Authentication', 'Encryption', 'dBm','Channel']])

# others things
print('\n\nEliga el número de una opción: ')
print("""
1: Exportar como archivo Excel
2: Exportar como archivo CSV

# Cualquier otra tecla cerrará el proceso
""")
try: 
    op = int(input('\nOpción: '))
    name = f'capture.{datetime.now().strftime("%d.%m.%Y.%H.%M")}'
    if op == 1:
        print('Convirtiendo a .xlsx')
        netDataframe.to_excel(f"{name}.xlsx")
    if op == 2:
        print('Convirtiendo a .csv')
        netDataframe.to_csv(f"./{name}.csv")
except:
    print('Cerrando ...')

