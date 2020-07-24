import tensorflow as tf

init_val = tf.random.normal((1,5),0,1)
var = tf.Variable(init_val, name='var')
print ("pre run: \n{}".format(var))

#init = tf.compat.v1.global_variables_initializer()
#with tf.compat.v1.Session() as sess:

#	sess.run(init)
#	init_val = tf.random.normal((1,5),0,1)
 #       var = tf.Variable(init_val, name='var')

#	post_var = sess.run(var)

#print ("\npost run: \n{}".format(post_var))
