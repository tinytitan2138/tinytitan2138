import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist

# 80 to 90 percent of data given for training, the rest is testing
# all images are arrays of 28x28 pixels
(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images/255.0
test_images = test_images/255.0
# representation is now from 0 to 1 instead of 0 to 255, makes data easier to work with


# print(train_labels[0])

#plt.imshow(train_images[0], cmap=plt.cm.binary)
#plt.show()

# model keras sequential allows for the archictexure to be made, as a sequence, thus is sequential
# Flatten alows for the input shape, 28, 28 allows for 28 x 28 = 784 nuerons
# Dense layer, contains nuerons all interconnected, just like the models drawn, activation is activation function
# softmax allows for probability of 1 or 0 for choice of output




model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam", loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=["accuracy"])
# metrics define that we look at accuracy, to get loss function to 0
model.fit(train_images, train_labels, epochs=5)
# epoch is training iteration, that change order of input to further optimize
# most of the keyword arguments are to be tweaked

test_loss, test_acc = model.evaluate(test_images, test_labels)

print("Tested Acc: ", test_acc)

prediction = model.predict([test_images])

for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel("Actual: " + class_names[test_labels[i]])
    plt.title("Prediction: " + class_names[np.argmax(prediction[i])])
    plt.show()



#print(class_names[np.argmax(prediction[0])])
# outputs 10 different values, due to 10 output nuerons
# prediction gives 10 probabilities, np.argmax returns index with highest probability
# class_names[i] gives the i'th elements, which is prediction
