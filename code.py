import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import os


os.chdir('C://Users//HP//Desktop//dupas//')
data = pd.io.stata.read_stata('main_dataset.dta')

pd.set_option('display.max_columns', None)
print(data)

    # to check wheter cfw_id is the retailer id
print(data['cfw_id'].describe())
print(data['cfw_id'].unique())
    # to check avg time to redeem of phase 1 across groups that redeemed at the same retailer
print(data.groupby('cfw_id')['timetoredeem1'].mean())


data_1 = data.loc[:, ['hhid', 'Long_home', 'Lat_home','timetoredeem1', 'cfw_id', 'purchasedwg']]
    # to check how many na's
print("NA COUNT",data_1.isna().sum())
    # to check mean of 'purchasedwg' of the non missing observations (264/1200)
print("PURCHASEDWG",data['purchasedwg'].describe())
    # to check how the non missing observations of 'timetoredeem' (575/1200) are distributed across vilages
data_1.dropna(axis=0,how='any',subset=['hhid', 'Long_home', 'Lat_home'],inplace=True)
for cfw_id, group in data_1.groupby('cfw_id'):
    plt.scatter(group['Long_home'], group['Lat_home'], label=f'retailer id: {cfw_id}')
data_1.dropna(axis=0,how='any',subset=['hhid', 'Long_home', 'Lat_home','timetoredeem1'],inplace=True) 
plt.scatter(data_1['Long_home'], data_1['Lat_home'], c='black',label='available timetoredeem1', s=10) 
plt.legend() 
plt.show()










