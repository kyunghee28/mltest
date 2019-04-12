#!/usr/bin/env python
# coding: utf-8

# # 주피터 노트북에서 TenserFlow 사용하기
# 
#     - 주피터 노트북에서 TenserFlow 코드를 실행해 봅시다!

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf


# In[6]:


# constant => 상수 만들기
a = tf.constant(100)
b = tf.constant(50)
add_op = a + b

# Variable => 변수 만들기
v = tf.Variable(0)

# app_op 의 연산결과를 transerflow변수 v 에 대입 => assign
let_op = tf.assign(v, add_op) 

# transerflow를 실행하기 위한 session을 생성
sess = tf.Session()

# transerflow변수(Variable)를 실행하기 위해서는 반드시 초기화!!
sess.run(tf.global_variables_initializer())

# let_op 에 지정한 수식 실행하기
sess.run(let_op)

# 연산결과갸 담긴 ranserflow변수(Variable) v 의 내용 출력
print(sess.run(v))


# In[ ]:




