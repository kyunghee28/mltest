import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pythonTest.day0408.bitutil

df = pythonTest.day0408.bitutil.getMovies()

# unstack() : index를 columns으로 바꿔준다.
r1 = df.pivot_table(values='rating', index='gender', aggfunc='mean')
# print(r1)
'''
          rating
gender          
F       3.620366
M       3.568879
'''
r2 =r1.unstack()
# print(r2)
'''
        gender
rating  F         3.620366
        M         3.568879
dtype: float64
'''

f1 = df.pivot_table(values='rating', index=['gender','age'], aggfunc='mean')
# print(f1)
'''
                rating
gender age          
F      1    3.616291
       18   3.453145
       25   3.606700
       35   3.659653
       45   3.663044
       50   3.797110
       56   3.915534
M      1    3.517461
       18   3.525476
       25   3.526780
       35   3.604434
       45   3.627942
       50   3.687098
       56   3.720327
'''
f2 =f1.unstack()
# print(f2)
'''
age           1         18       25        35        45        50        56
gender                                                                     
F       3.616291  3.453145  3.60670  3.659653  3.663044  3.797110  3.915534
M       3.517461  3.525476  3.52678  3.604434  3.627942  3.687098  3.720327
'''

f3 = f2.stack()     # column -> index
# print(f3)

# 예제 . 나이별, 성별로 별점의 평균과 합을 출력해 봅니다.
# help(pd.DataFrame.pivot_table)

# age_gender = df.pivot_table(values='rating', index=['gender','age'], aggfunc=['mean','sum'])
age_gender = df.pivot_table(values='rating', index=['age','gender'], aggfunc=['mean','sum'])
# age_gender = df.pivot_table(values='rating', index='age', columns='gender',aggfunc=['mean','sum'])
# 때에따라, numpy함수를 요구할 수도 있다.
# age_gender = df.pivot_table(values='rating', index='age', columns='gender',aggfunc=[np.mean,np.sum])
# print(age_gender)

# 예제 . 나이별, 성별로 별점의 평균을 구하세요
a = df.pivot_table(values='rating', index='age', columns='gender', aggfunc='mean')
print(a)
'''
gender         F         M
age                       
1       3.616291  3.517461
18      3.453145  3.525476
25      3.606700  3.526780
35      3.659653  3.604434
45      3.663044  3.627942
50      3.797110  3.687098
56      3.915534  3.720327
'''

# 예제 . 나이별, 성별로 별점의 합을 구하세요
b = df.pivot_table(values='rating', index='age', columns='gender', aggfunc='sum')
print(b)
'''
gender       F        M
age                    
1        31921    64665
18      156866   486900
25      329436  1072903
35      181054   538971
45       88316   215946
50       68591   200674
56       36019   110051
'''

# 위에 a,b를 합치고 싶어요
# r1 = pd.merge(r1,r2)
# print(r1)   #오류

# 열으로
r2 = pd.concat([a,b])
print(r2)
'''
gender              F             M
age                                
1            3.616291  3.517461e+00
18           3.453145  3.525476e+00
25           3.606700  3.526780e+00
35           3.659653  3.604434e+00
45           3.663044  3.627942e+00
50           3.797110  3.687098e+00
56           3.915534  3.720327e+00
1        31921.000000  6.466500e+04
18      156866.000000  4.869000e+05
25      329436.000000  1.072903e+06
35      181054.000000  5.389710e+05
45       88316.000000  2.159460e+05
50       68591.000000  2.006740e+05
56       36019.000000  1.100510e+05
'''
# 행으로
r3 = pd.concat([a,b], axis=1)
print(r3)
'''
gender         F         M       F        M
age                                        
1       3.616291  3.517461   31921    64665
18      3.453145  3.525476  156866   486900
25      3.606700  3.526780  329436  1072903
35      3.659653  3.604434  181054   538971
45      3.663044  3.627942   88316   215946
50      3.797110  3.687098   68591   200674
56      3.915534  3.720327   36019   110051
'''