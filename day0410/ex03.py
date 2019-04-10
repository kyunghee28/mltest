import numpy as np
import pandas as pd

member = pd.read_csv("../data/member.dat")
print(member)
'''
       id name  age addr
0   tiger  이순신   20   서울
1    lion  강감찬   30   대전
2     cat  유관순   40   울산
3  monkey  홍길동   40   서울
'''
print(member.columns)   # Index(['id', 'name', 'age', 'addr'], dtype='object')

# addr 칼럼과 age칼럼을 각각 one-hot 테이블을 생성,
b_age = pd.get_dummies(member['age'])
print(b_age)
'''
   20  30  40
0   1   0   0
1   0   1   0
2   0   0   1
3   0   0   1
'''

b_addr = pd.get_dummies(member['addr'])
print(b_addr)
'''
   대전  서울  울산
0   0   1   0
1   1   0   0
2   0   0   1
3   0   1   0
'''

#  id 칼럼의 종류만큼 테이블 만들어줌
b_member = pd.get_dummies(member)
print(b_member)
'''
   age  id_cat  id_lion  id_monkey  ...  name_홍길동  addr_대전  addr_서울  addr_울산
0   20       0        0          0  ...         0        0        1        0
1   30       0        1          0  ...         0        1        0        0
2   40       1        0          0  ...         0        0        0        1
3   40       0        0          1  ...         1        0        1        0

[4 rows x 12 columns]
'''
print(b_member.columns)
'''
Index(['age', 'id_cat', 'id_lion', 'id_monkey', 'id_tiger', 'name_강감찬',
       'name_유관순', 'name_이순신', 'name_홍길동', 'addr_대전', 'addr_서울', 'addr_울산'],
      dtype='object')
'''

# pandas 의 get_dummies 는
# 만약 1차원 배열을 매개변수로 받으면 그것이 숫자이던 문자이던 one-hot 인코딩을 해준다.
# 만약 DataFrame 을 매개변수로 받으면 기본적으로 숫자 데이터는 제외하고 one-hot 인코딩을 한다,
# 만약 숫자도 포함하여 one-hot 인코딩을 하려면 DataFrame의 숫자의 속성을 문자로 변경해야 한다.
# 형식 => 데이터프레임['속성명'] = 데이터프레임['속성명'].astype(str)
member['age'] = member['age'].astype(str)
b_member = pd.get_dummies(member)
print(b_member)

print(b_member.columns)