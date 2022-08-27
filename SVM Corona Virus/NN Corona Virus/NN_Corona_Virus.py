from keras import activations
import tensorflow as tf #I am importing tensorflow to use keras in my model
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
import pandas as pd
from sklearn.model_selection import train_test_split #for splitting our data
from keras.models import Sequential
from keras.layers import Dense


image_list_Negative = []
image_list_Positive = []
y=[]
X=[]
thresh = 120
maxval = 255

#Let us binarize, prepare and loop on our 40 different images.jpg of patients and store them in a numpy array

for filename in glob.glob(r"C:\Users\Sarah Hesham\OneDrive\Documents\PycharmProjects\Lab Neural Network\Negative/*.jpg"):
    im=Image.open(filename)
    im_gray=np.array((im).convert('L'))
    im_bin = (im_gray > thresh) * maxval
    image_list_Negative.append(im_bin)
    Image.fromarray(np.uint8(im_bin)).save("bin.jpg")

for filename in glob.glob(r"C:\Users\Sarah Hesham\OneDrive\Documents\PycharmProjects\Lab Neural Network\Positive/*.jpg"):
    im=Image.open(filename)
    im_gray2=(np.array((im).convert('L')))
    im_bin = (im_gray2 > thresh) * maxval
    image_list_Positive.append(im_bin)
    Image.fromarray(np.uint8(im_bin)).save("bin.jpg")

X=image_list_Negative+image_list_Positive

#This is a very important step ;to reshape your data to fit our output
X=np.array(X).reshape(40,-1)

for i in range (20):
    y.append(0)
for i in range (20):
    y.append(1)

#Split data into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,shuffle=True)

#Build the model
#Building the neural network requires configuring the layers of the model,
#Set up the layers
model = Sequential()
model.add(Dense(128, activation='relu'))
model.add(Dense(2))

# then compiling the model.
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

#This step I did not do it in SVM we only need to convert the y to a numpy array due to keras needs
y_train = np.array(y_train)
#Feed the model
model.fit(X_train, y_train, epochs=15)

#This step I did not do it in SVM we only need to convert the y to a numpy array due to keras needs
y_test = np.array(y_test)

#Let us evaluate the model
test_loss, test_acc = model.evaluate(X_test,  y_test, verbose=2)
print('\nTest accuracy:', test_acc)

#Make Predictions
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(X_test)

print("The predicted: \n\n",predictions)
print("The actual:\n\n",y_test)

#This is a value our model is confident of, let us test it
print(np.argmax(predictions[0]))
print(y_test[0])