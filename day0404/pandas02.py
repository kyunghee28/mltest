import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

r = pd.read_csv('./data/scores.csv')    # 파일을 읽어옴
print(r)
'''결과 
        class    name  kor  eng  mat  bio
0           1    adam   67   87   90   98
1           1  andrew   45   45   56   98
2           1     ben   95   59   96   88
3           1   clark   65   94   89   98
4           1     dan   45   65   78   98
5           1    noel   78   76   98   89
6           2    paul   87   67   65   56
7           2  walter   89   98   78   78
8           2   oscar  100   78   56   65
9           2  martin   99   89   87   87
10          2    hugh   98   45   56   54
11          2   henry   65   89   87   78
인덱스
(key역활)
'''

print(type(r))      # 결과 : <class 'pandas.core.frame.DataFrame'>  => 파일을 읽어 DataFrame
print(r.index)      # 결과 : RangeIndex(start=0, stop=12, step=1)   => 키(인덱스)를 확인
print(r.columns)    # 결과 : Index(['class', 'name', 'kor', 'eng', 'mat', 'bio'], dtype='object')  => 컬럼명들을 확인

print(r.values)
'''결과 
    [[1 'adam' 67 87 90 98]
     [1 'andrew' 45 45 56 98]
            ..
     [2 'henry' 65 89 87 78]]
'''

print(type(r.values))   # 결과 : <class 'numpy.ndarray'>

print(r['kor'])    # => 국어 점수만 출력
''' 결과 
    0      67
    1      45
        ''
    11     65
'''
#print(r[2]) # 결과 : 오류!! => 2번쩨 행만 출력 X , 2번째 열만 출력 X

'''
    pandas의 DataFrame에선 행에 접근할 때 loc 이나 iloc 함수를 이용해 행에 접근 할 수 있다.
    key 값을 부여하지 않았는데 행에 접근하려면 index로 접근합니다.
    이 때는 loc 이나 iloc 에 차이가 없다,
    그러나 key값을 부여했을 때는
    index로 접근할 때는 iloc을 쓰고
    key로 접근할 땐 loc 을 사용
'''

print(r.loc[2])
'''결과
Name: kor, dtype: int64
class      1
name     ben
kor       95
eng       59
mat       96
bio       88
Name: 2, dtype: object
'''

print(r.loc[2].values)  # 결과 : [1 'ben' 95 59 96 88]

print(r.iloc[2])
'''결과
class      1
name     ben
kor       95
eng       59
mat       96
bio       88
Name: 2, dtype: object
'''


# ex. 내가 직점 DataFrame 만들 수 있음
# df = pd.DataFrame([[1,2,3],[4,5,6]])
# print(df)
# print(type(df))
'''결과 
   0  1  2
0  1  2  3
1  4  5  6 
<class 'pandas.core.frame.DataFrame'>
'''

