import numpy as np
import pandas as pd
from matplotlib import font_manager,rc,colors
import matplotlib.pyplot as plt

info = pd.read_csv('data/scores.csv')  # 파일 읽어오기

print("-" * 2, '연습1', "-" * 20)
# 연습1 ) scores.scv 파일을 읽어 학생의 이름을 인덱스(key)로 설정하고 이름 칼럼을 삭제하세요

# 학생이름을 인덱스로 설정
info.index = info['name']

# 이름 컬럼 삭제
del info['name']

rc('font',family=font_manager.FontProperties(fname="C:/WINDOWS/Fonts/H2GPRM.TTF").get_name())

print("-" * 2, '연습4', "-" * 20)
# 연습4 ) ben학생의 과목별 점수를 막대그래프로 나타내 봅니다.

sub = ['kor','eng','mat','bio']

plt.subplot(211)
plt.bar(range(len(sub)),info.loc['ben',sub],0.5, color="g")
plt.xticks(range(len(sub)),sub,color="red")
plt.title("ben학생의 과목별 점수")

print("-" * 2, '연습5', "-" * 20)
# 연습8 ) 모든학생의 국어점수를 막대그래프로 나타내 봅니다.

plt.subplot(212)
plt.bar(range(len(info.index)), info["kor"],0.4,color=colors.TABLEAU_COLORS)
plt.xticks(range(len(info.index)),info.index, rotation="45")
plt.title("모든학생의 국어점수")

# 파일로 저장
plt.savefig('student.png')
print("차트 저장성공!")

plt.show()


