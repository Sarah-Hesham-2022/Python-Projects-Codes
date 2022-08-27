import numpy as np
from PIL import Image
import glob
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split


image_list_Negative = []
image_list_Positive = []
y=[]
X=[]
thresh = 120
maxval = 255

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
X=np.array(X).reshape(40,-1)
for i in range (20):
    y.append(0)
for i in range (20):
    y.append(1)

#Split data into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,shuffle=True)
#This gave me perfect accuracy rate, I have tried different kernels and this is the best one
model=SVC(kernel="linear")
model.fit(X_train,y_train)
y_Pred=model.predict(X_test)
print(accuracy_score(y_test,y_Pred))
#To get the number of support vectors of each class
print(model.n_support_)
#To get the support vectors
print(model.support_vectors_)
#To get the indices of the support vectors
print(model.support_)
print(model.dual_coef_)
print(model.intercept_)

print(y_Pred)