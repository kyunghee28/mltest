from sklearn import preprocessing
import numpy as np

# 때에 따라 데이터의 범위를 축소시켜야할 때가 있다.
# 값의 범위가 큰 것보다는 작은 것이 기계학습에 훨씬 효율을 높일 수 있다,
# 가급적 문자데이터 보다는 숫자데이터를 학습시키는 것이 더 좋다
# 가급적 숫자의 범위를 2진화 시키는 것이 더 효울성이 높을 수 있다.

x = [[1,-1,3],[2,0,0],[0,1,-1]]

# Binarizer() => 2진화 시켜주는 객체
binarizer = preprocessing.Binarizer()
print(binarizer)    # Binarizer(copy=True, threshold=0.0)
print(type(binarizer))  # <class 'sklearn.preprocessing.data.Binarizer'>

r = binarizer.fit(x)
print(r)    # Binarizer(copy=True, threshold=0.0)

# transform() => x 를 2진화 데이터로 만들어줌.
b = r.transform(x)
print(b)
'''
[[1 0 1]
 [1 0 0]
 [0 1 0]]
'''

c = preprocessing.Binarizer().fit(x).transform(x)
print(c)
'''
[[1 0 1]
 [1 0 0]
 [0 1 0]]
'''