import seaborn as sns
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

print(tf.__version__)

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

sns.countplot(x=y_train)
plt.show()

print("Any NaN training", np.isnan(x_train).any())
print("Any NaN testing", np.isnan(x_test).any())

#Tell what shape to expect
input_shape = (28, 28, 1) #28x28 pixels 1 color

x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
x_train = x_train/255.0 

x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)
x_test = x_test/255.0 

#one_hot not sparce
y_train = tf.one_hot(y_train.astype(np.int32), depth = 10)
y_test = tf.one_hot(y_test.astype(np.int32), depth = 10)

#Example image from MNIST
plt.imshow(x_train[100][:,:,0])
plt.show()


batch_size = 128
num_classes = 10
epochs = 5

#Build the model
model = tf.karas.models.sequential(
    [
    tf.karas.layers.Conv2D(32, (5,5), padding='same', activation='relu', input_shape=input_shape),
    tf.karas.layers.Conv2D(32, (3,3), padding='same', activation='relu', input_shape=input_shape),
    tf.karas.layers.maxpool2D(),
    tf.karas.layers.dropout[0,25],
    tf.karas.layers.Conv2D(64, (3,3), padding='same', activation='relu', input_shape=input_shape),
    tf.karas.layers.Conv2D(64, (3,3), padding='same', activation='relu', input_shape=input_shape),
    tf.karas.layers.Dense(num_classes, activation='sotmax')

    ]
)

model.comp(optimizer=)