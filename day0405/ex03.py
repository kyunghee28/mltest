# 합치고자 하는 두개의 파일에 데이터 수가 일치하지 않아요
# dan 학생의 점수정보는 없다.

import numpy as np
import pandas as pd

df1 = pd.read_csv('../data/stu01', sep="::", engine='python')
df2 = pd.read_csv('../data/stu02', sep="::", engine='python')

df = pd.merge(df1,df2)

print(df)   # dan은 나오지 않음
'''
      name  kor  eng  mat  bio  class  age
0     adam   67   87   90   98      1   27
1   andrew   45   45   56   98      1   25
2      ben   95   59   96   88      1   24
3    clark   65   94   89   98      1   26
4     noel   78   76   98   89      1   28
5     paul   87   67   65   56      2   55
6   walter   89   98   78   78      2   29
7    oscar  100   78   56   65      2   20
8   martin   99   89   87   87      2   29
9     hugh   98   45   56   54      2   28
10   henry   65   89   87   78      2   25

'''

