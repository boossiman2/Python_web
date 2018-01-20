import tensorflow as tf
# 플레이스홀더 정의하기
a = tf.placeholder(tf.int32, [None]) # 배열의 크기를 None로 지정
# 배열의 모든 값을 10배하는 연산 정의하기
b = tf.constant(10)
calc_mul = a * b
# 세션 시작하기
sess = tf.Session()
# 플레이스홀더에 값을 넣어 실행하기
r1 = sess.run(calc_mul, feed_dict={a:[1,2,3,4,5]})
print(r1)
r2 = sess.run(calc_mul, feed_dict={a:[10, 20]})
print(r2)