import KitNET.KitNET as kit
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

model = "10"

packet_limit = np.inf #the number of packets to process
# KitNET params:

features = 41
maxAE = 10 #maximum size for any autoencoder in the ensemble layer
FMgrace = 5000 #the number of instances taken to learn the feature mapping (the ensemble's architecture)

data = pd.read_csv("benign_dataset.csv").to_numpy()

K = kit.KitNET(features,maxAE, FMgrace, 50000)

i = 0
# Here we process (train/execute) each individual packet.
# In this way, each observation is discarded after performing process() method.
for i in range(0, data.shape[0]):
    K.process(data[i])
    pass
print("Done")

df = pd.read_csv("saved_models/10.csv")
data = df.copy()
categorical_columns = ['protocol_type', 'service', 'flag']
le = LabelEncoder()

for column in categorical_columns:
     data[column] = le.fit_transform(df[column])
data.drop(['class', 'detection_difficulty'], axis='columns', inplace=True)

predictions = []
for r in data.to_numpy():
    predictions.append(K.process(r))

df['RMSE'] = predictions
df.to_csv("saved_models/10RMSEd.csv", index=False)