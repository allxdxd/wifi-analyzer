def convert2dBm(percent):
    dBm = (percent / 2) - 100
    return dBm

def convert():
    try:
        percent = int(input('Digite la señal: '))
        dbm = convert2dBm(percent)
        print('\n\nSeñal en dBm: ', dbm)
    except:
        print('\n\nAlgún error ha ocurrido')
        convert()
    
