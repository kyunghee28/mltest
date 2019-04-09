from sklearn import preprocessing
import numpy as np

# 문자를 이진화 배열로 만들세요 => LabelBinarizer

# x = ['yes','no','yes']
# lb = preprocessing.LabelBinarizer()
# bn = lb.fit_transform(x)
# print(bn)
'''
[[1][0][1]]
'''

x = ['yes','no','yes','cencel']
lb = preprocessing.LabelBinarizer()
bn = lb.fit_transform(x)
# print(bn)
'''
[[0 0 1]
 [0 1 0]
 [0 0 1]
 [1 0 0]]
'''
#  다시 문자로 바꾸기
r = np.array([[0,0,1]])
s = lb.inverse_transform(r)
print(s)    # ['yes']

r2 = np.array([[1, 0 ,0]])
s2 = lb.inverse_transform(r2)
print(s2)   # ['cencel']

s3 = lb.inverse_transform(bn)
# print(s3)   ['yes' 'no' 'yes' 'cencel']

data = ['paris','tokyo','london','paris']
b = preprocessing.LabelBinarizer()
a = lb.fit_transform(data)
print(a)
'''
[[0 1 0]
 [0 0 1]
 [1 0 0]
 [0 1 0]]
'''

r = np.array([[0, 1, 0]])
result = lb.inverse_transform(r)
print(result)   # ['paris']
