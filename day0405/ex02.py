import numpy as np
import pandas as pd

# 서로 관련있는 두개의 데이터 파일을 읽어들어 하나의 데이터프레임으로 만들어 봅시다.

# student01과 student02 의 파일의 내용을 읽어들어 각각 df1과 df2에 담기.
df1 = pd.read_csv('../data/student01', sep="::", engine='python')
df2 = pd.read_csv('../data/student02', sep="::", engine='python')
# line terminator 는 engine 이 c 만 가능.

# 두개 데이터 합치기
df = pd.merge(df1,df2)

print(df)
'''
      name  kor  eng  mat  bio  class  age
0     adam   67   87   90   98      1   27
1   andrew   45   45   56   98      1   25
2      ben   95   59   96   88      1   24
3    clark   65   94   89   98      1   26
4      dan   45   65   78   98      1   45
5     noel   78   76   98   89      1   28
6     paul   87   67   65   56      2   55
7   walter   89   98   78   78      2   29
8    oscar  100   78   56   65      2   20
9   martin   99   89   87   87      2   29
10    hugh   98   45   56   54      2   28
11   henry   65   89   87   78      2   25
'''




