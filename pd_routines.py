#   editing examples

import numpy as np
import sklearn as sk
import pandas as pd


def gap():
    print "\n"
    print "-----------------------===------------------------------"
    print "-----------------------===------------------------------"
    return "\n"


sample = pd.read_csv('train.csv',sep=',')

#   sample.loc[indexer,column]
#   indexer can be bool function

print sample.Survived.value_counts(), gap()

sample.loc[sample['Survived']==1,'Survived'] = 2

print sample.Survived.value_counts(), gap()

print sample.dtypes, gap()

print sample.index, gap()

sample.loc[0,'Survived'] = 4

print sample[sample['Survived'] > 3], gap()

sample = sample.set_index('PassengerId')

print sample.index, gap()

sample.loc[1, 'Survived'] = 10

print sample.iloc[0], gap()

# ===================== for editing information

#   'iloc' uses int indexing from 0 to len-1

# series select returns a copy

# to edit use loc, use indexer using a callable function or a bool function

# also use apply to edit a series(i.e. a column in the data frame)

#

# ====================== for deleting information

# use dropna to drop NaN values and the corresponding rows

# assign to self the index if function(true) --> row deletion

# data.drop(row_index) or data.drop(col_label,axis=1) --> col deletion


