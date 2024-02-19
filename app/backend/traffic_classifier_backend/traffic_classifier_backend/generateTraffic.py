from scapy.all import *

# Funcție pentru a genera și trimite un pachet cu dimensiunea datelor specificată
def send_packet(data, type):
    # Construirea unui pachet IP și unul TCP
    ip_packet = IP(dst=data['ipDest'], src=data['ipsrc'])
    # if type == 'tcp'
    tcp_packet = TCP(dport=data[''])

    # Generarea de date de dimensiune specificată
    pkts_data = b"A" * data['pktsSize']  # Aici generăm date compuse doar din caractere 'A'

    # Crearea pachetului final prin adăugarea datelor (payload)
    packet = ip_packet / tcp_packet / Raw(load=pkts_data)

    # Trimiterea pachetului
    send(packet, verbose=False)

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
