from sklearn import datasets, svm, neighbors, model_selection
import numpy as np
import pandas as pd

# sklearn의 dataset 가 제공하는 iris 데이터를 읽어와 봅시다,
iris = datasets.load_iris()

# iris를 확인하고 문제(꽃받침의 길이,넓이, 꽃잎의 길이, 넓이)와 달(품종)이 어떤 속성으로 제공되는지 확인
# print(iris['DESCR'])
# print(iris['data'])
# print(iris['target'])
# print(iris['target_names']) # ['setosa' 'versicolor' 'virginica']

# 골고루 잘 섰어서 문제와 답을 분리하여 훈련용데이터 테이스용데이터로 분리
train_x, test_x, train_y, test_y = model_selection.train_test_split(iris['data'],iris['target'])
print(len(test_x),len(train_x)) # 38 112
print(len(test_y),len(train_y)) # 38 112

# 학습시키기 위하여 neighbors 객체를 생성합니다.
knn = neighbors.KNeighborsClassifier()
knn.fit(train_x,train_y)

r = knn.predict(test_x)
print(r == test_y)
'''
[False  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True False  True  True  True  True
  True  True  True  True  True  True  True  True  True  True  True  True
  True  True]
'''
label = iris['target_names']
x = [[4.6,3.6,1.,0.2]]
r = knn.predict(x)
rs = label[r]
print(rs)   # ['setosa']