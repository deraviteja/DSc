import csv
from enum import Enum
import numpy as np
from sklearn import linear_model
from scipy import linalg

stations = ['C','S','Q']

class Fields(Enum):
    pid = 0
    survived = 1
    pclass = 2
    name = 3
    sex = 4
    age = 5
    sibsp = 6
    parch = 7
    ticket = 8
    fare = 9
    cabin = 10
    embarked = 11


class Data:
    def __init__(self):
        self.info = []
        self.pid = []
        self.sex = []
        self.embarked = []
        self.fare = []
        self.age = []
        self.sibsp = []
        self.parch = []
        self.survived = []
        self.X = []
        self.Y = []

    def add_entry(self, inp):
        self.info.append(inp)

    def transform_data(self):
        for row in self.info:

            if row[Fields.sex.value] == "male":
                row[Fields.sex.value] = 1
            elif row[Fields.sex.value] == "female":
                row[Fields.sex.value] = 2
            else:
                print row[Fields.pid.value]
                continue

            if row[Fields.embarked.value] in stations:
                row[Fields.embarked.value] = stations.index(row[Fields.embarked.value])
            else:
                print row[Fields.pid.value]
                continue

            try:
                row[Fields.pid.value] = int(row[Fields.pid.value])
                row[Fields.pclass.value] = int(row[Fields.pclass.value])
                row[Fields.age.value] = float(row[Fields.age.value])
                row[Fields.sibsp.value] = int(row[Fields.sibsp.value])
                row[Fields.parch.value] = int(row[Fields.parch.value])
                row[Fields.fare.value] = float(row[Fields.fare.value])
                row[Fields.survived.value] = int(row[Fields.survived.value])

                self.pid.append(row[Fields.pid.value])
                self.sex.append(row[Fields.sex.value])
                self.embarked.append(row[Fields.embarked.value])
                self.fare.append(row[Fields.fare.value])
                self.age.append(row[Fields.age.value])
                self.sibsp.append(row[Fields.sibsp.value])
                self.parch.append(row[Fields.parch.value])
                self.survived.append(row[Fields.survived.value])

                self.X.append([row[Fields.pid.value],row[Fields.sex.value],
                    row[Fields.embarked.value],row[Fields.fare.value],
                    row[Fields.age.value],row[Fields.sibsp.value],
                    row[Fields.parch.value]])

                self.Y.append(row[Fields.survived.value])

            except:
                continue

    def get_data(self):
            return np.array(self.X), np.array(self.Y)



test = Data()
inp = 0

with open('train.csv','rb') as testfile:
    row_check = csv.reader(testfile,delimiter=',')
    for row in row_check:
        if inp:
            test.add_entry(row)
        else:
            print row
        inp += 1

test.transform_data()

X,Y = test.get_data()


X = [[p,p,p] for p in range(1,10)]

Y = [3,6,1,7,9,2,4,2,1]

tqnq = linear_model.LinearRegression()



tqnq.fit(X,Y)
Y_i = tqnq.predict(X)
Y_r = np.array([round(x) for x in Y_i])

residue = np.dot((Y_r-Y), (Y_r-Y))
print residue