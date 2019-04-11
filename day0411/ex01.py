# 예제) adult.data.txt 를 읽어 들어 연봉을 결정하는 중요한 7개의 속성코드로만 추립니다,.
# 숫자속성을 제외하고 one-hot 인코딩으로 변경하여 생성된 컬럼을 확인해 봅니다.
# 7개의 속성 => 나이, 직업분류, 학력, 성별, 주당일하는 시간, 직업, 수입

import numpy as np
import pandas as pd

names = ['age','workclass','fnlwgt','education','education-num','marital-status',
         'occupation','relationship','race','sex','capital-gain','capital-loss',
         'hours-per-week','native-country','income']

info = pd.read_csv('../data/adult.data.txt' ,header=None, names=names)

data = info[['age','workclass','education','sex','hours-per-week','occupation','income']]

# 위에 데아터프레임을 one-hot을 하면 몇개의 feature가 생성될지 예측
# workclass 의 값의 종류의 수
print(len(data['workclass'].unique()))    # 9
# education 의 값의 종류의 수
print(len(data['education'].unique()))    # 16
# occupation 의 값의 종류의 수
print(len(data['occupation'].unique()))    # 15
# sex 의 값의 종류의 수
print(len(data['sex'].unique()))    # 2
# income 의 값의 종류의 수
print(len(data['income'].unique()))    # 2

print(9+16+15+2+2+2)  # 46  => 숫자(age,hours-per-week)는 바로 출력

new_df = pd.get_dummies(data)
# 원래 가지고 있는 데이터 프레임(7개의 속성(feature)을 one-hot encoding하여 새로운 데이터 프레임을 생성함)
# 새로운 데이터프레임의 feature의 수는 46개
#  => 숫자(age,hours-per-week => 2개)를 제외한 문자속성인 칼럼(9+16+15+2+2 => 총 44개 )은 값의 종류의 수만큼 칼럼이 생성

print(new_df.head(1))
'''
   age  hours-per-week  ...  income_ <=50K  income_ >50K
0   39              40  ...              1             0

[1 rows x 46 columns]
'''

print(new_df.columns)
'''
Index(['age', 'hours-per-week', 'workclass_ ?', 'workclass_ Federal-gov',
       'workclass_ Local-gov', 'workclass_ Never-worked', 'workclass_ Private',
       'workclass_ Self-emp-inc', 'workclass_ Self-emp-not-inc',
       'workclass_ State-gov', 'workclass_ Without-pay', 'education_ 10th',
       'education_ 11th', 'education_ 12th', 'education_ 1st-4th',
       'education_ 5th-6th', 'education_ 7th-8th', 'education_ 9th',
       'education_ Assoc-acdm', 'education_ Assoc-voc', 'education_ Bachelors',
       'education_ Doctorate', 'education_ HS-grad', 'education_ Masters',
       'education_ Preschool', 'education_ Prof-school',
       'education_ Some-college', 'sex_ Female', 'sex_ Male', 'occupation_ ?',
       'occupation_ Adm-clerical', 'occupation_ Armed-Forces',
       'occupation_ Craft-repair', 'occupation_ Exec-managerial',
       'occupation_ Farming-fishing', 'occupation_ Handlers-cleaners',
       'occupation_ Machine-op-inspct', 'occupation_ Other-service',
       'occupation_ Priv-house-serv', 'occupation_ Prof-specialty',
       'occupation_ Protective-serv', 'occupation_ Sales',
       'occupation_ Tech-support', 'occupation_ Transport-moving',
       'income_ <=50K', 'income_ >50K'],
      dtype='object')
'''

# 예쩨) 학습을 시키려면 가지고 있는 데이터로 부터 문제와 답을 분리시키고
# 문제는 x 에 답은 y 에 담으세요
# 뒤에서 부터 2개를 제외한 모든 속성(feature)을 문제로 하고 맨 마지막의 속성은 답으로 만드세요


# fancy indexing
# 2차원 배열인 경우 원하는 데이터를 추출하기 위하여 행열을 분리하여 범위를 지정하여 slicing할 수 있다.
# 데이터프레임[행,열]

