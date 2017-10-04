import numpy as np
import pandas as pd

chip = pd.read_csv('chipotle.tsv',sep='\t',header=0)

#   print chip.describe()

print chip.info()
print "------------------------------------------"
print "------------------------------------------"
print chip.count()
print "------------------------------------------"
print "------------------------------------------"
print "number of columns are : ", chip.columns.size
print "number of rows are", chip.shape[0]
print "------------------------------------------"
print "------------------------------------------"

print chip.cummax(axis={0,'quantity'})

#   print chip[:10]
