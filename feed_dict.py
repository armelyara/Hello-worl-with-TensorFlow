import tensorflow as tf

#Create Operations, Tensors, etc (using the default graph)
a = tf.add(2, 5)
b = tf.multiply(a, 3)

# Start up a 'Session ' using the default graph
#sess = tf.Session()

# Define a dictionnary that says to replace the value of 'a' with 15
with tf.compat.v1.Session() as sess:
	a = tf.add(2, 5)
	b = tf.multiply(a, 3)

	replace_dict = {a:15}

# Run the session, passing in 'replace_dict' as the value to 'feed_dict'

	print (sess.run(b, feed_dict=replace_dict)) #returns 45

# Open Session

#sess = tf.Session

# Run the graph, write summary statistics, etc.
# Close the graph, release its resources
#sess.close()
