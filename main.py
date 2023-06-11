from NetworksAPI import Networks
import pandas as pd
import matplotlib.pyplot as plt

# initialize class
nt = Networks()
# create a dataframe
netDataframe = nt.convert_Dataframe()

print(netDataframe)
