# Imports
import numpy as np
import keras
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.preprocessing.text import Tokenizer
from time import time
import matplotlib.pyplot as plt
# %matplotlib inline

np.random.seed(42)


# Loading the data (it's preloaded in Keras)
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=1000)

print(x_train.shape)
print(x_test.shape)

# One-hot encoding the output into vector mode, each of length 1000
tokenizer = Tokenizer(num_words=1000)
x_train = tokenizer.sequences_to_matrix(x_train, mode='binary')
x_test = tokenizer.sequences_to_matrix(x_test, mode='binary')
print(x_train[0])


# One-hot encoding the output
num_classes = 2
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
print(y_train.shape)
print(y_test.shape)


# DONE: Build the model architecture
model = Sequential()
model.add(Dense(2, input_dim=x_train.shape[1]))
model.add(Activation('sigmoid'))

# DONE: Compile the model using a loss function and an optimizer.
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])
model.summary()


# DONE: Run the model. Feel free to experiment with different batch sizes
# and number of epochs.
start = time()
model.fit(x_train, y_train, epochs=5, batch_size=10)
print(time() - start)

# Dense(16/2), words: 100,  Epochs: 100, batch_size: 10, time: 546, accuracy: 71%
# Dense(16/2), words: 100,  Epochs: 200, batch_size: 10, time: 1272
# Dense(16/2), words: 1000, Epochs: 20,  batch_size:  5, time: 324, accuracy: 0.83
# Dense(16/2), words: 1000, Epochs: 20,  batch_size: 50,  time: 27,  accuracy: 0.85
# Dense(16/2), words: 1000, Epochs: 30,  batch_size: 50,  time: 41,  accuracy: 0.8526
# Dense(4/2), words: 1000, Epochs: 30, batch_size: 50,  time: 41, accuracy 0.8566
# Dense(4), words: 1000, Epochs: 30, batch_size: 50, time: 41, accuracy 0.8566


# This will give you the accuracy of the model, as evaluated on the
# testing set. Can you get something over 85%?
score = model.evaluate(x_test, y_test, verbose=0)
print("Accuracy: ", score[1])
