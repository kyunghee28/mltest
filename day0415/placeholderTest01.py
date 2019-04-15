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
#제일키가 큰키와 제일작은키는 얼마인가요?
print(csv['height'].max(),csv['height'].min())   #200 120
#제일큰몸무게와 제일작은 몸무게는 얼마인가요?
print(csv['weight'].max(),csv['weight'].min())   #80 35

#기계학습 시키기위한 feature들의 값의 범위가 너무커서
#범위를 0~1사이의 값으로 줄이고 싶어요        ==> 정규화
#    =>  데이터를 0 이상 1미만으로 지정하는데,
#           키의 최대값은 200cm, 몸무게의 최대값은 100kg 으로 정규화!

# 키의 제일큰값이 200을 넘지 않아요  그래서 200으로 나누고
csv['height'] = csv['height'] / 200

# 몸무게의 제일큰값은 100을 넘지 않아요 그래요 100으로 나누려고 합니다.
csv['weight'] = csv['weight'] / 100

#값의 범위를 축소시켜 0~1사이의 값들로 만들었습니다.
#제일키가 큰키와 제일작은키는 얼마인가요?
print(csv['height'].max(), csv['height'].min()  )       #1.0 0.6

#제일큰몸무게와 제일작은 몸무게는 얼마인가요?
print(csv['weight'].max(), csv['weight'].min()  )       #0.8 0.35

# 답의 종류를 [1,0,0],[0,1,0],[0,0,1] 형태로 변환(답의 종류에 따른 one-hot 인코딩 값을 정해요.)
bclass = {"thin":[1,0,0],"normal":[0,1,0],"fat":[0,0,1]}

# 그럼, 위에서 계획한 한데로
# 원본데이터의 label에 따라 one-hot 인코딩 테이블을 생성하여
# 새로운 칼럼(label_pat)를 추가 해 봅시다.
csv["label_pat"] = csv["label"].apply(lambda x : np.array(bclass[x]))
print(csv.head())
'''
  height  weight   label  label_pat
0   0.710    0.62     fat  [0, 0, 1]
1   0.710    0.73     fat  [0, 0, 1]
2   0.885    0.61  normal  [0, 1, 0]
'''

# 갖고있는 데이터를 모두 훈련에 참여시키면 훈련된 데이타만 잘 알아 맞추어요.
#  즉 새로운 데이터에 대해서는 잘 못 알아맞춰요  ==> overfit
#  기준이 애매해요..
#   반드시는 아니고 보통은 갖고 데이터의 70~80%를 훈련에 참여시키고
#   나머지 데이터를 갖고 반드시 검증을 해야 합니다.

print(csv.tail())
#        height  weight   label  label_pat
# 19995   0.610    0.58     fat  [0, 0, 1]
# 19996   0.965    0.69  normal  [0, 1, 0]
# 19997   0.965    0.37    thin  [1, 0, 0]
# 19998   0.975    0.51    thin  [1, 0, 0]
# 19999   0.815    0.67  normal  [0, 1, 0]

#전체 데이터의수는 20000건이 있어요
#이중에 3분의 2를 훈련데이터로 3분의 1을 검증데이터로 사용하려고 해요.


# 테스트를 위한 데이터 분류
#   (현재 20000개의 데이터가 있으므로 뒤에있는 5000개의 테이터를 테스트 데이터로 사용)
test_csv = csv[15000:20000]

#검증을 위한 데이터 test_csv로 부터 문제와 답을 나누어요
test_pat = test_csv[["weight","height"]]

print(test_pat.head())
#        weight  height
# 15000    0.55   0.690
# 15001    0.36   0.760
# 15002    0.72   0.915
# 15003    0.51   0.990
# 15004    0.47   0.745

# test_ans = test_csv['label_pat']
# print(type(test_ans))   #<class 'pandas.core.series.Series'>
#       test_csv['label_pat']가 Series라서 list로 형변환 해야 합니다
test_ans = list(test_csv["label_pat"])
print(test_ans[:5])  # [array([0, 0, 1]), array([1, 0, 0]), array([0, 1, 0]), array([1, 0, 0]), array([0, 1, 0])]


# tensorflow를 위한 데이터 플로우 그래프 구축
# 플레이스 홀더 선언하기(값이 여러개인 경우 더 효율적)

#훈련시키기 위한 문제 placeHolder를 만들어요
x = tf.placeholder(tf.float32,[None,2])   # 키와 몸무게 데이타 넣기

#훈련시키기 위한 답 placeHolder를 만들어요
y_ = tf.placeholder(tf.float32,[None,3])   # 정답 레이블 넣기

#변수 선언하기  : 0으로 초기화
#가중치를 위한 배열을 만들어요
#       [feature의 수, 답의 수]
W = tf.Variable(tf.zeros([2,3]))  # W : 가중치(어떤 속성이 얼마나 더 중요할까?)
                                    # 2:피쳐(문제-키,몸무게)수 3:답의 수

# bias(편향)는 만들어요
# 바이어스의 값의 수는 답의 수와 동일하게 해요
# 답의수 3가지 입니다. thin, normal, fat
# 각각의 feature에 각각 weight을 적용한 값이 thin이 되려면 얼마가 넘아야 되는지
# 각각의 feature에 각각 weight을 적용한 값이 normal이 되려면 얼마가 넘아야 되는지
# 각각의 feature에 각각 weight을 적용한 값이 fat이 되려면 얼마가 넘아야 되는지
#   각각에 대한 기준치(임계치)가 3개의값이 필요해요(값의 수만큼 필요)
#   일단 0으로 채워두면 tensor을 학습을 하면서 이것을 알맞은 값을 셋팅을 합니다.
b = tf.Variable(tf.zeros([3]))        # bias 기준치          3:답의 수

