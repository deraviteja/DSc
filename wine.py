import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
import seaborn as sb


def gap():
    print "\n"
    print "    =======================================      "
    print "-------------------------------------------------"
    return "\n"


data = pd.read_csv('wine.data.txt', sep=',',na_values=['#','@'])# , header=None)

info = data.describe()

print gap(), info

assert (len(info.loc['count'].unique()) is 1)
# assert if there are no missing values

#   print type(data['Class'].unique()) returns

assert (len(data['Class'].unique()) is 3)
# assert that there are only 3 classes

print gap(), data.Class.value_counts()

output_data = data['Class'].values

column_names = [x for x in data.columns.values if x is not 'Class']

print gap(), type(data.columns)

print gap(), data.dtypes

print gap(), column_names

input_data = data[column_names].values

#   print gap(), input_data[0:4,0:4]

#   data[column_names].hist()

#   print gap(), data[' Flavanoids'].describe()

#   testing cross validation

from sklearn.model_selection import train_test_split as tst
from sklearn.model_selection import StratifiedKFold

X_train, X_test, Y_train, Y_test = tst(input_data,output_data,test_size=0.1)

print gap(), np.unique(Y_train,return_counts=True)

print gap(), np.unique(Y_test,return_counts=True)

X_train, X_test, Y_train, Y_test = tst(input_data,output_data,test_size=0.25,stratify=output_data)

print gap(), np.unique(Y_train,return_counts=True)

print gap(), np.unique(Y_test,return_counts=True)

from sklearn.tree import DecisionTreeClassifier

dclassifier = DecisionTreeClassifier(max_depth=2)

print gap(), dclassifier.fit(X_train, Y_train)

print gap(), dclassifier.score(X_test,Y_test)

from sklearn.model_selection import cross_val_score

dclassifier = DecisionTreeClassifier(max_depth=2)

cross_validator = StratifiedKFold(n_splits=20, shuffle=True)

cv_score = cross_val_score(dclassifier,input_data,output_data,cv=cross_validator)

#   sb.distplot(cv_scores)

import matplotlib.pylab as plt

#   plt.hist(cv_score)

#   plt.ylabel('CV_Score')

#   plt.show()


from sklearn.linear_model import LogisticRegression

LR = LogisticRegression()

cv_score = cross_val_score(LR,input_data,output_data,cv=cross_validator)

print cv_score

plt.hist(cv_score)

plt.ylabel('CV_Score')

plt.show()