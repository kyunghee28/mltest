# 연습 1. baseball.txt파일을 DataFrame으로 읽어들입니다.

# 연습 2. 팀별로 우승한 횟수를 출력해 봅니다.
import numpy as np
import pandas as pd

df = pd.read_csv('../world-series/baseball.txt')
# print(df.columns)   # Index(['Year', 'Champion', 'Wins', 'Losses', 'Ties', 'WinRatio'], dtype='object')

Champion_cnt = df.pivot_table(values='Wins', index='Champion', aggfunc='count')    # pivot_table : ~ 별로

Champion_cnt = Champion_cnt.sort_values(by='Wins', ascending='True')

print(Champion_cnt)
