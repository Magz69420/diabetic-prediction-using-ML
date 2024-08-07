import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score  

#Data Collection and Analysis

diabetes_dataset = pd.read_csv('F:\mnml\data\diabetes.csv')

#printing the first five rows of the dataset

diabetes_dataset.head()

#numbers of rows and Columns in this dataset

diabetes_dataset.shape

#Getting the Statistical measures of the data

diabetes_dataset.describe()
diabetes_dataset['Outcome'].value_counts()
diabetes_dataset.groupby('Outcome').mean()

# Separating the data and labels
 
X = diabetes_dataset.drop(columns= 'Outcome' , axis=1)
y = diabetes_dataset['Outcome']

#Data Standardization

scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)
print(standardized_data)

X = standardized_data
y = diabetes_dataset['Outcome']

# Train and split

X_train , X_test , y_train , y_test = train_test_split(X,y , test_size=0.2 , stratify = y ,random_state= 2)

# Training the model
classifier = svm.SVC(kernel= 'linear')

# Training the support vector machine classifier
classifier.fit(X_train , y_train)

# Model Evaluation / accuracy Score

X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction , y_train)

#print ('Accuracy score of the training data: ' , training_data_accuracy)

#Accuracy on test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction , y_test)
#print ('Accuracy score of the training data: ' , test_data_accuracy)

# Prediction system process

input_data = (4,110,92,0,0,37.6,0.191,30)

# change to numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the array as we predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# Standardize the input data 
std_data = scaler.transform(input_data_reshaped)
print(std_data)
prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0]== 0):
    print('The person is not diabetic')
else:
    print ('The person is diabetic')
