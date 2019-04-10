# 연습 1. baseball.txt파일을 DataFrame으로 읽어들입니다.

# 연습 2. 팀별로 우승한 횟수를 출력해 봅니다.

import numpy as np
import pandas as pd

df = pd.read_csv('../world-series/baseball.txt')
print(df)
# print(df.columns)   # Index(['Year', 'Champion', 'Wins', 'Losses', 'Ties', 'WinRatio'], dtype='object')

b = df.pivot_table(values='Wins', index='Champion', aggfunc='count')

print(b)

