import numpy as np
import pandas as pd

# d= pd.read_csv('/data/scores.csv')  : 절대 경로
df = pd.read_csv('../data/scores.csv') # 상대 경로
# print(d)  : 오류

# 조건에 맞는 데이터 추출
# 학생들 중에 1 번 학생만 뽑아오고 싶어요
# Pandas의 DataFrame에 추출할 행에 조건식을 부여할 수 있다.

# df으로 부터 class 컬럼의 속성이 1인지 판별하여 boolean Array
arr_1 = df['class'] == 1 # vector Operation

print(arr_1)    # 1반이면 True 아니면 False
''' 결과     
    0      True
    1      True
    2      True
    3      True
    4      True
    5      True
    6     False
    7     False
    8     False
    9     False
    10    False
    11    False
    Name: class, dtype: bool
'''

class_1 = df[arr_1]

print(class_1)  # 1반 학생들을 출력
''' 결과 
       class    name  kor  eng  mat  bio
    0      1    adam   67   87   90   98
    1      1  andrew   45   45   56   98
    2      1     ben   95   59   96   88
    3      1   clark   65   94   89   98
    4      1     dan   45   65   78   98
    5      1    noel   78   76   98   89
'''


print("-" * 2, '연습1', "-" * 20)
# 연습1) 1반학생의 과목별 평균을 출력해 봅시다.

# 방법1.
class_1ban = df[df['class'] == 1]  # 1반 학생들 추출

print(class_1ban)
''' 결과 
       class    name  kor  eng  mat  bio
    0      1    adam   67   87   90   98
    1      1  andrew   45   45   56   98
    2      1     ben   95   59   96   88
    3      1   clark   65   94   89   98
    4      1     dan   45   65   78   98
    5      1    noel   78   76   98   89
'''

del class_1ban['class']

class_1ban.index = class_1ban['name']
del class_1ban['name']

print(class_1ban)
''' 결과  
            kor  eng  mat  bio
    name                      
    adam     67   87   90   98
    andrew   45   45   56   98
    ben      95   59   96   88
    clark    65   94   89   98
    dan      45   65   78   98
    noel     78   76   98   89
'''

print(class_1ban.mean())    # 데이터 분석에서는 '열', '특성' 을 중요하게 생각!

''' 결과
    kor    65.833333
    eng    71.000000
    mat    84.500000
    bio    94.833333
    dtype: float64
'''

print(class_1ban.mean(axis=1))    # 학생별 평균, '행'으로 평균을 원한다면 axis = 1

''' 결과
    name
    adam      85.50
    andrew    61.00
    ben       84.50
    clark     86.50
    dan       71.50
    noel      85.25
    dtype: float64
'''
# 방법2.

kor_score = np.average(class_1['kor'])
print("1반의 국어점수 평균 : ",kor_score)

eng_score = np.average(class_1['eng'])
print("1반의 영어점수 평균 : ",eng_score)


mat_score = np.average(class_1['mat'])
print("1반의 수학점수 평균 : ",mat_score)


bio_score = np.average(class_1['bio'])
print("1반의 생물점수 평균 : ",bio_score)


print("-" * 2, '연습2', "-" * 20)
# 연습2) 1반 학생들의 국어점수를 막대그래프로 나타내 봅니다.

from matplotlib import font_manager,rc,colors
import matplotlib.pyplot as plt

rc('font',family=font_manager.FontProperties(fname="C:/WINDOWS/Fonts/H2GPRM.TTF").get_name())

plt.bar(range(len(class_1ban.index)),class_1ban['kor'],0.5, color="g")
plt.xticks(range(len(class_1ban.index)),class_1ban.index,color="red")
plt.title("1반학생들의 국어 점수")
plt.show()


print("-" * 2, '연습3', "-" * 20)
# 연습3) 1반 학생들의 전체과목을 그래프로 나타내 봅니다.

# 방법1. 선그래프
class_1ban.plot()
plt.title("1반학생들의 과목별 점수")
plt.show()

# 방법2. 세로막대그래프
class_1ban.plot(kind='bar')
plt.title("1반학생들의 과목별 점수")
plt.show()

# 방법3. 가로그래프
class_1ban.plot(kind='barh')
plt.title("1반학생들의 과목별 점수")
plt.show()

# 방법4. 박스그래프
class_1ban.plot(kind='box')
plt.title("1반학생들의 과목별 점수")
plt.show()

# 방법5.
class_1ban.plot(kind='area')
plt.title("1반학생들의 과목별 점수")
plt.show()


# pandas 라이브러리의 DataFrame이 제공하는 plot 함수에 대한 도움말
help(pd.DataFrame.plot)



