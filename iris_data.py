import numpy as np
import pandas as pd


def gap():
    print "\n"
    print "============================================="
    print "---------------------------------------------"
    print "============================================="
    return "\n"


data = pd.read_csv('iris-data.csv',na_values="NA")

# data must be containing only 5 'classes' of data.

classes = {'Iris-setossa': 'Iris-setosa',
           'versicolor': 'Iris-versicolor',
           'Iris-setosa': 'Iris-setosa',
           'Iris-versicolor': 'Iris-versicolor',
           'Iris-virginica': 'Iris-virginica'}

data['class'] = data['class'].apply(lambda x: classes[x])

print gap(), data['class'].value_counts()

print gap(), data.describe()

# print gap(), data.dtypes
#
# sepal_mean = data.sepal_length_cm.mean()
#
# print gap(), sepal_mean
#
# k = data.sepal_length_cm.select(lambda x: data.sepal_length_cm.iloc[x] >= sepal_mean)
#
# print gap(), k
#
# data.sepal_length_cm.select(lambda x: data.sepal_length_cm.iloc[x] >= sepal_mean)['sepal_length_cm'] = 'kidding'
#
# print gap(), data.sepal_length_cm.select(lambda x: data.sepal_length_cm.iloc[x] is 'kidding')
#
# print gap(), data.dtypes

print gap(), data.describe()

#   print data.loc[(data['class'] == 'Iris-setosa') & (data['sepal_length_cm'] <= 2.5)]

data = data.loc[(data['class'] != 'Iris-setosa') | (data['sepal_length_cm'] >= 2.5)]

print gap(), data.describe()

#   data = data.loc[data['petal_width_cm'] is not ]

print gap(), data.loc[(data['class'] == 'Iris-versicolor') & (data['sepal_length_cm'] < 1.0)]

data.loc[(data['class'] == 'Iris-versicolor') & (data['sepal_length_cm'] < 1.0), 'sepal_length_cm'] *= 100

#   print gap(), data.loc[(data['class'] == 'Iris-versicolor') & (data['sepal_length_cm'] < 1.0)]

print gap(), data.loc[(data['class'] == 'Iris-versicolor') & (data['sepal_length_cm'] < 1.0)].isnull()

print gap(), data.loc[data['petal_width_cm'].isnull()]

Iris_setosa_petal_mean = data.loc[data['class'] == 'Iris-setosa','petal_width_cm'].mean()

print gap(), Iris_setosa_petal_mean

data.loc[(data['petal_width_cm'].isnull()) & (data['class'] == 'Iris-setosa'), 'petal_width_cm'] = Iris_setosa_petal_mean

# data = data.dropna()

# data.drop('sepal_length_cm',axis=1)
#
# print gap(), data.describe()
#
# data = data.drop('sepal_length_cm',axis=1)
#
# print gap(), data.describe()
#
# data = data.drop(4)
#
# print gap(), data.describe()


