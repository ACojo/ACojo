from scapy.all import *

# Funcție pentru a genera și trimite un pachet cu dimensiunea datelor specificată
def send_packet(data, type):
    # Construirea unui pachet IP și unul TCP
    ip_packet = IP(dst=data['ipDest'], src=data['ipSrc'])

    # Generarea de date de dimensiune specificată
    pkts_data = b"A" * int(data['pktsSize'])  # Aici generăm date compuse doar din caractere 'A'

    if type == 'udp':
        
        if data['method'] == '250' : # the DNS method
            tcp_packet = TCP(dport=53)
        elif data['method'] == '500' : # the NTP method
            tcp_packet = TCP(dport=123)
        elif data['method'] == '750' : # the SNMP method
            tcp_packet = TCP(dport=161)
        elif data['method'] == '0' : # the TFTP method
            tcp_packet = TCP(dport=69)
        
        request = ip_packet / tcp_packet #/  pkts_data
        print(request)
        send(request)

    else:
        if data['flags'] == '250' : # the ACK method
            tcp_packet = TCP(dport=80, flags='A')
        elif data['flags'] == '500' : # the SYN method

            tcp_packet = TCP(dport=80, flags="S")
        elif data['flags'] == '750' : # the ECHO REQ method
            icmp_packet = IP(dst=data['ipDest']) / ICMP(type=8, code=0)
            send(icmp_packet)
            return
        elif data['flags'] == '0' : # the RESET method
            tcp_packet = TCP(dport=80, flags='R')
    
        if data['method'] == '250' : # the GET method
            request = ip_packet / tcp_packet /  Raw("GET / HTTP/1.1\r\nHost: 192.168.1.1\r\n\r\n")
        elif data['method'] == '500' : # the POST method
            request = ip_packet / tcp_packet / Raw("PUT /path/to/resource HTTP/1.1\r\nHost: example.com\r\nContent-Length: {}\r\n\r\n".format(data['pktsSize'])) / pkts_data
        elif data['method'] == '750' : # the PUT method
            request = ip_packet / tcp_packet / Raw("DELETE /path/to/resource HTTP/1.1\r\nHost: example.com\r\nContent-Length: {}\r\n\r\n".format(data['pktsSize'])) / pkts_data
        elif data['method'] == '0' : # the DELETE method
            request = ip_packet / tcp_packet / Raw("PUT /path/to/resource HTTP/1.1\r\nHost: example.com\r\nContent-Length: {}\r\n\r\n".format(data['pktsSize'])) / pkts_data

        print(request)
        send(request)
  

    # # Crearea pachetului final prin adăugarea datelor (payload)
    # packet = ip_packet / tcp_packet / Raw(load=pkts_data)

    # # Trimiterea pachetului
    # send(packet, verbose=False)

# # Utilizare
# try:
#     # Specificați adresa IP destinație, portul destinație și dimensiunea datelor dorită
#     destination_ip = "192.168.1.1"
#     destination_port = 80
#     data_size = 10000  # Modificați în funcție de dimensiunea dorită a pachetului

#     # Generați și trimiteți pachetul cu dimensiunea specificată
#     send_large_packet(destination_ip, destination_port, data_size)

#     print(f"Pachet cu dimensiunea {data_size} trimis către {destination_ip}:{destination_port}")

# except PermissionError:
#     print("Executați acest script cu privilegii de administrator (sudo pe sisteme Unix).")


# if __name__ == "__main__":
#         data = {'traffic': 'tcp', 'pkts': '1112', 'TimeBetweenPackets': '12', 'pktsSize': '123', 'ipDest': '1.1.1.1', 'ipSrc': '1.1.1.1', 'method': '0', 'flags': '0'}

#         print(data)
#         send_packet(data, 'udp')
#         # th_server = Thread(target = app.run, args = ('0.0.0.0',))



#         # th_server.start()
