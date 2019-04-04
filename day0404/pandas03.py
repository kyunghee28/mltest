import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
    pandas의 DataFrame에서 행에 접근할 때 loc 이나 iloc 함수를 이용해 행에 접근 가능

    1. key 값을 부여하지 않았는데 행에 접근하려면 index로 접근.(이 때는 loc 이나 iloc 에 차이가 없다.)

    2. key값을 부여했을 때는
        index로 접근할 때는 iloc을 쓰고
        key로 접근할 땐 loc 을 사용
'''

df = pd.read_csv('./data/scores.csv')

# 학생의 이름을 키로 설정
df.index = df['name']
print(df)
''' 결과 
            class    name  kor  eng  mat  bio
    name                                     
    adam        1    adam   67   87   90   98
    andrew      1  andrew   45   45   56   98
    ben         1     ben   95   59   96   88
            ''
    henry       2   henry   65   89   87   78
'''

# 데이터 프레임에서 name 칼럼은 삭제
del df['name']
print(df)
''' 결과 
                class  kor  eng  mat  bio
    name                             
    adam        1   67   87   90   98
    andrew      1   45   45   56   98
    ben         1   95   59   96   88
            ''
    henry       2   65   89   87   78
'''

print("-" * 2, '연습1', "-" * 20)
# 연습1) henry의 정보를 출력해 봅시다.(loc, iloc 다 사용)

# loc 사용
print(df.loc['henry'])
print(df.loc['henry'].values)

# iloc 사용
print(df.iloc[-1].values)

print("-" * 2, '연습2', "-" * 20)
# 연습2) andrew 부터 paul 까지의 정보를 출력해 봅니다.

print(df.loc['andrew':'paul'])

print("-" * 2, '연습3', "-" * 20)
# 연습3) adam, dan, walter 의 정보를 출력해 봅니다.

print(df.loc[['adam', 'dan', 'walter']])

print("-" * 2, '연습4', "-" * 20)
# 연습4) 앞에서 5번째 학생들의 국어점수를 출력해 봅니다.

print(df.iloc[:5, [1]])

print("-" * 2, '연습5', "-" * 20)
# 연습5) 앞에서 5번쨰 학생들의 국어,수학점수를 출력해 봅니다.

print(df.iloc[:5, [1, 3]])

print("-" * 2, '연습6', "-" * 20)
# 연습6) adam, dan, walter 의 bio를 제외한 과목의 점수를 출력해 봅니다.

print(df.loc[['adam', 'dan', 'walter'], ['kor', 'eng', 'mat']])
print(df.iloc[[0, 4, 7], 1:4])
