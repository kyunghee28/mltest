import tensorflow as tf
import numpy as np
import pandas as pd

# 1) 위의 데이터를 넣어 테스트를 해 보도록 합시다.
# 2) 사용자로부터 키와 몸무게를 입력받아 마른정도(thin, normal, fat) 를 출력하는 웹어플리케이션을 작성합시다,

f = pd.read_csv("bmi.csv")
