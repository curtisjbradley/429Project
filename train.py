import pandas as pd
from ctgan import CTGAN
from sdv.metadata import SingleTableMetadata
from sdv.evaluation.single_table import evaluate_quality
import sys
from datetime import datetime as time

data = pd.read_csv(sys.argv[1])

print("Data read")

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

tgan.save(str(time.now()) + ".pkl")
