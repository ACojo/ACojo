def generate(data, type):
    if type =='tcp':
        traffic_file = open("traffic_tcp.txt", "a")
    else:
        traffic_file = open('traffic_udp.txt', "a")
    print(data)
    traffic=""
    for key,value in data.items():
        print(key, "->", value)
        if (not(key == 'traffic' or key =='pkts')):
            traffic = traffic +" " + value + " "
    
    for i in range(0,int(data['pkts'])):
        traffic_file.write(traffic + "\n")

    



    traffic_file.close()
    return


