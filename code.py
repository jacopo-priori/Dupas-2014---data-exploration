import pandas as pd
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

data = pd.io.stata.read_stata('data.dta')  # to import Dupas data

# VISUALIZATION TO SEE WHERE VILLAGES ARE LOCATED

cords = data.loc[:, 'Long_home':'Lat_home']
cords.dropna(axis=0,how='any',subset=None,inplace=True)  # dropping 26/1200
fig = px.scatter_mapbox(cords, lat="Lat_home", lon="Long_home")
fig.update_layout(mapbox_style="open-street-map")
fig.show()

# EXPLORATION TO CHECK FOR NON RANDOMIZATION DUE TO (ASSUMED) DIFFERENCE TREATMENT TIMING FOR EACH VILLAGE

## EXPLORATION OF VARIABLES

data_1 = data.loc[:, ['hhid', 'Long_home', 'Lat_home', 'purchasednet','timetoredeem1', 'purchasedwg', 'fol1_hanging']]  # there is no variable with voucher delivery day so impossible to check for difference malaria exposure due to season
print(data_1.isna().sum())
# data_1.dropna(axis=0,how='any',subset=None,inplace=False)  # only two villages remain so no point exploring 'timetoredeem1' and 'fol1_hanging'
data_1.dropna(axis=0,how='any',subset=['hhid', 'Long_home', 'Lat_home', 'purchasednet'],inplace=True)  # dropping 26/1200
plt.scatter(data_1['Long_home'], data_1['Lat_home'])  # to check if all villages remained
plt.show()

## CREATION OF CLUSTERS TO THEN GROUP BY VILLAGE (AS THERE IS NO VARIABLE THAT TELLS WHAT VILLAGE)

x = data_1[['Long_home', 'Lat_home']]
kmeans = KMeans(n_clusters=6, random_state=123)  # to create clusters
cluster_labels = kmeans.fit_predict(x)  
plt.scatter(data_1['Long_home'], data_1['Lat_home'], c=cluster_labels)  # to check if clusterisation approximately worked
plt.colorbar(label='cluster_labels')
plt.show()

## CHECK IF PURCHASE RATE VARIES BY VILLAGE 

data_1['village'] = cluster_labels  # to add clusters as a column
print(data_1.describe())  # to check if actually assigned 6 different values for village
print(data_1.groupby('village')['purchasednet'].mean())  # to calculate rates
avg_of_village = data_1.groupby('village')['purchasednet'].mean()
avg_of_village.plot(kind='bar')  # to plot rates
plt.show()
