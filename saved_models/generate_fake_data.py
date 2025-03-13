from ctgan import CTGAN
import sys

CTGAN.load(sys.argv[1] + '.pkl').sample(10000).to_csv(sys.argv[1] + '.csv', index=False)
