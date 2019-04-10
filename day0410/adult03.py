import numpy as np
import pandas as pd

names = ['age','workclass','fnlwgt','education','education-num','marital-status',
         'occupation','relationship','race','sex','capital-gain','capital-loss',
         'hours-per-week','native-country','income']

data = pd.read_csv('../data/adult.data.txt' ,header=None, names=names)

data = data[['age','workclass','education','sex','hours-per-week','occupation','income']]

# 예제1. 50000달러 이상인 사람은 모두 몇명인가요

income_1 = data[data['income'] == ' >50K']
print(len(income_1),'명')  # 7841 명

# 예제2. 여자중에 50000달러 이상인 사람은 모두 몇명인가요

gender = data[data['sex'] == ' Female']
# print(gender)

income_2 = gender[gender['income'] == ' >50K']
print(len(income_2),'명')  # 1179 명

# 예제3. 50000달러 이상인 사람들의 평균나이는 몇살인가요

income_3 = data[data['income'] == ' >50K']
print(income_3['age'].mean())   # 44.24984058155847

# 예제4. 가장 많은 직업군은 무엇인가요

many_job = data.pivot_table(values='age', index='occupation', aggfunc='count').sort_values(by='age', ascending=False)

print(many_job[:1])
print(many_job.head(1))

'''
                  age
occupation           
 Prof-specialty  4140
'''

# 예제5. 가장 많은 학력은 무엇인가요

many_edu = data.pivot_table(values='age', index='education', aggfunc='count').sort_values(by='age', ascending=False)

print(many_edu[:1])
print(many_edu.head(1))
'''
             age
education       
 HS-grad   10501
'''

# 예제6. 5000달러 이상인 직업중에 주당 일하는 시간이 가장 적은 직업군 top5은 무엇인가요

income_4 = data[data['income'] == ' >50K']
less_time = income_4.pivot_table(values='hours-per-week', index='occupation', aggfunc='mean')
less_time_income = less_time.sort_values(by='hours-per-week')

print(less_time_income[:5])
print(less_time_income.head(5))

'''
                  hours-per-week
occupation                      
 Priv-house-serv       35.000000
 ?                     36.146597
 Armed-Forces          40.000000
 Adm-clerical          40.942801
 Tech-support          41.427562

'''
