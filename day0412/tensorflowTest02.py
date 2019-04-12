import tensorflow as tf

# tensorflow 에서 사용할 수 있는 상수(변하지 않는 값)을 선언
# a 는 120이외의 다른 값을 가질 수 없다.
# 자바의 문법인 final int a = 120 과 같은 의미
a = tf.constant(120, name="a")
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")

# 변수 선언
v = tf.Variable(0, name="v")

# 데이터 플로우(흐름) 그래프(tensorflow 사용할 수식) 정의
# a+b 먼저하고 출력된 결과를 e 라고 하면 e 와 c 를 더한다 => 이런것을 그래프라고 한다.
calc_op = a + b + c
'''
    위의 수식을 위해서 몇번의 연산이 일어날까요?
    
    a
     +   = e
    b       +   =  calc_op 
           c
    
    위의 같은 모양을 그래프라고 한다.
    위와 같은 수식을 만나면 텐서는 이러한 그래프를 생성.
        => 그래서 "데이터 플로우 그래프" 라 한다.
'''

# 아직 계산을 한 상태는 아님,
# 이런 계산을 할 거라고 계획하는 단계
# 텐서의 Session을 얻고 run을 만나야 실제 계산이 동작!
assign_op = tf.assign(v, calc_op)   # 수식의 결과(calc_op)를 텐서 변수 v 에 대입

# 텐서의 수식(assign_op)를 실행시키기 위해 텐서의 Session 필요
sess = tf.Session()
sess.run(assign_op) # 결과가 텐서 변수 v 에 담긴다.

# v 에 담긴 내용을 실행하여 출력
print(sess.run(assign_op))     # 390

print(sess.run(v))     # 390
print(v)    # <tf.Variable 'v:0' shape=() dtype=int32_ref>
