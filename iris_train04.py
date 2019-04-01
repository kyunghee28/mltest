# 사용자한테 꽃받침의 길이, 넓이, 꽃잎의 길이,넓이를 입력받아 붓꽃의 품종을 알아 맞추는 웹어플리케이션 작성

import pandas as pd
from sklearn import svm,metrics
from sklearn.model_selection import train_test_split

def irislist(r1,r2,r3,r4):
    # 붓꽃의 csv 데이터 읽어오기
    csv = pd.read_csv('iris.csv')
    # print(csv)
    # 필요한 열 추출하기
    csv_data = csv[['SepalLength','SepalWidth', 'PetalLength' , 'PetalWidth']]
    csv_label = csv['Name']

    train_data,test_data,train_label,test_label = train_test_split(csv_data,csv_label)

    # 데이터 학습시키고 예측하기
    clf = svm.SVC()
    clf.fit(train_data,train_label)

    pre = clf.predict(test_data)
    ac_score = metrics.accuracy_score(test_label,pre)

    real_data = [[r1,r2,r3,r4]]
    result = clf.predict(real_data)
    result = result[0]
    ac = int(ac_score * 100)

    return result,ac
