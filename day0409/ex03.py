import numpy as np
import pandas as pd

f = open('../data/i_have_a_dream.txt')
data = f.read()
# print(data)

import matplotlib.pyplot as plt
from wordcloud import WordCloud

colud1 = WordCloud().generate(data)
# print(colud1)   #   <wordcloud.wordcloud.WordCloud object at 0x0000000002987A20>
# print(type(colud1)) #<class 'wordcloud.wordcloud.WordCloud'>

plt.imshow(colud1)  # 워드클라우드 객체에 해당하는 이미지 생성

#  워드클라우드에선 차트의 축을 없애는 것이 보기 좋음
plt.axis("off")     #  차트의 x , y 축을 없애 주세요
plt.show()  # 워드클라우드를 보여주세요

