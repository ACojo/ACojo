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
from custom_traffic import *





knn_tcp = KNeighborsClassifier(n_neighbors=5)
dt_tcp = DecisionTreeClassifier()

knn_udp = KNeighborsClassifier(n_neighbors=3)
dt_udp = DecisionTreeClassifier()


data = pd.read_csv("/home/scooby-doo/Disertatie/DataSet/tcp_data.csv")
# reading the data from the dataset
x_data = data.drop("class", axis=1)
y_data = data["class"]

        # scaling the data so that it will be in 0 1 range
scaler = MinMaxScaler()
x_data = scaler.fit_transform(x_data)

        # spliting the data into test and train

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=1)
print(x_train)


knn_tcp.fit(x_train, y_train)
dt_tcp.fit(x_train, y_train)




data = pd.read_csv("/home/scooby-doo/Disertatie/DataSet/udp_data.csv")
# reading the data from the dataset    x_data = data.drop("class", axis=1)
y_data = data["class"]

# scaling the data so that it will be in 0 1 range
scaler = MinMaxScaler()
x_data = scaler.fit_transform(x_data)

# spliting the data into test and train

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=1)
print(x_train)


knn_udp.fit(x_train, y_train)
dt_udp.fit(x_train, y_train)







app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/api/getClassifiedData', methods = ['GET'])
def classified_data():
        if request.method =='GET':
                traffic_classification()
                appearances_tcp = [0, 0, 0, 0]
                appearances_udp = [0, 0, 0, 0]
                # y_predict = knn_tcp.predict(x_test)
                # print(confusion_matrix(y_test, y_predict))
                # print(knn_tcp)
                try:

                        line = pd.read_csv("traffic_tcp_processed.csv")
                        print(len(line)) #este un obiect data frame
                        if len(line) >0:
                                # print(line)
                                real_line = scaler.fit_transform(line)
                                print(line)
                                result = knn_tcp.predict(real_line)
                                # print(result)
                                for value in result:
                                        # print(value)
                                        appearances_tcp[value] +=1
                # print(appearances)
                except:
                        print("there is no tcp traffic")
                try:
                        line = pd.read_csv("traffic_udp_processed.csv")
                        if len(line) >0:
                                real_line = scaler.fit_transform(line)
                                result = knn_udp.predict(real_line)
                                # result = knn_udp.predint(line)
                                for value in result:
                                        appearances_udp[value] +=1
                except:
                        print("there is no udp traffic")
                proccessed_traffic  = open("traffic_tcp_processed.csv", "w")
                proccessed_traffic.write('')
                proccessed_traffic.close()
                
                
                proccessed_traffic  = open("traffic_udp_processed.csv", "w")
                proccessed_traffic.write('')
                proccessed_traffic.close()

                return appearances_tcp + appearances_udp




@app.route('/api/generatetraffic',methods = ['GET','PUT'])
def index_generate():
        if request.method == "GET":

                return "generate"
        if request.method =='PUT':
                try:
                        data = request.json
        

                        print("Date primite:", data)

                        print(data['traffic'])

                        response = jsonify({'response': 'processed'})
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        
                        print(data['pkts'])
                        print(type(data['pkts']))
                        print(type(int(data['pkts'])))
                        for i in range(0,int(data['pkts'])):

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
        

@app.route('/api/generateCustomTraffic',methods = ['GET','PUT'])
def index_custom_traffic():
        if request.method == "GET":

                return "normal"
        if request.method =='PUT':
                try:
                        data = request.json
        

                        print("Date primite:", data)

                        # print(data['traffic'])

                        response = jsonify({'response': 'processed'})
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        
                        # print(data['pkts'])
                        # print(type(data['pkts']))
                        # print(type(int(data['pkts'])))
                        # for i in range(0,int(data['pkts'])):

                                # time.sleep(random.randint(12, 25)*0.001)
                        if data['traffic'] == 'tcp':
                                print('tcp')
                                if data['type'] == 'normal':
                                        
                                        for i in range(0,int(data['pkts'])):
                                                print('normal')
                                                print(i)
                                                tcp_usual_traffic()
                                elif data['type'] == 'buffer':
                                        
                                        for i in range(0,int(data['pkts'])):
                                                print('buffer')
                                                tcp_gen_buffer_attack()
                                elif data['type'] == 'ddos':
                                        for i in range(0,int(data['pkts'])):
                                                print('ddos')
                                                tcp_gen_dos_attack()
                                else:
                                        for i in range(0,int(data['pkts'])):
                                                print('smurf')
                                                tcp_gen_smurf_attack()
                        else:
                                if data['type'] == 'normal':
                                         for i in range(0,int(data['pkts'])):
                                                udp_usual_traffic()                               
                                elif data['type'] == 'buffer':
                                        for i in range(0,int(data['pkts'])):
                                                udp_gen_amplification_attack()
                                elif data['type'] == 'ddos':
                                         for i in range(0,int(data['pkts'])):
                                                udp_gen_dos_attack()                               
                                else:
                                        for i in range(0,int(data['pkts'])):
                                                udp_gen_insider_attack()
                        # generate(data=data, type=data['traffic'])    
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



@app.route('/api/getStatisticsdData', methods = ['GET'])
def statistics_data():
        if request.method == GET:
                

if __name__ == "__main__":
        

        app.run(host='0.0.0.0')

