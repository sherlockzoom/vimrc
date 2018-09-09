from keras import backend as K
from keras.engine.topolopy import Layer
import numpy as np

class MyLayer(Layer):
    def __init__(self, output_dim, **kwargs):
        self.output_dim = output_dim
        supper(MyLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        self.kernel = self.add_weight(name="kernel",
                                      shape=(input_shape[1], self.output_dim),
                                      initializer='uniform',
                                      traninable=True)
        super(MyLayer, self).build(input_shape)

    def call(self, x):
        return K.dot(x, self.kernel)

    def compute_output_shape(self, input_shape):
        return (input_shape[0], self.output_dim)
