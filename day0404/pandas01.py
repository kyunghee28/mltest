# numpy     배열의 조작을 편리하게 해준다.
# pandas    데이터프레임의 조작을 편리하게 해준다.

# 머신러닝을 위한 많은 라이브러리들이
# 상대하는 데이터형태가 numpy 이거나 pandas를 취급한다.

'''
pandas의 자료구조
Series : 1차원배열
DataFrame : 2차원배열
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 예제1-1. 파이썬 기본배열을 Pandas의 1차원 배열로 만들어 봅시다,
a = [1,2,3,4,5]
arr = pd.Series(a)
print(arr)
''' 결과
0    1
1    2
2    3
3    4
4    5
dtype: int64
'''
print(type(a))  # 결과 : <class 'list'>
print(type(arr))  # 결과 : <class 'pandas.core.series.Series'>

print("-"*30)

# 예제1-2. pandas의 1차원 배열인 Series를 파이선 배열로 만들어 봅시다.
arr = pd.Series(['강감찬','홍길동','이순신','유관순'])
print(arr)
''' 결과 -> 인덱스(0,1,2,3)를 부여한 형태
0    강감찬
1    홍길동
2    이순신
3    유관순
dtype: object
'''
print(type(arr))      # 결과 : <class 'pandas.core.series.Series'>

name = list(arr) # => pandas배열을 파이썬 배열로

print(name)          # 결과 : ['강감찬', '홍길동', '이순신', '유관순']
print(type(name))    # 결과 : <class 'list'>

print("-"*30)

# 예제2-1. Series는 pandas에서 1차원 배열을 취급한다고 되어있었는데
#   Series를 만들때 2차원 배열을 매개변수로 주면 어떤일이 일어나는지 알아봅시다.

arr = pd.Series([[1,2,3],[4,5,6]])
print(arr)
'''결과 
0    [1, 2, 3]
1    [4, 5, 6]
dtype: object
'''
print(arr[0])           # 결과 : [1, 2, 3]
print(type(arr[0]))     # 결과 : <class 'list'>
print(arr[0][1])        # 결과 : 2
print(type(arr[0][1]))  # 결과 : <class 'int'>

print("-"*30)

# 예제2-2.  Series를 만들때 2차원 배열을 주었을 때
arr = pd.Series([['강감찬','홍길동','이순신'],['서울','광주','울산']])
print(arr)
'''결과 
0    [강감찬, 홍길동, 이순신]
1       [서울, 광주, 울산]
dtype: object
'''

arr2 = pd.Series([['강감찬','홍길동','이순신'],['강감찬','홍길동','이순신']])
print(arr2)
'''결과 
0    [강감찬, 홍길동, 이순신]
1    [강감찬, 홍길동, 이순신]
dtype: object
'''

print("-"*30)

# 예제2-3. Series를 만들때 3차원 배열을 주었을 때
arr = pd.Series([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6,]],[[1,2,3],[4,5,6,]]])
print(arr)
'''결과 
0    [[1, 2, 3], [4, 5, 6]]
1    [[1, 2, 3], [4, 5, 6]]
2    [[1, 2, 3], [4, 5, 6]]
dtype: object
'''

print("-"*30)

# 예제 3-1.
# Series는 마치 자바의 map 같이 key , value 가 한쌍으로 이루어지는 자로구조를 표현하기에 적합하다.
# key를 부여하지 않으면 차례대로 index가 부여된다.
# 필요하다면 key를 부여할 수 있다.

a = pd.Series([5,6,3,7,6])
print(a)
'''결과 
0    5
1    6
2    3
3    7
4    6
dtype: int64
'''
print(a.values)         # 결과 : [5 6 3 7 6]
print(type(a.values))   # 결과 : <class 'numpy.ndarray'>
print(a.index)          # 결과 : RangeIndex(start=0, stop=5, step=1)

print("-"*30)

# 예제 3-2
# 각각의 값을 어떤 값을 의미하는지 key를 부여할 수 있다.,
# 생략시, 차례대로 인덱스가 부여된다.

a = pd.Series([5,6,3,7,6], index=['김경희','박민서','이혜민','김미영','이미영'])

print(a)
''' 결과 
김경희    5
박민서    6
이혜민    3
김미영    7
이미영    6
dtype: int64
'''

# key로 접근 -> key 값을 부여하면 key값으로 데이터에 접근할 수 있다. => 직관적
print(a['김미영'])    # 결과 : 3

# 인덱스로 접근 ->  key 값을 부여했다 하더라고 index로 접근할 수 있따.
print(a[3])     # 결과 : 3

print(a.index)  # 결과 : Index(['김경희', '박민서', '이혜민', '김미영', '이미영'], dtype='object')

print("-"*30)

# 예제 3-3.

keys = a.index              # Series의 키값을 모두 뽑아온다
for key in keys:            # key의 개수만큼 반복수행하여 각 요소의 key 와 value를 출력
    print(key, a[key])
    ''' 결과 
        김경희 5
        박민서 6
        이혜민 3
        김미영 7
        이미영 6
    '''
print("-"*30)

# pandas의 serise는 파이썬 배열을 갖고 key값을 부여해 보다 직관적으로 접근할 수 있다.
# 예제 3-4. 파이썬 딕셔너리를 갖고 serise를 만들수 있는지 확인해보세요.
a = {'김경희' : 5, '박민서' : 9, '이혜민' : 2, '김미영' : 11, '이미영' : 20}

print(type(a))      # 결과 : <class 'dict'>
s = pd.Series(a)
print(s)
''' 결과 
김경희     5
박민서     9
이혜민     2
김미영    11
이미영    20
dtype: int64
'''