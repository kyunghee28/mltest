import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import  train_test_split

def irismodule(realdatanum1,realdatanum2,realdatanum3,realdatanum4):
    # 알아서 데이터 프레임 형태로 읽어오게하기
    csv = pd.read_csv('iris.csv')

    # 문제와 답 분리
    csv_data = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
    csv_label = csv['Name']

    # 학습 전용 데이터와 테스트 전용 데이터로 나누기
    # 훈련시킬 데이터, 검증을 하기위한 문제, 훈련의 대한 답
    # 다중반환 가능하기때문에 한번에 여러변수를 나란히 놓을 수 있다.
    train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)
    #  train_test_split가 매개변수 csv_data(문제), csv_label(답) 을 주면 4덩어리로 반환한다.
    # train_test_split가 잘 섞어줌

    # 학습시키고 예측하기
    clf = svm.SVC()
    clf.fit(train_data, train_label) # fit이 공부시켜줌.

    realdata = [[realdatanum1, realdatanum2, realdatanum3, realdatanum4]]
    r = clf.predict(realdata)
    return r

