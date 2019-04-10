import numpy as np
import pandas as pd

names = ['age','workclass','fnlwgt','education','education-num','marital-status',
         'occupation','relationship','race','sex','capital-gain','capital-loss',
         'hours-per-week','native-country','income']

data = pd.read_csv('../data/adult.data.txt' ,header=None, names=names)

data = data[['age','workclass','education','sex','hours-per-week','occupation','income']]

workkind = data['workclass'].unique()