import numpy as np
import pandas as pd

names = ['age','workclass','fnlwgt','education','education-num','marital-status',
         'occupation','relationship','race','sex','capital-gain','capital-loss',
         'hours-per-week','native-country','income']

data = pd.read_csv('../data/adult.data.txt' ,header=None, names=names)
# print(data.head(1))
'''
   age   workclass  fnlwgt  ... hours-per-week  native-country  income
0   39   State-gov   77516  ...             40   United-States   <=50K
'''

# 원본 데이터에는 15개의 특성(feature)이 있었다,
# 이중에 연봉을 결정하는데 의미 있을 것 같은 7개로 특성을 추림.
data = data[['age','workclass','education','sex','hours-per-week','occupation','income']]
print(data.head(1))
'''
   age   workclass   education    sex  hours-per-week     occupation  income
0   39   State-gov   Bachelors   Male              40   Adm-clerical   <=50K
'''

