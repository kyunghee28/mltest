import numpy as np
import pandas as pd
from sklearn import linear_model, model_selection

names = ['age','workclass','fnlwgt','education','education-num','marital-status',
         'occupation','relationship','race','sex','capital-gain','capital-loss',
         'hours-per-week','native-country','income']

df = pd.read_csv('../data/adult.data.txt' ,header=None, names=names)

df_choice = df[['age','workclass','education','sex','race','hours-per-week','occupation','income']]

new_df = pd.get_dummies(df_choice)

x = new_df.iloc[:,:-2]
y = new_df.iloc[:,-1]

#  문제와 답의 차수 확인
print(x.shape)  # (32561, 44)   2차원
print(y.shape)  # (32561,)  1차원

# 문제 x 와 답 y를 훈련에 참여시킬 데이터와 검증을 위한 데이터로 분리
train_x, test_x, train_y, test_y = model_selection.train_test_split(x,y)

lr = linear_model.LogisticRegression()
lr.fit(train_x,train_y) # 훈련용 데이터와 답을 갖고 학습 시키기
r = lr.predict(test_x)  # 검증용 문제를 갖고 훈련이 잘 되었는지 검증 (예측하기 - 문제로)

# 연습 ) 실 데이터를 가지고 적용시켜 봅시다.
# 47, Private, 287828, Bachelors, 13, Married-civ-spouse, Exec-managerial, Wife, White, Female, 0, 0, 40, United-States, >50K

# 알고자하는 데이터를 훈련시킨 feature 의 수와 동일하게 하기 위하여
# 원래 원본데이터의 맨 마지막에 추가시키고 one-hot 인코딩을 합시다. (data => 원본데이터)

n = [[47,' Private',' Bachelors',' Female',' White',40,' Exec-managerial',' >50K']]
n_df = pd.DataFrame(n, columns=['age','workclass','education','sex','race','hours-per-week','occupation','income'])

print(len(df_choice))    # 32561

df2 = df_choice.append(n_df, ignore_index=True)    # => 행을 추가
print(len(df2))    # 32562

print(df2.iloc[-1,:])
'''
age                             47
workclass                  Private
education                Bachelors
sex                         Female
race                         White
hours-per-week                  40
occupation         Exec-managerial
income                        >50K
Name: 32561, dtype: object
'''

one_hot = pd.get_dummies(df2)

print(len(one_hot.columns)) # 51
print(len(new_df.columns))  # 51

pred_x = np.array(one_hot.iloc[-1,:-2]).reshape(1,-1)
pred_y = lr.predict(pred_x)

print(pred_y)   # [0]

'''
1 이 나오면 5만달라 이상 버는 것
0 이 나오면 5만달라 미만 버는 것
'''











































































































































































