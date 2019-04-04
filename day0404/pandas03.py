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
# 연습1) henry의 정보를 출력해 봅시다.

# loc 사용
print(df.loc['henry'])
''' 결과 
    class     2
    kor      65
    eng      89
    mat      87
    bio      78
    Name: henry, dtype: int64
'''
print(df.loc['henry'].values)   #   결과 : [ 2 65 89 87 78]

# iloc 사용
print(df.iloc[-1].values)   #   결과 : [ 2 65 89 87 78]


print("-" * 2, '연습2', "-" * 20)
# 연습2) andrew 부터 paul 까지의 정보를 출력해 봅니다.

# [시작 : 끝]  => loc 는 끝이 포함! , iloc는 끝이 포함되지 않음!

# loc 사용
print(df.loc['andrew':'paul'])

# iloc 사용
print(df.iloc[1:7])

'''  결과 
            class  kor  eng  mat  bio
    name                             
    andrew      1   45   45   56   98
    ben         1   95   59   96   88
    clark       1   65   94   89   98
    dan         1   45   65   78   98
    noel        1   78   76   98   89
    paul        2   87   67   65   56
'''

print("-" * 2, '연습3', "-" * 20)
# 연습3) adam, dan, walter 의 정보를 출력해 봅니다.

# 방법 1.
print(df.loc[['adam', 'dan', 'walter']])

# 방법 2. 내가 원하는 정보를 배열에 담아놓고 출력
name = ['adam', 'dan', 'walter']
print(df.loc[name])


''' 결과 
            class  kor  eng  mat  bio
    name                             
    adam        1   67   87   90   98
    dan         1   45   65   78   98
    walter      2   89   98   78   78
'''


print("-" * 2, '연습4', "-" * 20)
# 연습4) 앞에서 5번째 학생들의 국어점수를 출력해 봅니다.

# 방법 1.
print(df.iloc[:5,[1]])

''' 결과 
            kor
    name       
    adam     67
    andrew   45
    ben      95
    clark    65
    dan      45
'''

# 방법 2.
print(df.iloc[:5]['kor'])

# 방법 3.
print(df.loc[:'dan']['kor'])

''' 결과 
    name
    adam      67
    andrew    45
    ben       95
    clark     65
    dan       45
    Name: kor, dtype: int64
'''

print("-" * 2, '연습5', "-" * 20)
# 연습5) 앞에서 5번쨰 학생들의 국어,수학점수를 출력해 봅니다.

# 방법 1.
print(df.iloc[:5, [1, 3]])

# 방법 2.
print(df.iloc[:5][['kor','mat']])

# 방법 3.
print(df.loc[:'dan'][['kor','mat']])

'''  결과 
            kor  mat
    name            
    adam     67   90
    andrew   45   56
    ben      95   96
    clark    65   89
    dan      45   78
'''


print("-" * 2, '연습6', "-" * 20)
# 연습6) adam, dan, walter 의 bio를 제외한 과목의 점수를 출력해 봅니다.


# 방법1. loc 사용
print(df.loc[['adam', 'dan', 'walter'], ['kor', 'eng', 'mat']])

# 방법2. iloc 사용
print(df.iloc[[0, 4, 7], 1:4])

# 방법 3 ~ 4
names = ['adam','dan','walter']
sub = ['kor', 'eng','mat']

# 방법 3.
print(df.loc[name,sub])

# 방법 4.
print(df.loc[name][sub])

# 방법 5.
name = [0,4,7]
print(df.iloc[name, 1:-1])


'''  결과

            kor  eng  mat
    name                 
    adam     67   87   90
    dan      45   65   78
    walter   89   98   78

'''
