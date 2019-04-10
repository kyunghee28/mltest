import numpy as np
import pandas as pd

names = ['age','workclass','fnlwgt','education','education-num','marital-status',
         'occupation','relationship','race','sex','capital-gain','capital-loss',
         'hours-per-week','native-country','income']

data = pd.read_csv('../data/adult.data.txt' ,header=None, names=names)

data = data[['age','workclass','education','sex','hours-per-week','occupation','income']]

workkind = data['workclass'].unique()
print(workkind)
print(len(workkind))

jobkind = data['occupation'].unique()
print(jobkind)
print(len(jobkind))

educationkind = data['education'].unique()
print(educationkind)
print(len(educationkind))

sexkind = data['sex'].unique()
print(sexkind)
print(len(sexkind))

incomekind = data['income'].unique()
print(incomekind)
print(len(incomekind))
