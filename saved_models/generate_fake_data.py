from ctgan import CTGAN

CTGAN.load('90.pkl').sample(10000).to_csv('90.csv', index=False)
