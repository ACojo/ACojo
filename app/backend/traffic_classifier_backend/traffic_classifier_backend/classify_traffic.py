
def traffic_classification():
    with open('traffic_tcp.txt','r') as file:
        li = file.readlines()
        total_line = len(li)
        # print(li[0].split())
        line = [line.split() for line in li ]
        # print(data)
        # print(data[3])
        print(len(li))
        if len(li) > 8:
               same_ip_dest = 1
               same_ip_src = 1
               print(li)
               print("date initiale)")
               for i in range(0, len(li) - 7):
                        data = [ line[i] for i in range(i, i+8) ]
                        # print(i)
                        dimension_mean = int(data[i][1])
                        time_mean = int(data[i][0])
                        flags = [data[i][5]]
                        method = [ data[i][4] ]
                        print(len(data))
                        print(data)
                        for y in range(0,7):
                            print(y)
                            if data[y][2] != data[y+1][2]:
                                same_ip_dest = 0
                            if data[y][3] != data[y+1][3]:
                                same_ip_src = 0
                            dimension_mean += int(data[y+1][1])
                            time_mean += int(data[y+1][0])
                            method.append(data[y+1][4] )
                            flags.append(data[y+1][5] )
                        
                        # method -= ','
                        dimension_mean = int(dimension_mean / 8)
                        time_mean = int(time_mean / 8)
                        print(flags)
                        print([f for f in flags])
                        network_input = [time_mean, dimension_mean, same_ip_dest, same_ip_src]
                        network_input += flags
                        network_input += method
                        print()
                        print(network_input)
                        print()



                            

                        
        # print(f"Number of lines in the notepad file: {total_line}")
    

    # if data:
    #     print(data)
    # else:
    #     traffic_udp_file = open('traffic_udp', "w")
    #     li = traffic_udp_file.readlines()
    #     print(len(data))
    #     # print(data)
    #     with open('traffic_udp.txt','r') as file:
    #     li = file.readlines()
    #     total_line = len(li)
    #     print(f"Number of lines in the notepad file: {total_line}")
    



if __name__ == "__main__":
        data = {'traffic': 'tcp', 'pkts': '1112', 'TimeBetweenPackets': '12', 'pktsSize': '123', 'ipDest': '1.1.1.1', 'ipSrc': '1.1.1.1', 'method': '0', 'flags': '0'}

        # print(data)
        traffic_classification()
        # th_server = Thread(target = app.run, args = ('0.0.0.0',))



        # th_server.start()