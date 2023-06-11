from NetworksAPI import Networks
import pandas as pd

# initialize class
nt = Networks()

# create a dataframe
netDataframe = nt.convert_Dataframe()
print(netDataframe)

