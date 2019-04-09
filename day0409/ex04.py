# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import font_manager,rc
# from wordcloud import WordCloud

#예제. 문재인 대통령 연설문을 워드 클라우드로 표현해봅시다.
# f = open('../data/moon.txt', 'r' ,encoding='UTF-8')
# data = f.read()
# # print(data)
#
# font = 'C:/Windows/Fonts/DXKPMB-KSCpc-EUC-H.ttf'
# speech = WordCloud(font_path = font, background_color='white', width=800, height=600).generate(data)
# rc("font",family=font_manager.FontProperties(fname=font).get_name())
# plt.imshow(speech)
# plt.title("문재인 대통령 연설문")
# plt.axis("off")
# plt.show()

# 위의 연설문에서 데이터 분석에 의미 없는 단어를 모두 제거하고 다시 워드클라우드로 표현

# f = open('../data/moon.txt', 'r' ,encoding='UTF-8')
# data = f.read()
#
# delWord = ['것입니다','합니다','위해','있도록','우리의','있습니다','모든','국민여러분','우리','우리가','표준이','비롯한']
# for dw in delWord:
#     data = data.replace(dw,'')
# # print(data)
#
# font = 'C:/Windows/Fonts/DXKPMB-KSCpc-EUC-H.ttf'
# speech = WordCloud(font_path = font, background_color='white', width=800, height=600).generate(data)
# rc("font",family=font_manager.FontProperties(fname=font).get_name())
# plt.imshow(speech)
# plt.title("문재인 대통령 연설문")
# plt.axis("off")
# plt.show()

# 예제. 단어별 빈도수를 먼저 파악하고 빈도수별 내림차순 정렬하여 필요없는 단어를 파악.
# help(WordCloud.process_text)
# f = open('../data/moon.txt', 'r' ,encoding='UTF-8')
# data = f.read()
#
# # 단어별 빈도수 파악
# cloud = WordCloud(font_path='C:/Windows/Fonts/DXKPMB-KSCpc-EUC-H.ttf')
# # wordcnt = cloud.process_text(data)
#
# delWord = ['것입니다','있습니다','표준이','모든','국민 여러분','있도록','위해','합니다','우리의'
#            ,'정부와','향한','우리가','더욱','우리',"있는"]
# for dw in delWord:
#     data = data.replace(dw,'')
#
# font = 'C:/Windows/Fonts/DXKPMB-KSCpc-EUC-H.ttf'
# speech = WordCloud(font_path = font, background_color='white', width=800, height=600).generate(data)
#
# # 빈도수를 알려줌.
# print(speech.words_)    # {'5G': 1.0, '세계': 0.5294117647058824, '새로운': 0.29411764705882354, '5G는': 0.23529411764705882, ...
#
# rc("font",family=font_manager.FontProperties(fname=font).get_name())
# plt.imshow(speech)
# plt.title("문재인 대통령 연설문")
# plt.axis("off")
# plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
from wordcloud import WordCloud
from PIL import Image

# 이미지 기반으로 mask 만들기
font_mask = np.array(Image.open("../data/world_map.png"))

font = 'C:/Windows/Fonts/DXKPMB-KSCpc-EUC-H.ttf'
cloud =  WordCloud(font_path = font, mask = font_mask ,
                   background_color='white', stopwords='세계지도')

f = open('../data/moon.txt', 'r' ,encoding='UTF-8')
data = f.read()

word_count = cloud.process_text(data)

delWord = ['것입니다','있습니다','표준이','모든','국민 여러분','있도록','위해','합니다','우리의'
           ,'정부와','향한','우리가','더욱','우리',"있는"]
for dw in delWord:
    data = data.replace(dw,'')

speech = WordCloud(font_path = font, background_color='white', width=800, height=600,mask = font_mask ).generate(data)

rc("font",family=font_manager.FontProperties(fname=font).get_name())
plt.imshow(speech)
plt.title("문재인 대통령 연설문")
plt.axis("off")
plt.show()