import pandas as pd
from sklearn import svm,metrics
from sklearn.model_selection import train_test_split

# 붓꽃의 csv 데이터 읽어오기
csv = pd.read_csv('iris.csv')

# print(csv)
    #      SepalLength  SepalWidth  PetalLength  PetalWidth            Name
    # 0            5.1         3.5          1.4         0.2     Iris-setosa
    # 1            4.9         3.0          1.4         0.2     Iris-setosa
    # 2            4.7         3.2          1.3         0.2     Iris-setosa
    # 3            4.6         3.1          1.5         0.2     Iris-setosa
# print(type(csv)) #<class 'pandas.core.frame.DataFrame'>

# 필요한 열 추출하기 - data : 문제 , label : 답
csv_data = csv[['SepalLength','SepalWidth', 'PetalLength' , 'PetalWidth']]
csv_label = csv['Name']

# print(csv_data)
    #    SepalLength  SepalWidth  PetalLength  PetalWidth
    # 0            5.1         3.5          1.4         0.2
    # 1            4.9         3.0          1.4         0.2
# print(csv_label)
    # 0         Iris-setosa
    # 1         Iris-setosa


# 학습전용 데이터와 테스트 전용 데이터로 나누기!
# 파이썬은 다중반환 가능!
# 훈련시킬 문제, 검증하기 위한 문제, 훈련시킬 답, 검증시킬 답 = train_test_split(전체문제,전체 답)
train_data,test_data,train_label,test_label = train_test_split(csv_data,csv_label)
                                                                #pandas의 데이터 프레임을 원함

# 데이터 학습시키고 예측하기
clf = svm.SVC()
clf.fit(train_data,train_label)

# train_test_split는 데이터를 섞어 무작위로 훈련데이터와 테스트데이터로 나눈다.(따로 random안해줘도 된다.)
# print(train_data)
    #      SepalLength  SepalWidth  PetalLength  PetalWidth
    # 28           5.2         3.4          1.4         0.2
    # 71           6.1         2.8          4.0         1.3
# print(train_label)
    # 28         Iris-setosa
    # 71     Iris-versicolor

pre = clf.predict(test_data)

#정답률 구하기
ac_score = metrics.accuracy_score(test_label,pre)
print('정답률 :',ac_score) #정답률 : 0.9736842105263158

real_data = [[5.8,2.7,4.1,1.0]]
r2 = clf.predict(real_data)
print(r2) #['Iris-versicolor']