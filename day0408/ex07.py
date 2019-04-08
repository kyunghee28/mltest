import numpy as np
import pandas as pd

scores = pd.read_csv("../data/scores.csv")
print(scores)
'''
    class    name  kor  eng  mat  bio
0       1    adam   67   87   90   98
1       1  andrew   45   45   56   98
2       1     ben   95   59   96   88
3       1   clark   65   94   89   98
4       1     dan   45   65   78   98
5       1    noel   78   76   98   89
6       2    paul   87   67   65   56
7       2  walter   89   98   78   78
8       2   oscar  100   78   56   65
9       2  martin   99   89   87   87
10      2    hugh   98   45   56   54
11      2   henry   65   89   87   78
'''


print(scores.mean())    # 과목별 평균
'''
class     1.500000
kor      77.750000
eng      74.333333
mat      78.000000
bio      82.250000
dtype: float64
'''

print(scores[['kor','eng','mat','bio']].mean(axis=1))
'''
0     85.50
1     61.00
2     84.50
3     86.50
4     71.50
5     85.25
6     68.75
7     85.75
8     74.75
9     90.50
10    63.25
11    79.75
dtype: float64
'''

# scores 데이터 프레임에 각 학생별 평균을 계산해서 avg 칼럼추가
scores['avg'] = scores[['kor','eng','mat','bio']].mean(axis=1)
print(scores)
'''
    class    name  kor  eng  mat  bio    avg
0       1    adam   67   87   90   98  85.50
1       1  andrew   45   45   56   98  61.00
2       1     ben   95   59   96   88  84.50
3       1   clark   65   94   89   98  86.50
4       1     dan   45   65   78   98  71.50
5       1    noel   78   76   98   89  85.25
6       2    paul   87   67   65   56  68.75
7       2  walter   89   98   78   78  85.75
8       2   oscar  100   78   56   65  74.75
9       2  martin   99   89   87   87  90.50
10      2    hugh   98   45   56   54  63.25
11      2   henry   65   89   87   78  79.75
'''