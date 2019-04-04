# 숙제)2016_GDP.txt 파일을 읽어 들여 상위 10개의 나라를 막대그래프로 그려주세요
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager,rc

                                # r : 읽기용도
f = open('Data/2016_GDP.txt','r',encoding="UTF-8")
r = f.readline() # 순위:국가:미 달러($) ->  파일의 첫 번째 줄을 읽어 출력
list = f.readlines() # readlines - 파일을 모두 읽어줘.
# print(list)  -> 결과 : ['1:룩셈부르크:101,715\n', '2:스위스:78,245\n', '3:노르웨

# 나라이름과 GDP를 추출
name = []
money = []
for row in list:
    row = row.split(":") # : 으로 분리한 리스트 만듬,.-> ['1', '룩셈부르크', '101,715\n'] 으로 나옴.
    name.append(row[1])
    money.append(row[2].strip().replace(",","")) # strip 는 \n(개행문자)를 없애 달라는 것임.

name = np.array(name)
money = np.array(money, dtype='int32')

# 한글 글꼴 설정 - 차트 그리기전
rc('font',family=font_manager.FontProperties(fname="C:/WINDOWS/Fonts/H2GPRM.TTF").get_name())

plt.bar(name[:10],money[:10])
plt.xticks(name[:10],name[:10], rotation="90") # rotation="90" : x축에 국가 이름들이 세로로 출력된다.
        # ( 축이 몇개인지, 축에 들어갈 이름, 축의 이름의 각도)
plt.xlabel("국가이름")
plt.ylabel("GDP")
plt.title("2016년 GDP TOP10")
plt.show()

