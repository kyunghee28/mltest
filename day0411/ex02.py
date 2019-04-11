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

# fancy indexing
# 2차원 배열인 경우 원하는 데이터를 추출하기 위하여 행열을 분리하여 범위를 지정하여 slicing할 수 있다.
# 데이터프레임[행,열]

x = new_df.iloc[:,:-2]
print(x.columns)

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

a = result.values     # 검증한 결과가 Series 라서 value 만 뽑아온다,
b = a[a == True]     # True 인것만 추출
print(len(b))         # 6668

print('정답률 : ',len(b)/len(test_y)*100)  # 정답률 :  81.90639970519592

# 정답률을 알기 위해 LogisticRegression 의 score 함수를 이용해 봅시다,
print("정답률 : ", lr.score(test_x,test_y))



































































































