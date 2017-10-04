import numpy as np
import pandas as pd

user_data = pd.read_csv('u.user.txt',sep='|')

user_data = user_data.set_index('user_id')

print user_data[:25]

print user_data.columns.size

print user_data.occupation

print len(user_data.occupation.unique())

print user_data.occupation.unique()

k = user_data.occupation

print k

k.loc[5] = "nothing"

print k[:5]

print user_data[:5]