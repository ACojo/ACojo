import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, \
    f1_score

from keras.models import Sequential

from tensorflow.keras.layers import Dense
# from tensorflow.python.keras.callbacks import ModelCheckpoint
from keras.callbacks import ModelCheckpoint
from keras.saving import load_model


# transforming from decimal classes to binary classes
def transform_decimal_labels(y_data):
    y_data_formatted = []
    for i in range(0, y_data.shape[0]):
        if y_data[i] == 0:
            y_data_formatted.append([1, 0, 0, 0])  # normal traffic
        elif y_data[i] == 1:
            y_data_formatted.append([0, 1, 0, 0])  # Dos traffic
        elif y_data[i] == 2:
            y_data_formatted.append([0, 0, 1, 0])  # Dos traffic
        elif y_data[i] == 3:
            y_data_formatted.append([0, 0, 0, 1])  # Dos traffic

    return pd.DataFrame(y_data_formatted)


# trasnforming from binary classes to decimal classes
def transform_binary_labels(y_test, y_pred):
    y_test_transformed = np.empty([y_test.shape[0], 1])
    y_pred_transformed = np.empty([y_test.shape[0], 1])

    for index, l_test, l_pred in zip(range(0, y_test.shape[1]), y_test, y_pred):
        print(l_test)
        y_test_transformed[index] = np.where(l_test == 1)[0]
        y_pred_transformed[index] = np.where(l_pred == 1)[0]

    return y_test_transformed, y_pred_transformed


data = pd.read_csv("/home/scooby-doo/Disertatie/DataSet/tcp_data.csv")

# reading the data from the dataset
x_data = data.drop("class", axis=1)
y_data = data["class"]  # the data formated in decimal

# scaling the data so that it will be in 0 1 range
scaler = MinMaxScaler()
x_data = scaler.fit_transform(x_data)

# transforming from decimal classes to binary classes
y_data = transform_decimal_labels(y_data)

# splitting the data into test and train

train_size = 0.85
X_data = np.array(x_data)
Y_data = np.array(y_data)

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=42)


# defining the model
def get_model():
    model = Sequential([
        Dense(50, activation='relu'),
        Dense(50, activation='relu'),
        Dense(4, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    return model


checkpoint = ModelCheckpoint(
    'best_model.keras',        # where to save the model
    monitor='val_loss',               # metric to be monitored
    verbose = 1,
    save_best_only = True,            # save only the best model
    mode='min'                        # for the val_loss should be kept only the min value
)

# training the model
model = get_model()
model.fit(x_train, y_train, batch_size=32, epochs=70, validation_split=0.2, callbacks=[checkpoint])

print("predicting...")
# Making predictions on the testing set
y_pred = model.predict(x_test)


print("load new model")
new_model = load_model('best_model.keras')
y_pred = new_model.predict(x_test)
print(y_pred)
maxValues = y_pred.max(axis=1)

# tranforming from probabilities to class labels
Y_pred = np.empty([0, 4])
i = 0
for l in y_pred:

    if np.where(l == maxValues[i])[0][0] == 0:

        Y_pred = np.append(Y_pred, [[1, 0, 0, 0]], axis=0)
    elif np.where(l == maxValues[i])[0][0] == 1:
        Y_pred = np.append(Y_pred, [[0, 1, 0, 0]], axis=0)
    elif np.where(l == maxValues[i])[0][0] == 2:
        Y_pred = np.append(Y_pred, [[0, 0, 1, 0]], axis=0)
    else:
        Y_pred = np.append(Y_pred, [[0, 0, 0, 1]], axis=0)
    i += 1

# transforming the results from binary clases to decimal classes
Y_pred = (np.rint(Y_pred)).astype(int)
y_test_transformed, y_pred_transformed = transform_binary_labels(np.array(y_test), Y_pred)

# Evaluating the model
accuracy = accuracy_score(np.array(y_test), Y_pred)
# precision = precision_score(y_test_transformed, y_pred_transformed, average='macro')
# recall = recall_score(y_test_transformed, y_pred_transformed)
f1 = f1_score(y_test_transformed, y_pred_transformed, average='macro')
conf_matrix = confusion_matrix(y_test_transformed, y_pred_transformed)
class_report = classification_report(y_test_transformed, y_pred_transformed)

# Printing the evaluation metrics
print("Accuracy:", accuracy)
# print("Precision:", precision)
# print("Recall:", recall)
print("F1 Score:", f1)
print("\nConfusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", class_report)
