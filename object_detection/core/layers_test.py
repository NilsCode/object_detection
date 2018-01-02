import tensorflow as tf
import numpy as np
from layers import area_conv2d11
from layers import create_mask4
from layers import gradient_conv2d411

def area_conv2d11_test():
    images_np = np.array([[[[1111, 1211], [1112, 1212], [1113, 1213]],
                           [[1121, 1221], [1122, 1222], [1123, 1223]],
                           [[1131, 1231], [1132, 1232], [1133, 1233]]],

                          [[[2111, 2211], [2112, 2212], [2113, 2213]],
                           [[2121, 2221], [2122, 2222], [2123, 2223]],
                           [[2131, 2231], [2132, 2232], [2133, 2233]]]])

    images = tf.placeholder(tf.float32, images_np.shape)

    out = area_conv2d11(images, images_np.shape[1:], 6, 'AreaConv2d11')

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        result = sess.run([out],feed_dict={images: images_np})

        print(result[0])
        print(np.array(result[0]).shape)


def create_mask4_test():
    inputs_hwc = [2,2,1]
    print(create_mask4(inputs_hwc))

def gradient_conv2d411_test():
    images_np = np.array([[[[1111, 1211], [1112, 1212], [1113, 1213]],
                           [[1121, 1221], [1122, 1222], [1123, 1223]],
                           [[1131, 1231], [1132, 1232], [1133, 1233]]],

                          [[[2111, 2211], [2112, 2212], [2113, 2213]],
                           [[2121, 2221], [2122, 2222], [2123, 2223]],
                           [[2131, 2231], [2132, 2232], [2133, 2233]]]])

    images = tf.placeholder(tf.float32, images_np.shape)

    outputs = gradient_conv2d411(images, images_np.shape[1:], 6, 'GradientConv2d411')

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        result = sess.run([outputs],feed_dict={images: images_np})

        print(result[0])
        print(np.array(result[0]).shape)


# area_conv2d11_test()
# create_mask4_test()
gradient_conv2d411_test()


