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

