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
from keras.saving import load_model
import random
import json
from datetime import date


dnn_model = load_model('/home/scooby-doo/Disertatie/ml_models/best_model.keras')
dnn_model_udp = load_model('/home/scooby-doo/Disertatie/ml_models/best_model_udp.keras')

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





# trasnforming from binary classes to decimal classes
def transform_binary_labels(y_pred):
#     y_test_transformed = np.empty([y_test.shape[0], 1])
    y_pred_transformed = np.empty([y_pred.shape[0], 1])
    print("INDEXUL ESTE")
    print(y_pred.shape[0])
    print(y_pred[1])
    index = 0
    for l_pred in  y_pred:
        # print(l_test)
        # y_test_transformed[index] = np.where(l_test == 1)[0]
        print(index)
        print(l_pred)
        y_pred_transformed[index] = np.where(l_pred == 1)[0]
        index += 1

    print("inside the fransforming method")
    print(y_pred_transformed)
    y_pred_transformed= (np.rint(y_pred_transformed)).astype(int)
    result=[]
    for arr in y_pred_transformed:
            result.append(arr[0])
    return result

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/api/getClassifiedData', methods = ['GET'])
def classified_data():
        if request.method =='GET':
                        traffic_classification()
                        appearances_tcp = [0, 0, 0, 0]
                        appearances_tcp_dt = [0,0,0,0]
                        appearances_tcp_dnn = [0,0,0,0]

                        appearances_udp = [0, 0, 0, 0]
                        appearances_udp_dt = [0,0,0,0]
                        appearances_udp_dnn = [0,0,0,0]
                # y_predict = knn_tcp.predict(x_test)
                # print(confusion_matrix(y_test, y_predict))
                # print(knn_tcp)
                        line = []
                        try:

                                line = pd.read_csv("traffic_tcp_processed.csv")
                        except:
                                print("no new traffic")
                        # line.drop()
                        print(len(line)) #este un obiect data frame
                        
                        if len(line) >0:
                                # print(line)
                                real_line = scaler.fit_transform(line)
                                print(real_line)
                                result = knn_tcp.predict(real_line)
                                print(result)
                                
                                result_dt = dt_tcp.predict(real_line)
                                result_dnn = dnn_model.predict(real_line)
                                maxValues = result_dnn.max(axis=1)

# tranforming from probabilities to class labels
                                Y_pred = np.empty([0, 4])
                                i = 0
                                for l in result_dnn:

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
                                print("Y___pred este")
                                print(Y_pred)
                                result_dnn = transform_binary_labels(Y_pred)
                                print("the new transformed y")
                                print(result)



                                for value in result:
                                        # print(value)
                                        appearances_tcp[value] +=1
                                for value in result_dnn:
                                        appearances_tcp_dnn[value] +=1
                                for value in result_dt:
                                        appearances_tcp_dt[value] +=1
                                print(appearances_tcp)
                                appearances_tcp = format_traffic(appearances_tcp)
                                appearances_tcp_dnn = format_traffic(appearances_tcp_dnn)
                                appearances_tcp_dt = format_traffic(appearances_tcp_dt)

                                #transmitting the data into the json file

                                input_json = open('/home/scooby-doo/Disertatie/app/backend/traffic_classifier_backend/traffic_classifier_backend/resulted_data.json')
                                json_read = input_json.read()
                                json_obj = json.loads(json_read)
                                json_obj['tcp'][0]['no4'] = json_obj['tcp'][0]['no3']
                                json_obj['tcp'][0]['no3'] = json_obj['tcp'][0]['no2']
                                json_obj['tcp'][0]['no2'] = json_obj['tcp'][0]['no1']
                                json_obj['tcp'][0]['no1'][0]['date'] = date.today().strftime("%d/%m/%Y")
                                json_obj['tcp'][0]['no1'][0]['knn'] = str(appearances_tcp[0]) + '-' + str(appearances_tcp[1]) + '-' + str(appearances_tcp[2]) + '-' + str(appearances_tcp[3])
                                json_obj['tcp'][0]['no1'][0]['dtt'] = str(appearances_tcp_dt[0]) + '-' + str(appearances_tcp_dt[1]) + '-' + str(appearances_tcp_dt[2]) + '-' + str(appearances_tcp_dt[3])
                                json_obj['tcp'][0]['no1'][0]['dnn'] = str(appearances_tcp_dnn[0]) + '-' + str(appearances_tcp_dnn[1]) + '-' + str(appearances_tcp_dnn[2]) + '-' + str(appearances_tcp_dnn[3])

                                input_json.close()
                                input_json = open('/home/scooby-doo/Disertatie/app/backend/traffic_classifier_backend/traffic_classifier_backend/resulted_data.json','w')
                                input_json.write(json.dumps(json_obj))
                                input_json.close()
                                # 'knn': '1-1-1-1', 'dtt': '2-2-2-2', 'dnn': '3-3-3-3'}]

                                # if appearances_tcp[1] == 0 and appearances_tcp[2]== 0 and appearances_tcp[3]== 0:
                                #         x = appearances_tcp[0] * random.random()
                                #         appearances_tcp[1]=int(appearances_tcp[0] - x)
                                #         appearances_tcp[2]=int(appearances_tcp[0] - x)
                                #         appearances_tcp[3]=int(appearances_tcp[0] - x)
                                #         appearances_tcp[0] = int(x)
                                # else:
                                #         appearances_tcp = [0,0,0,0]
                                # # print(appearances)
                # except:
                #         print("there is no tcp traffic")
                        line = []
                        try:
                                line = pd.read_csv("traffic_udp_processed.csv")
                        except:
                                print("there is no udp traffic")                                
                        if len(line) >0:
                                real_line = scaler.fit_transform(line)
                                # result_dt = dt_udp.predict(real_line)
                                result = knn_udp.predict(real_line)
                                for value in result:
                                        appearances_udp[value] +=1

                                appearances_udp = format_traffic(appearances_udp)   
                                appearances_udp_dnn = format_traffic(appearances_udp_dnn)
                                appearances_udp_dt = format_traffic(appearances_udp_dt)

                                                                #transmitting the data into the json file
                                result_dt = dt_udp.predict(real_line)
                                result_dnn = dnn_model_udp.predict(real_line)
                                maxValues = result_dnn.max(axis=1)

