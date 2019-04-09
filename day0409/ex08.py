from sklearn import preprocessing
import numpy as np

# 결측치에 대한 처리
# 수집한 데이터에는 결측치가 많을 수 있다,

x = [[1,2],[np.nan,3],[7,6],[7,2],[2,3],[3,4]]

# preprocessing  에 Imputer 함수로 결측치를 원하는 값으로 설정가능
imp =preprocessing.Imputer(missing_values='NaN', strategy='mean')    # strategy='mean' -> 평균을 채워줘
x2 = imp.fit(x).transform(x)
print(x2)
'''
[[1. 2.]
 [4. 3.]
 [7. 6.]
 [7. 2.]
 [2. 3.]
 [3. 4.]]
'''
imp2 =preprocessing.Imputer(missing_values='NaN', strategy='median')    # strategy='median' -> 중앙값으로 채워줘
x3 = imp2.fit(x).transform(x)
print(x3)
'''
[[1. 2.]
 [3. 3.]
 [7. 6.]
 [7. 2.]
 [2. 3.]
 [3. 4.]]
'''