# 방법1.
# x = new_df.loc[:,'age':'sex_ Male']
# print(x.columns)
# '''
# Index(['age', 'hours-per-week', 'workclass_ ?', 'workclass_ Federal-gov',
#        'workclass_ Local-gov', 'workclass_ Never-worked', 'workclass_ Private',
#        'workclass_ Self-emp-inc', 'workclass_ Self-emp-not-inc',
#        'workclass_ State-gov', 'workclass_ Without-pay', 'education_ 10th',
#        'education_ 11th', 'education_ 12th', 'education_ 1st-4th',
#        'education_ 5th-6th', 'education_ 7th-8th', 'education_ 9th',
#        'education_ Assoc-acdm', 'education_ Assoc-voc', 'education_ Bachelors',
#        'education_ Doctorate', 'education_ HS-grad', 'education_ Masters',
#        'education_ Preschool', 'education_ Prof-school',
#        'education_ Some-college', 'sex_ Female', 'sex_ Male'],
#       dtype='object')
# '''
#
# y = new_df.loc[:,'income_ >50K']
# print(y.head())
'''
0    0
1    0
2    0
3    0
4    0

Name: income_ >50K, dtype: uint8
'''


# 방법2.

x = new_df.iloc[:,:-2]
print(x.columns)
# Index(['age', 'hours-per-week', 'workclass_ ?', 'workclass_ Federal-gov',
#        'workclass_ Local-gov', 'workclass_ Never-worked', 'workclass_ Private',
#        'workclass_ Self-emp-inc', 'workclass_ Self-emp-not-inc',
#        'workclass_ State-gov', 'workclass_ Without-pay', 'education_ 10th',
#        'education_ 11th', 'education_ 12th', 'education_ 1st-4th',
#        'education_ 5th-6th', 'education_ 7th-8th', 'education_ 9th',
#        'education_ Assoc-acdm', 'education_ Assoc-voc', 'education_ Bachelors',
#        'education_ Doctorate', 'education_ HS-grad', 'education_ Masters',
#        'education_ Preschool', 'education_ Prof-school',
#        'education_ Some-college', 'sex_ Female', 'sex_ Male'],
#       dtype='object')
#

y = new_df.iloc[:,-1]
print(y.head())
'''
0    0
1    0
2    0
3    0
4    0
Name: income_ >50K, dtype: uint8
'''

#  문제와 답의 차수 확인
print(x.shape)  # (32561, 44)   2차원
print(y.shape)  # (32561,)  1차원


#  기계학습을 시키기 위하여
#  Regression => 회귀 분석
#  sklearn 의 linear_model 의 LogisticRegression()

from sklearn import linear_model, model_selection

# 문제 x 와 답 y를 훈련에 참여시킬 데이터와 검증을 위한 데이터로 분리
train_x, test_x, train_y, test_y = model_selection.train_test_split(x,y)
print(len(train_x)) # 24420
print(len(train_y)) # 24420
print(len(test_x))  # 8141
print(len(test_y))  # 8141

lr = linear_model.LogisticRegression()
lr.fit(train_x,train_y) # 훈련용 데이터와 답을 갖고 학습 시키기
r = lr.predict(test_x) # 검증용 문제를 갖고 훈련이 잘 되었는지 검증 (예측하기 - 문제로)

# 예측한 것(r)과 진짜 답하고 비교
print(len(r))   # 8141
print(len(test_y))  # 8141

result = r == test_y    # 예측한 결과 r과 검증을 위한 진짜 답 test_y 를 서로 비교합니다.
print(result)
'''
11125     True
15212     True
1950     False
16024     True
30898     True
23324    False
16066     True
12771     True
8966      True
15650     True
Name: income_ >50K, Length: 8141, dtype: bool
'''

a = result.values     # 검증한 결과가 Series 라서 value 만 뽑아온다,
b = a[a == True]     # True 인것만 추출
print(len(b))         # 6668

print('정답률 : ',len(b)/len(test_y)*100)  # 정답률 :  81.90639970519592


# 정답률을 알기 위해 LogisticRegression 의 score 함수를 이용해 봅시다,
print("정답률 : ", lr.score(test_x,test_y))



































































































