import pandas as pd
import numpy as np
import tensorflow as tf

csv = pd.read_csv("../data/bmi.csv")
print(csv)

'''       height  weight   label
0         142      62     fat
1         142      73     fat
        ...
19999     163      67  normal

[20000 rows x 3 columns]
'''

# 학습시키기 위하여 label의 종류 3가지를 (fat, normal,thin) one - hot Encoding
print(csv['height'].max(),csv['height'].min())   #200 120
print(csv['weight'].max(),csv['weight'].min())   #80 35

#키와 몸무게 기본값들이 170,57 등 값의 부피가 크므로
# 정규화 ( 값의 범위를 0 ~ 1 사이값으로 줄인다)
#    =>  데이터를 0 이상 1미만으로 지정하는데,
#           키의 최대값은 200cm, 몸무게의 최대값은 100kg 으로 정규화!
print(csv['height'])
'''
0        142
1        142
    ...
19999    163
Name: height, Length: 20000, dtype: int64
'''
csv['height'] = csv['height'] / 200        # 키의 최대값이 200
print(csv['height'])
'''
0        0.710
1        0.710
    ...
19999    0.815
Name: height, Length: 20000, dtype: float64
'''

csv['weight'] = csv['weight'] / 100       # 몸무게가 최대값이 80을 넘지 않기 때문

# print(csv['height'].max(),csv['height'].min())   #1.0    0.6
# print(csv['weight'].max(),csv['weight'].min())   #0.8    0.35

# 답의 종류(thin, normal, fat)를 직접 [1,0,0],[0,1,0],[0,0,1] 형태로 변환
bclass = {"thin":[1,0,0],"normal":[0,1,0],"fat":[0,0,1]}
csv["label_pat"] = csv["label"].apply(lambda x : np.array(bclass[x]))
print(csv)
'''
       height  weight   label  label_pat
0       0.710    0.62     fat  [0, 0, 1]
1       0.710    0.73     fat  [0, 0, 1]
            ...
19999   0.815    0.67  normal  [0, 1, 0]
[20000 rows x 4 columns]          
'''

# 테스트를 위한 데이터 분류
#   (현재 20000개의 데이터가 있으므로 뒤에있는 5000개의 테이터를 테스트 데이터로 사용)
test_csv = csv[15000:20000]
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])

# tensorflow를 위한 데이터 플로우 그래프 구축
# 플레이스 홀더 선언하기
x = tf.placeholder(tf.float32,[None,2])   # 키와 몸무게 데이타 넣기
y_ = tf.placeholder(tf.float32,[None,3])   # 정답 레이블 넣기

#변수 선언하기  : 0으로 초기화
W = tf.Variable(tf.zeros([2,3]))      # W : 가중치  2:피쳐수 3:답의 수
b = tf.Variable(tf.zeros([3]))        # bias 기준치          3:답의 수

# 소프트맥스 회귀 정의하기 (자동으로 가중치와 기준치를 만든다.)
# 입력 x 가 있을 때 어떻게 분류하는 것이 좋을지 나타내는 계산
# x : 입력 , W : 가중치 , b : 바이어스
# 가중치 W 와 바이어스 b는 TensorFlow 변수로 선언 - 모델을 학습하면서 자동으로 조정된다.
y = tf.nn.softmax(tf.matmul(x, W) + b)

#모델 훈련하기 - 데이터를 학습할 때는 오차함수(cross_entropy) 활용
# 2개의 확률 분포 사이에서 정의되는 척도, 교차 엔트로피 값이 작을수록 정확한 값을 낸다.
# 예상 레이블 : y , 정답 레이블 : y_
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# 오차합수가 최소가 되게 학습하는 프로그램 작성 (0.01은 학습 계수)
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(cross_entropy)

#정답률 구하기
predict = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(predict,tf.float32))

#세션 시작하기
sess = tf.Session()
sess.run(tf.global_variables_initializer()) #변수 초기화

#학습시키기 (100개식 3500번 학습)
for step in range(3500):
    i = (step * 100) % 14000
    rows = csv[1 + i : 1 + i +100]
    x_pat = rows[["weight","height"]]
    y_ans = list(rows["label_pat"])
    fd = {x:x_pat, y_:y_ans}
    sess.run(train,feed_dict=fd)
    if step % 500 ==0:
        cre = sess.run(cross_entropy, feed_dict=fd)
        acc = sess.run(accuracy, feed_dict={x:test_pat,y_:test_ans})
        print("step=",step,"cre=",cre,"acc=",acc)
        '''
        step= 0 cre= 108.66269 acc= 0.3242
        step= 500 cre= 57.58866 acc= 0.8904
        step= 1000 cre= 45.02092 acc= 0.898
        step= 1500 cre= 41.654335 acc= 0.9566
        step= 2000 cre= 34.66403 acc= 0.943
        step= 2500 cre= 34.287025 acc= 0.9674
        step= 3000 cre= 26.880764 acc= 0.9726
        
        '''

# 최종적인 정답률 구하기
acc = sess.run(accuracy, feed_dict={x:test_pat,y_:test_ans})
print("정답률=",acc)   # 정답률= 0.9712


# 1) 데이터(174,46,thin)를 넣어 테스트를 해 보도록 합시다.

# 2) 사용자로부터 키와 몸무게를 입력받아 마른정도(thin, normal, fat) 를 출력하는 웹어플리케이션을 작성합시다,
