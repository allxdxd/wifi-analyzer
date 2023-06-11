import subprocess
from signal_convert import convert2dBm

class Networks():

    def __init__(self):
        # this is the script to execute
        self.__script_str = """ 
        (netsh wlan show network  mode=bssid |  Select-Object -Skip  3).Trim()  | Out-String
        """

        # execute the script and storage the output
        self.__output = subprocess.check_output(['powershell','-Command', self.__script_str], input=None, stderr=subprocess.STDOUT)
        self.__outputStr = self.__output.decode('utf-8','ignore')

        # format output
        self.__outputStr = self.__outputStr.split('\r\n')
        self.__netList = list(filter(None, self.__outputStr))
        self.nets = []
        for i in range(0, len(self.__netList), 10):
            self.nets.append(self.__netList[i:(i+10)])
        
    def howmanyNets(self):
        return len(self.__netList) // 10

    def show(self):
        # make a diccionary with networks
        self.networks = []
        self.__count = 0
        for net in self.nets:
            self.networks.append({
                'SSID' : net[0].replace(f'SSID {self.__count+1} : ',''),
                'Type' : net[1].replace('Tipo de red             : ',''),
                'Authentication': net[2].replace('Autenticacin           : ', ''),
                'Encryption' : net[3].replace('Cifrado                 : ', ''),
                'BSSID' : net[4].replace('BSSID 1             : ', ''),
                'Signal' : net[5].replace('Seal              : ',''),
                'dBm' : convert2dBm(int(net[5].replace('Seal              : ','').replace('%',''))),
                'Radio': net[6].replace('Tipo de radio      : ',''),
                'Channel' : net[7].replace('Canal              : ','')
            })
            print(self.networks[self.__count])
            self.__count += 1





networks = Networks()

print(networks.show())
