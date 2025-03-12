import pandas as pd
from ctgan import CTGAN
import sys
from datetime import datetime as time
from os import chdir

data = pd.read_csv(sys.argv[1])

tgan = CTGAN(epochs=100, verbose=True)
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
