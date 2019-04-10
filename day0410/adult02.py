import numpy as np
import pandas as pd

names = ['age','workclass','fnlwgt','education','education-num','marital-status',
         'occupation','relationship','race','sex','capital-gain','capital-loss',
         'hours-per-week','native-country','income']

data = pd.read_csv('../data/adult.data.txt' ,header=None, names=names)

data = data[['age','workclass','education','sex','hours-per-week','occupation','income']]

# 직업분류의 종류는 모두 몇가지 인지 출력
workkind = data['workclass'].unique()
print(workkind)
print(len(workkind))

# 직업의 종류는 모두 몇가지 인지 출력
jobkind = data['occupation'].unique()
print(jobkind)
print(len(jobkind))

# 학력의 종류는 모두 몇가지 인지 출력
educationkind = data['education'].unique()
print(educationkind)
print(len(educationkind))

# 성별의 종류는 모두 몇가지 인지 출력
sexkind = data['sex'].unique()
print(sexkind)
print(len(sexkind))

# 수익의 종류는 모두 몇가지 인지 출력
incomekind = data['income'].unique()
print(incomekind)
print(len(incomekind))
