import tensorflow as tf

# 크가가 상관없응 정수형 1차원 배열의 placeholder 를 만들고
# 				이것의 *2 한 결과를 tensor를 이용하여 출력해 봅시다.

# 크기가 정해지지 않는 1차원 배열에 placeholder 만들기
#     ex. 2차원 배열일 경우 [None][None]
arr = tf.placeholder(tf.int32, [None])

# arr의 *2 한 수식 만들기

# 2를 직접 표현하지 않고 tensorflow 의 상수로!!
b =tf.constant(2)

# 위의 상수를 이용하여 수식 만들기
x_op = arr * b

# Session 을 얻어와 위의 수식을 실행
# 실행 시킬 땐 placeholder 의 값을 지정해야 한다1!
sess = tf.Session()

r1 = sess.run(x_op, feed_dict={ arr:[1,2,3,4,5,6] })    # 딕셔너리 상태로 적용
print(r1)   # 결과 :  [ 2  4  6  8 10 12]

r2 = sess.run(x_op, feed_dict={ arr:[10,20] })
print(r2)   # 결과 : [20 40]

row = [4,5,-2,9]
r3 = sess.run(x_op, feed_dict={ arr:row })
print(r3)   # 결과 : [ 8 10 -4 18]


