import numpy as np
from sklearn import preprocessing

age = [28,20,38,34]

b_age = preprocessing.LabelBinarizer().fit_transform(age)
print(b_age)
'''
[[0 1 0 0]  28
 [1 0 0 0]  20
 [0 0 0 1]  38
 [0 0 1 0]] 34
'''

addr = ['서울','마산','서울','대전','광주']
b_addr = preprocessing.LabelBinarizer().fit_transform(addr)
print(b_addr)

'''     
[[0 0 0 1]  서울
 [0 0 1 0]  마산
 [0 0 0 1]  서울
 [0 1 0 0]  대전
 [1 0 0 0]] 광주
'''

# 데이터의 value 만큼 속성이 만들어 진다.

