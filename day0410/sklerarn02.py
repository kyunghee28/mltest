import numpy as np
import pandas as pd

age = [28,20,38,34]
addr = ['서울','마산','서울','대전','광주']

b_age = pd.get_dummies(age)
print(b_age)
''' 
pandas는 칼럼이름까지 지정해준다.

   20  28  34  38
0   0   1   0   0
1   1   0   0   0
2   0   0   0   1
3   0   0   1   0
'''

b_addr = pd.get_dummies(addr)
print(b_addr)
'''
   광주  대전  마산  서울
0   0   0   0   1
1   0   0   1   0
2   0   0   0   1
3   0   1   0   0
4   1   0   0   0
'''