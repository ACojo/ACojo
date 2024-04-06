import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
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

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(x_train, y_train)

y_predict = knn.predict(x_test)

print(x_test)
print(type(x_test))

print(confusion_matrix(y_test, y_predict))
print(classification_report(y_test, y_predict))
print(accuracy_score(y_test, y_predict))



#to delete / this is for the test purposes only
data = pd.read_csv("/home/scooby-doo/Disertatie/DataSet/traffic_tcp_processed.csv")
# data = pd.read_csv("/home/scooby-doo/Disertatie/DataSet/tcp_data.csv")
data = data.drop("class", axis=1)
x_real = scaler.fit_transform(data)
y_real = knn.predict(x_test)
print("**************")
print(x_real)
print("*************")
wtf = [ 0, 0, 0, 0] 
print("*************")
print(y_real)
print("*************")
for x in y_real:
    wtf[x] +=1

print("************")
print(wtf)

print("***************")



# # finding the best k
# err_rate = []
# min = np.mean(y_predict != y_test)
# for i in range(1, 30):
#     knn = KNeighborsClassifier(n_neighbors=i)
#     knn.fit(x_train, y_train)

#     i_predict = knn.predict(x_test)
#     err_rate.append((np.mean(i_predict != y_test)))

#     if err_rate[i-1] < min :
#         min = err_rate[i-1]





# plt.figure(figsize=(10, 6))
# plt.plot(range(1, 30), err_rate, color='blue', linestyle='--', markersize=10, markerfacecolor='red', marker='o')
# plt.title("Error rate")
# plt.xlabel('k')
# plt.ylabel('Error')
# plt.draw()

# print("-----------------------")
# print("best classifier")
# print(min)
# knn = KNeighborsClassifier(n_neighbors=3)

# knn.fit(x_train, y_train)

# y_predict = knn.predict(x_test)

# print(confusion_matrix(y_test, y_predict))
# print(classification_report(y_test, y_predict))
# print(classification_report(y_test, y_predict))


# plt.show()