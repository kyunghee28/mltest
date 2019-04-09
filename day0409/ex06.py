from sklearn import preprocessing
import numpy as np

#  때에 따라 존재하지 않는 임의의 특징값(feature)를 만들어야 하는 경우가 있을 수 있는데
# sklearn 의 preprocessing 을 이용하여 임의의 특징값을 생성해 봅시다,

x = [[0,1],[3,5]]
x2 = preprocessing.add_dummy_feature(x)
print(x2)
