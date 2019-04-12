'''
placeholder 란,
    마치 데이터베이스의 PrepareStatment 처럼 질의문에 ? 를 생각하면 된다.
    사용자가 입력한 값을 질의문에 대응시키기 위하여 ? 를 대신하듯이
    어떤 수식에 대응시키기 위한 변수의 틀을 미리 만들어 두는 개념.
    
    예를 들어, 다음의 수식을 보면 
        a = [1,2,3]
        b = a * 2
        b 는 정해진 배열 [1,2,3] * 2 만 할 줄 안다.
        
    만약, 어떤요소와 배열이라도 연산시키고자 한다면 위와 같이 값을 구체화 하지 않고 
        3개 짜리 배열이라고 틀을 만들어 두면 어떤 요소의 배열이라도 연산 시킬 수 있다.
'''

import tensorflow as tf

# 어떤 값이라도 담을 수 있는 정수형 3개를 담을 수 있는 placeholder 정의
# placeholder 이름은 a 라고 지정
a = tf.placeholder(tf.int32, [3])   # 32비트 정수 자료형 3개를 가진 배열

# 위에서 만든 placeholder 가 사용되는 수식(데이터 플로우 그래프) 만들기
b =tf.constant(2)   # 상수 정의
x_op = a * b       # 배열의 모든 값을 2배한는 연산 정의

# 위의 수식 실행
# tensorflow 의 Session 을 얻어옴
sess = tf.Session()

# 위의 수식 x_op 실행
# x_op 엔 결정되지 않은 값 (placeholder) 를 갖고 있기 때문에
# placeholder 의 값을 설정해 줘야 한다.  => feed_dict={ key-placeholder 이름: value }
r1 = sess.run(x_op, feed_dict={ a:[1,2,3] })   # a 에 [1,2,3] 을 적용 시켜주세요
print(r1)   # 결과 : [2 4 6]

r2 = sess.run(x_op, feed_dict={ a:[10,20,30] })
print(r2)    # 결과 : [20 40 60]

row = [4,5,6]
r3 = sess.run(x_op, feed_dict={ a:row })
print(r3)    # 결과 : [ 8 10 12]