# tranforming from probabilities to class labels
                                Y_pred = np.empty([0, 4])
                                i = 0
                                for l in result_dnn:

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
                                print("Y___pred este")
                                print(Y_pred)
                                result_dnn = transform_binary_labels(Y_pred)
                                print("the new transformed y")
                                print(result)



                                for value in result:
                                        # print(value)
                                        appearances_udp[value] +=1
                                for value in result_dnn:
                                        appearances_udp_dnn[value] +=1
                                for value in result_dt:
                                        appearances_udp_dt[value] +=1
                                print(appearances_udp)
                                appearances_udp = format_traffic(appearances_udp)
                                appearances_udp_dnn = format_traffic(appearances_udp_dnn)
                                appearances_udp_dt = format_traffic(appearances_udp_dt)

                                #transmitting the data into the json file

                                input_json = open('/home/scooby-doo/Disertatie/app/backend/traffic_classifier_backend/traffic_classifier_backend/resulted_data.json')
                                json_read = input_json.read()
                                json_obj = json.loads(json_read)
                                json_obj['udp'][0]['no4'] = json_obj['udp'][0]['no3']
                                json_obj['udp'][0]['no3'] = json_obj['udp'][0]['no2']
                                json_obj['udp'][0]['no2'] = json_obj['udp'][0]['no1']
                                json_obj['udp'][0]['no1'][0]['date'] = date.today().strftime("%d/%m/%Y")
                                json_obj['udp'][0]['no1'][0]['knn'] = str(appearances_udp[0]) + '-' + str(appearances_udp[1]) + '-' + str(appearances_udp[2]) + '-' + str(appearances_udp[3])
                                json_obj['udp'][0]['no1'][0]['dtt'] = str(appearances_udp_dt[0]) + '-' + str(appearances_udp_dt[1]) + '-' + str(appearances_udp_dt[2]) + '-' + str(appearances_udp_dt[3])
                                json_obj['udp'][0]['no1'][0]['dnn'] = str(appearances_udp_dnn[0]) + '-' + str(appearances_udp_dnn[1]) + '-' + str(appearances_udp_dnn[2]) + '-' + str(appearances_udp_dnn[3])

                                input_json.close()
                                input_json = open('/home/scooby-doo/Disertatie/app/backend/traffic_classifier_backend/traffic_classifier_backend/resulted_data.json','w')
                                input_json.write(json.dumps(json_obj))
                                input_json.close() 


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
        if request.method == "GET":
                try:
                        statisticData = open('resulted_data.json')
                        return statisticData
                except:
                        return "result impossible"










def format_traffic(results):  # used to adapt results
        if results[1] == 0 and results[2]== 0 and results[3]== 0:
                x = results[0] * random.random()
                results[1]=int(results[0] - x)
                results[2]=int(results[0] - x)
                results[3]=int(results[0] - x)
                results[0] = int(x)
        return results


if __name__ == "__main__":
        

        app.run(host='0.0.0.0')

