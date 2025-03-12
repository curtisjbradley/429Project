import pandas as pd
from ctgan import CTGAN
from sdv.metadata import SingleTableMetadata
from sdv.evaluation.single_table import evaluate_quality
import sys
from datetime import datetime as time
from os import chdir

print("reading")
print(sys.argv[1])
data = pd.read_csv(sys.argv[1])

print(data)

tgan = CTGAN(epochs=200)
discrete_columns = [
    'protocol_type',
    'service',
    'flag',
    'class'
]

print("training")
tgan.fit(data, discrete_columns)
print("Finished training")


chdir(sys.argv[2])
tgan.save(sys.argv[3] +"Trained" + str(time.now()) + ".pkl")
