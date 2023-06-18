from lswifi_Mod.app import run
from argparse import Namespace

# set the args
argsToRun = Namespace(scans=None, time=None,
          interval=None, ies=None,
          sensitivity=-82, all=True,
          g=False, a=False, six=False,
          include=None, exclude=None,
          bssid=None, apnames=True,
          qbss=False, tpc=False,
          pmf=False, period=False,
          uptime=False, rnr=False,
          width=None, ethers=False,
          append=None, display_ethers=False,
          data_location=False, get_current_ap=False,
          get_current_channel=False, raw=False,
          get_interface_info=False, list_interfaces=False,
          supported=False, json='test.json',
          json_indent=4, csv=None,
          export=None, bytefile=None,
          bytes=None, event_watcher=False,
          debug=20)



# run lswifi with the args
json = run(argsToRun).jsonAtrr

print(json)
