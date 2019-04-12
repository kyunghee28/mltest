# tensorflow 읽어 들이기
import tensorflow as tf

# 상수 선언하기 -> constant : 상수 만들기
a = tf.constant(2)  # a 는 2 이외에 다른 값을 가질 수 없음
b = tf.constant(3)
c = tf.constant(4)

# 연산 정의
calc1_op = a + b * c
# print(calc1_op)    # Tensor("add:0", shape=(), dtype=int32)
    # ->  tensorflow의 상수나 변수의 수식의 결과는 바로 알 수 없고
    #      tensorflow의 실행환경에서 실행시키고 결과를 확인 할 수 있다.

calc2_op = (a + b) * c

# 세션 시작하기
sess = tf.Session()
res1 = sess.run(calc1_op)   # run() 메소드로 계산
res2 = sess.run(calc2_op)

# tensorflow의 스테이지를 열어서 결과를 확인할 수 있다!!
print(res1) # 14
print(res2) # 20
