import numpy as np
import pandas as pd

member = pd.read_csv("../data/member.dat")
print(member)
'''
       id name  age addr
0   tiger  이순신   20   서울
1    lion  강감찬   30   대전
2     cat  유관순   40   울산
3  monkey  홍길동   40   서울
'''
print(member.columns)   # Index(['id', 'name', 'age', 'addr'], dtype='object')

# addr 칼럼과 age칼럼을 각각 one-hot테이브을 생성,
b_age = pd.get_dummies(member['age'])
print(b_age)
'''
   20  30  40
0   1   0   0
1   0   1   0
2   0   0   1
3   0   0   1
'''

b_addr = pd.get_dummies(member['addr'])
print(b_addr)
'''
   대전  서울  울산
0   0   1   0
1   1   0   0
2   0   0   1
3   0   1   0
'''