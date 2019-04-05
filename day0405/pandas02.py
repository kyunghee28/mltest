import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import matplotlib.pyplot as plt

# 예제) 수학점수가 평균이하인 모든학생의 성적을 막대그래프로 나타내기

df = pd.read_csv('../data/scores.csv')  # csv파일 읽어오기

matavg = df[df['mat'] <= df['mat'].mean()]
# print(matavg)
'''
        class    name  kor  eng  mat  bio
    1       1  andrew   45   45   56   98
    6       2    paul   87   67   65   56
    8       2   oscar  100   78   56   65
    10      2    hugh   98   45   56   54
'''

del matavg['class']
matavg.index = matavg['name']   # 인덱스(키)를 이름으로
del matavg['name']
matavg_math = matavg['mat']
# print(matavg['mat'])
'''
    name
    andrew    56
    paul      65
    oscar     56
    hugh      56
    Name: mat, dtype: int64
'''

rc('font',family=font_manager.FontProperties(fname="C:/WINDOWS/Fonts/H2GPRM.TTF").get_name())

matavg_math.plot(kind='bar')
plt.title("수학점수가 평균이하인 학생")
plt.show()
