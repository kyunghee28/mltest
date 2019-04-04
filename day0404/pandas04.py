import numpy as np
import pandas as pd

info = pd.read_csv('data/scores.csv')  # 파일 읽어오기

print("-" * 2, '연습1', "-" * 20)
# 연습1 ) scores.scv 파일을 읽어 학생의 이름을 인덱스(key)로 설정하고 이름 칼럼을 삭제하세요

# 학생이름을 인덱스로 설정
info.index = info['name']

# 이름 컬럼 삭제
del info['name']

# print(info)

''' 결과 

                class  kor  eng  mat  bio
    name                             
    adam        1   67   87   90   98
    andrew      1   45   45   56   98
    ben         1   95   59   96   88
    clark       1   65   94   89   98
    dan         1   45   65   78   98
    noel        1   78   76   98   89
    paul        2   87   67   65   56
    walter      2   89   98   78   78
    oscar       2  100   78   56   65
    martin      2   99   89   87   87
    hugh        2   98   45   56   54
    henry       2   65   89   87   78

'''

# print("-" * 2, '연습2', "-" * 20)
# 연습2 ) scores.scv 파일을 읽어 모든 학생의 국어점수를 출력하세요

#방법1.
# print(info.iloc[:][['kor']])

''' 결과 
            kor
    name       
    adam     67
    andrew   45
    ben      95
    clark    65
    dan      45
    noel     78
    paul     87
    walter   89
    oscar   100
    martin   99
    hugh     98
    henry    65
'''

#방법2.
print(info['kor'])

''' 결과 
    name
    adam       67
    andrew     45
    ben        95
    clark      65
    dan        45
    noel       78
    paul       87
    walter     89
    oscar     100
    martin     99
    hugh       98
    henry      65
    Name: kor, dtype: int64
'''


# print("-" * 2, '연습3', "-" * 20)
# 연습3 ) scores.scv 파일을 읽어 모든 과목의 점수를 출력하세요

# print(info[['kor','eng','mat','bio']])

''' 결과 

            kor  eng  mat  bio
    name                      
    adam     67   87   90   98
    andrew   45   45   56   98
    ben      95   59   96   88
    clark    65   94   89   98
    dan      45   65   78   98
    noel     78   76   98   89
    paul     87   67   65   56
    walter   89   98   78   78
    oscar   100   78   56   65
    martin   99   89   87   87
    hugh     98   45   56   54
    henry    65   89   87   78

'''

from matplotlib import font_manager,rc,colors
import matplotlib.pyplot as plt

rc('font',family=font_manager.FontProperties(fname="C:/WINDOWS/Fonts/H2GPRM.TTF").get_name())

print("-" * 2, '연습4', "-" * 20)
# 연습4 ) ben학생의 과목별 점수를 막대그래프로 나타내 봅니다.

sub = ['kor','eng','mat','bio']

print(info.loc['ben',sub])
plt.subplot(211)
plt.bar(sub,info.loc['ben',sub],0.5, color="g")
plt.title("ben학생의 과목별 점수")


print("-" * 2, '연습5', "-" * 20)
# 연습8 ) 모든학생의 국어점수를 막대그래프로 나타내 봅니다.

print(info['kor'])
print(info.index)
plt.subplot(212)
plt.bar(info.index,info["kor"],0.4,color=colors.TABLEAU_COLORS)
plt.title("모든학생의 국어점수")
plt.show()



