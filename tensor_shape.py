import tensorflow as tf

#shapes that specify a 0-D Tensor (scalar)
# e.g any single number: 7, 1, 3, 4, etc.

s_0_list = []
s_0_tuple = ()

#shapes that describes a vector of length 3
# e.g. [1, 2, 3]
s_1 = [3]

#shapes that describes a 3-by-2 matrix
# e.g [[1, 2],
#[3, 4],
#[5, 6]]
s_2 = (3, 2)



# Shape for a vector of any length:
s_1_flex = [None]
#Shape for a matrix that is any amount of rows tall, and 3 columns wide:
s_2_flex =(none, 3)
# Shape of a 3-D Tensor with lenght 2 in its first dimension, and variable-
#lenght in its second and third dimensions:
s_3_flex = [2, None, None]
# Shape that could be any Tensor
s_any = None

# ..create some sort of mystery tensor
# Find the shape of the mystery
tensorshape = tf.shape(mystery_tensor, name="mystery_shape")
print tensorshape


