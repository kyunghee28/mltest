# 합치고자 하는 두개의 파일에 데이터 수가 일치하지 않아요
# dan 학생의 점수정보는 없다.

import numpy as np
import pandas as pd

# 서로 일치하지 않는 데이터 dan의 정보도 나타내 봅니다.
# 			그 학생의 정보는 0으로 출력합니다.
# help(pd.merge)

df1 = pd.read_csv('../data/stu01', sep="::", engine='python')
df2 = pd.read_csv('../data/stu02', sep="::", engine='python')

df = pd.merge(df1,df2, how="outer")
df.fillna(0, inplace=True)    # 결측치를 0으로 채워줘!

print(df)

