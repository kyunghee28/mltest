# 연습 ) 고객의 나이, 직업분류, 학력, 직업, 성별, 인종, 주당근무시간을 입력받아
#  연봉이 5만달러 이상이면 '대출가능' 그렇지 않으면 '대출불가능'을 출력하는 웹어플리케이션을 구현합니다,
#  단, 직업분류, 학력, 직업, 성별, 인종 은 우리가 훈련시킬 데이터 adult.data.txt 의 내용으로 제한하도록 합니다.

import numpy as np
import pandas as pd
from sklearn import linear_model, model_selection

def MemberInfo(list):

    names = ['age','workclass','fnlwgt','education','education-num','marital-status',
             'occupation','relationship','race','sex','capital-gain','capital-loss',
             'hours-per-week','native-country','income']

    df = pd.read_csv('../data/adult.data.txt' ,header=None, names=names)

    df = df[['age','workclass','education','occupation','sex','race','hours-per-week','income']]

    new_df = pd.get_dummies(df)
    # print(new_df) [32561 rows x 35 columns]

    # 문제는 x , 답은 y
    x = new_df.iloc[:, :-2]  # income 칼럼 제외
    # print(x)    [32561 rows x 33 columns]

    y = new_df.iloc[:, -1]
    # print(y) # :  1 -> 5만달러 이상  , 0 -> 5만달러 미만

    # 문제 x 와 답 y를 훈련에 참여시킬 데이터와 검증을 위한 데이터로 분리
    train_x, test_x, train_y, test_y = model_selection.train_test_split(x,y)

    lr = linear_model.LogisticRegression()
    lr.fit(train_x,train_y) # 훈련용 답,문제를 학습시키기
    # lr.predict(test_x)  # 훈련잘 되었는지 확인

    n_df = pd.DataFrame(list, columns=['age','workclass','education','occupation','sex','race','hours-per-week'])

    df2 = df.append(n_df, ignore_index=True)
    op = pd.get_dummies(df2)

    pred_x = np.array(op.iloc[-1,:-2]).reshape(1,-1)
    pred_y = lr.predict(pred_x)
    print(pred_y)
    return pred_y



