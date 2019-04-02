import numpy as np

a = ['160.7','180.9','145.2','175.7','160.7','165.8']

# 연습 ) 파이썬 배열의 numpy 배열로 만든 후 170이상 데이터 뽑아
# 새로운 numpy배열로 만드세요

b = np.array(a, dtype='float64')
c = b[b > 170]
print(c)
print(type(c))

