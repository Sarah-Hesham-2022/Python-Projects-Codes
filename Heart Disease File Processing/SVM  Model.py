#Importing the dataset
#import pandas as pd
#data = pd.read_excel("Sheet Numerical Data.xlsx")
#data.to_csv("Sheet Numerical Data.csv")

import pandas as pd
data = pd.read_csv("Sheet Numerical Data.csv")

#Splitting the dataset into training and test samples
from sklearn.model_selection import train_test_split
training_set, test_set = train_test_split(data, test_size = 0.2, random_state = 1)

#Classifying the predictors and target
X_train = training_set.iloc[:,0:13].values
Y_train = training_set.iloc[:,14].values
X_test = test_set.iloc[:,0:13].values
Y_test = test_set.iloc[:,14].values

#Initializing Support Vector Machine and fitting the training data
from sklearn.svm import SVC
classifier = SVC(kernel='rbf', random_state = 1)
classifier.fit(X_train,Y_train)

#Predicting the classes for test set
Y_pred = classifier.predict(X_test)

#Attaching the predictions to test set for comparing
test_set["New Prdiction"] = Y_pred

#Calculating the accuracy of the predictions
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test,Y_pred)
accuracy = float(cm.diagonal().sum())/len(Y_test)*100
print("Accuracy Of SVM For The Given Dataset : ", accuracy,"\n")


from sklearn.svm import SVC
classifier = SVC(kernel='rbf', random_state = 1)
classifier.fit(X_train,Y_train)

print("Y_test \t Y_Predict")
for i in range(len(Y_test)):
    print(str(Y_test[i])+" \t "+str(Y_pred[i]))
