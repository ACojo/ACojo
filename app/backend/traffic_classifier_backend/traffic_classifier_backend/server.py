from threading import Thread
from multiprocessing import Process
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from generateTraffic import send_packet
from generate import generate
#from time import sleep
import time
import os
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from classify_traffic import traffic_classification




data = pd.read_csv("/home/scooby-doo/Disertatie/DataSet/tcp_data.csv")

# reading the data from the dataset
x_data = data.drop("class", axis=1)
y_data = data["class"]

# scaling the data so that it will be in 0 1 range
scaler = MinMaxScaler()
x_data = scaler.fit_transform(x_data)

# spliting the data into test and train

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=1)

knn = KNeighborsClassifier(n_neighbors=3)
dt = DecisionTreeClassifier()



knn.fit(x_train, y_train)
dt.fit(x_train, y_train)








app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'





# @app.route('/api/generatetraffic',methods = ['GET'])
# def test():
#         return "GOOD"


@app.route('/api/getClassifiedData', methods = ['GET'])
def classified_data():
        if request.method =='GET':
                traffic_classification()
                appearances = [0, 0, 0, 0]
                # with open('traffic_udp.csv','r') as file:
                # li = file.readlines()
                # line = [line.split() for line in li ]
                # line = pd.array( 12, 124312, 1, 1, 500, 500, 500, 500, 500 ,500, 500, 500, 250, 250, 250, 250, 250, 250, 250, 250)
                line = pd.read_csv("traffic_tcp_processed.csv")
                result = knn.predict(line)
                for value in result:
                        appearances[value] +=1
                print(appearances)
                return appearances




@app.route('/api/generatetraffic',methods = ['GET','PUT'])
# @cross_origin(supports_credentials=True)
def index_generate():
        if request.method == "GET":
                # # return "generate"
                # knn.predict(x_test)
                # print(knn.predict(x_test))
                return "generate"
        if request.method =='PUT':
                try:
                # Primiți datele JSON trimise în corpul cererii PUT
                        data = request.json
        
                # Aici poți face ce dorești cu datele primite
                        print("Date primite:", data)

                        print(data['traffic'])
                # Răspunde cu un mesaj de succes
                        response = jsonify({'response': 'processed'})
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        
                        print(data['pkts'])
                        print(type(data['pkts']))
                        print(type(int(data['pkts'])))
                        for i in range(0,int(data['pkts'])):
                                # send_packet(data=data, type=data['traffic'])
                                time.sleep(int(data['TimeBetweenPackets'])*0.001)
                        generate(data=data, type=data['traffic'])    
                        print(data)
                        return response

                except Exception as e:

                        response = jsonify({'error': str(e)})
                        print(e)
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        return response
                        # În caz de eroare, răspunde cu un mesaj de eroare
                        return jsonify({"error": str(e)}), 500
                        # return "GOOD"
        else:
                return "not good"
        
#         try:
#         # Primiți datele JSON trimise în corpul cererii PUT
#         data = request.json
        
#         # Aici poți face ce dorești cu datele primite
#         print("Date primite:", data)

#         # Răspunde cu un mesaj de succes
#         return jsonify({"message": "Date primite cu succes"}), 200
#     except Exception as e:
#         # În caz de eroare, răspunde cu un mesaj de eroare
#         return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
        app.run(host='0.0.0.0')

        # th_server = Thread(target = app.run, args = ('0.0.0.0',))



        # th_server.start()

