import subprocess
import pandas as pd


class Networks():

    def __init__(self):
        self.capture()

    def capture(self):
        # this is the script to execute
        self.__script_str = """ 
        (netsh wlan show network  mode=bssid |  Select-Object -Skip  3).Trim()  | Out-String
        """

        # execute the script and storage the output
        self.__output = subprocess.check_output(
            ['powershell', '-Command', self.__script_str], input=None, stderr=subprocess.STDOUT)
        self.__outputStr = self.__output.decode('utf-8', 'ignore')

        # format output
        self.__outputStr = self.__outputStr.split('\r\n')
        self.__netList = list(filter(None, self.__outputStr))
        self.nets = []
        for i in range(0, len(self.__netList), 10):
            self.nets.append(self.__netList[i:(i+10)])

    def howmanyNets(self):
        return len(self.__netList) // 10

    def getNetworks(self):
        # make a diccionary with networks
        self.networks = []
        self.__count = 0
        for net in self.nets:
            self.networks.append({
                'SSID': net[0].replace(f'SSID {self.__count+1} : ', ''),
                'Type': net[1].replace('Tipo de red             : ', ''),
                'Authentication': net[2].replace('Autenticacin           : ', ''),
                'Encryption': net[3].replace('Cifrado                 : ', ''),
                'BSSID': net[4].replace('BSSID 1             : ', ''),
                'Signal': net[5].replace('Seal              : ', ''),
                'dBm': self.convert2dBm(int(net[5].replace('Seal              : ', '').replace('%', ''))),
                'Radio': net[6].replace('Tipo de radio      : ', ''),
                'Channel': net[7].replace('Canal              : ', ''),
                'Basic_rates_(Mbps)': net[8].replace('Velocidades bsicas (Mbps): ', ''),
                'Other_rates _(Mbps)': net[9].replace('Otras velocidades (Mbps): ', '')

            })
            self.__count += 1
        return self.networks

    def convert2dBm(self, percent):
        self.dBm = (percent / 2) - 100
        return self.dBm

    def convert(self):
        try:
            percent = int(input('Digite la señal: '))
            dbm = self.convert2dBm(percent)
            print('\n\nSeñal en dBm: ', dbm)
        except:
            print('\n\nAlgún error ha ocurrido')
            self.convert()

    def convert_Dataframe(self, _orient='columns'):
        # create a dict for convert in dataframe
        self.__nets = self.getNetworks()
        self.__netkeys = list(self.__nets[0].keys())
        self.__dataNets = {}
        for key in self.__netkeys:
            self.__dataNets[key] = []
            for net in self.__nets:
                self.__dataNets[key].append(net[key])
        # create dataframe
        self.netDataframe = pd.DataFrame.from_dict(
            self.__dataNets, orient=_orient)
        return self.netDataframe
