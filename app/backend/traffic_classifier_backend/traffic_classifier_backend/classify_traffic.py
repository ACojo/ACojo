
def traffic_classification(data):
    traffic_tcp_file = open("traffic_tcp.txt", "w")
    data = traffic_tcp_file.read()

    if data:
        print(data)
    else:
        traffic_udp_file = open('traffic_udp', "w")
        data = traffic_udp_file.read()
        print(data)
    



if __name__ == "__main__":
        # data = {'traffic': 'tcp', 'pkts': '1112', 'TimeBetweenPackets': '12', 'pktsSize': '123', 'ipDest': '1.1.1.1', 'ipSrc': '1.1.1.1', 'method': '0', 'flags': '0'}

        # print(data)
        traffic_classification()
        # th_server = Thread(target = app.run, args = ('0.0.0.0',))



        # th_server.start()