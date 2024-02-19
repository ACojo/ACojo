from threading import Thread
from multiprocessing import Process
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from generateTraffic import send_packet


#from time import sleep
import time

import os


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'





# @app.route('/api/generatetraffic',methods = ['GET'])
# def test():
#         return "GOOD"


@app.route('/api/generatetraffic',methods = ['GET','PUT'])
# @cross_origin(supports_credentials=True)
def index_generate():
        if request.method == "GET":
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
                        
                
                        for i in range(0,data['pkts']):
                                send_packet(data=data)
                                time.sleep(data['TimeBetweenPackets'])
                                
                        return response

                except Exception as e:

                        response = jsonify({'error': str(e)})
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

