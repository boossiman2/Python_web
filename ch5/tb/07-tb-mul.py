import tensorflow as tf

# 데이터 플로우 그래프 구축하기 --- 1
a = tf.constant(20, name="a")
b = tf.constant(30, name="b")
mul_op = a * b
# 세션 정의하기
sess = tf.Session()
# TensorBoard 사용하기
tw = tf.summary.FileWriter("./tb_dir", graph=sess.graph)
# 세션 실행하기
print(sess.run(mul_op))