# 소프트맥스 회귀 정의하기
#텐서가 제공하는 기계학습을 위한 softmax객체를 생성
#       (모델을 만들어요)
                  # y = wx + b
                  # y = w1x1 + w2x2 + b1 + b2 + b3
# 입력 x 가 있을 때 어떻게 분류하는 것이 좋을지 나타내는 계산 (x : 입력 , W : 가중치 , b : 바이어스)
# 가중치 W 와 바이어스 b는 TensorFlow 변수로 선언 - 모델을 학습하면서 자동으로 조정된다.
y = tf.nn.softmax(tf.matmul(x, W) + b)                          #C

#훈련된 결과와 진짜답과의 거리를 가능하면 작게 만들기 위한 객체를 생성
#모델 훈련하기 - 데이터를 학습할 때는 오차함수(cross_entropy) 활용
# 2개의 확률 분포 사이에서 정의되는 척도, 교차 엔트로피 값이 작을수록 정확한 값을 낸다.
# 예상 레이블 : y , 정답 레이블 : y_
# 진짜답과 예측한 답의 합을 담아요
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))                   #B

# 오차합수가 최소가 되게 학습하는 프로그램 작성 (0.01은 학습 계수)
#그 정답과 예측한 답 사이의 거리를 최소화 되게끔 해주는 개체를 생성 -> GradientDescentOptimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)

#optimzer 객체를 통해 train객체를 생성
#optimer 객체를 통해 훈련
train = optimizer.minimize(cross_entropy)                           #A

# 이 train객체를 텐서를 이용하여 실행시킬텐데
# 이 수식에는 placeHolder가 몇개 있나요??
# A의 수식에 사용된 cross_entropy는 B이며
#   B의 cross_entropy는 y_와 y를 포함한다.
#   y_ 는 진짜답을 답을 placeHolder이며
#   y  훈련을 위한 식이며 즉 훈련된 결과가 담길 변수이다.
#           이식에 문제가 담길 placeHolder x가 포함된다.
#   그래서 tensor에서 실행시길때
#           y_와 x에 해당하는 값을 설정해야 합니다.


#훈련시키는 과정에서 정확도를 확인하기 위한 수식  ==> 정답률 구하기

#예측한 답과 진짜답을 비교하여 predict배열에 담아요
predict = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))

#예측한 답과 진짭을 비교한 predict는 boolean 배열인데
#이것을 실수형으로 변환하여 평균값을 얻어요
accuracy = tf.reduce_mean(tf.cast(predict,tf.float32))

#세션 시작하기
sess = tf.Session()
sess.run(tf.global_variables_initializer()) #변수 초기화


#학습시키기
# 원본데이터 20000개 중에 검증용 데이터 15000~20000를 제외한 모든 데이터를 훈련
# 15000개를 한꺼번에 훈련시키기 않고 100개씩 끊어서 훈련

# W 와 b를 알고자 하는 것이 목적
# 각 feature 마다 가중치가 얼마인지, 각 feature 마다 bias는 얼마인지
for step in range(3500):
    i = (step * 100) % 14000
    # i는 0, 100, 200 ~  14900

    # i번째 부터 100개씩 뽑아와요
    rows = csv[1 + i : 1 + i +100]

    # 문제와 답을 분리해요
    x_pat = rows[["weight","height"]]
    y_ans = list(rows["label_pat"])

    #훈련객체 train에 사용된 placeHolder에 적용할 새로운 객체를 만들기
    fd = {x:x_pat, y_:y_ans}

    sess.run(train,feed_dict=fd)

    if step % 500 == 0:
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


# 1) 데이터(174,46,thin)를 넣어 테스트

# 위의 학습결과로 부터 학습된 W 와 b 를 변수에 담기.
W1 = sess.run(W)
print(W1)
'''
[[-17.602276     0.83813375  16.764153  ]
 [ 21.7983       1.179182   -22.977499  ]]
'''

b1 = (sess.run(b))
print(b1)  # [-7.9854293 -0.3871097  8.37257  ]

# 알고자 하는 사람의 몸무게와 키를 다음과 같이 정규화
# 학습한 x 가 0 ~1 사이의 범위이므로 알고자 하는 데이터도 같게 만든다.
# 데이터를 훈련시킬때 몸무게, 키 순으로 훈련시켰으므로 몸무게 키 순으로 작성
x1 = np.array([[46 / 100,174 / 200]],np.float32)

#알고자 하는 식을 만들어요 ==> y = wx + b
# W와 b에는 각각 학습된 최적의 W와 b를 적용
# 행렬곱을 위하여 텐서의 matmul함수를 이용.
y1 = tf.matmul(x1,W1) + b1

# 예측한 결과 y1을 one-hot 인코딩으로 만들어 어디에 불이 들어왔는지 확인
#thin이면 0번째 불이 들어온다 -> 1 0 0   ==> 0을 반환
#normal이면 1번째 불이 들어온다 -> 0 1 0   ==> 1을 반환
#fat이면 2번째 불이 들어온다 -> 0 0 1   ==> 2를 반환
'''
# 174,69,normal     010     1
# 173,35,thin       100     0
# 136,53,fat        001     2
# 189,79,normal     010     1
# 139,78,fat        001     2
'''
predict1 = tf.argmax(y1,1)

print(sess.run(predict1))   # [0]

sess.close()
