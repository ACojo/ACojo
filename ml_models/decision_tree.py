import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

data = pd.read_csv("/home/scooby-doo/Disertatie/DataSet/tcp_data.csv")

# reading the data from the dataset
x_data = data.drop("class", axis=1)
y_data = data["class"]

# scaling the data so that it will be in 0 1 range
scaler = MinMaxScaler()
x_data = scaler.fit_transform(x_data)

# spliting the data into test and train

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=1)

dt = DecisionTreeClassifier()

dt.fit(x_train, y_train)

y_predict = dt.predict(x_test)

print(confusion_matrix(y_test, y_predict))
print(classification_report(y_test, y_predict))
print(accuracy_score(y_test, y_predict))
