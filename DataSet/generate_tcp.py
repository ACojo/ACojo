# from scapy.all import *
#
# # Funcție pentru a genera și afișa un pachet TCP
# def generate_tcp_packet(source_ip, source_port, destination_ip, destination_port, data):
#     # Construirea unui pachet IP și unul TCP
#     ip_packet = IP(src=source_ip, dst=destination_ip)
#     tcp_packet = TCP(sport=source_port, dport=destination_port)
#
#     path = "/"
#     # Cererea HTTP GET
#     http_get_request = f"GET {path} HTTP/1.1: {destination_ip}"
#
#     # Crearea pachetului final prin adăugarea datelor (payload)
#     packet = ip_packet / tcp_packet / Raw(load=http_get_request)
#
#     # Afișarea informațiilor despre pachet
#     sr(packet)
#     print(packet.show())
#
# # Utilizare
# try:
#     # Specificați adresele IP, porturile și datele dorite
#     source_ip = "192.168.1.11"
#     source_port = 12345
#     destination_ip = "192.168.1.192"
#     destination_port = 5000
#     data = "Hello, this is a TCP packet!"
#
#     # Generați și afișați pachetul TCP
#
#     generate_tcp_packet(source_ip, source_port, destination_ip, destination_port, data)
#
# except PermissionError:
#     print("Executați acest script cu privilegii de administrator (sudo pe sisteme Unix).")

#import tensorflow as tf

from scapy.all import *
import requests
#from tensorflow import keras
#x = tf.transpose(1, perm=[1, 0])


# Funcție pentru a genera și trimite un pachet HTTP GET
def send_http_get_packet(destination_ip, destination_port, path):
    # Construirea unui pachet IP și unul TCP
    ip_packet = IP(dst=destination_ip)
    tcp_packet = TCP(dport=destination_port)

    # SYN
    ip = IP(src='192.168.1.192', dst=destination_ip)
    SYN = TCP(sport=20, dport=destination_port, flags='S', seq=1000)
    SYNACK = sr1(ip / SYN)

    # ACK
    ACK = TCP(sport=20, dport=destination_port, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + 1)
    send(ip / ACK)

    # Cererea HTTP GET
    http_get_request = f"GET {path} HTTP/1.1\r\nHost: {destination_ip}\r\n\r\n"

    # Crearea pachetului final prin adăugarea datelor (payload)
    packet = ip_packet / tcp_packet / Raw(load=http_get_request)

    # Trimiterea pachetului
    response_packet = sr1(packet, verbose=True)
    print(response_packet.show())
    print(packet.show())
    pck = ip / ACK
    print(pck.show())


# Utilizare
try:
    # Specificați adresa IP destinație, portul destinație și calea dorită pentru cererea GET
    destination_ip = '192.168.1.107'
    destination_port = 5000
    path = "/"

    # Generați și trimiteți pachetul HTTP GET
    # for i in range(0, 10):
    send_http_get_packet(destination_ip, destination_port, path)
    # r = requests.get(url='http://192.168.1.107:5000/')
    print(f"Pachet HTTP GET trimis către {destination_ip}:{destination_port}{path}")
    # print(r)

except PermissionError:
    print("Executați acest script cu privilegii de administrator (sudo pe sisteme Unix).")

#
# import requests
#
# # Funcție pentru a trimite o cerere HTTP GET
# def send_http_get_request(url):
#     try:
#         response = requests.get(url)
#         print(f"Status code: {response.status_code}")
#         print("Response content:")
#         print(response.text)
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#
# # Utilizare
# try:
#     # Specificați URL-ul dorit pentru cererea GET
#     url = "http://192.168.1.192:5000/"
#
#     # Trimiteți cererea HTTP GET
#     send_http_get_request(url)
#
# except Exception as e:
#     print(f"Error: {e}")
