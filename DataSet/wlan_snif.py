# from scapy.all import *
#
#
# def capture_tcp_packet():
#     # Capturarea unui singur pachet TCP
#     packet = sniff(filter="tcp", count=1)[0]
#     return packet
#
#
# # Utilizare
# tcp_packet = capture_tcp_packet()
# print(tcp_packet.summary())  # Afișează un rezumat al pachetului

from scapy.all import *
from collections import Counter
import time

# Funcție pentru a captura pachete timp de 'duration' secunde
def capture_packets(duration):
    packets = sniff(timeout=duration)
    return packets

# Funcție pentru a calcula frecvența pachetelor
def calculate_packet_frequency(packets):
    packet_times = [packet.time for packet in packets]
    packet_counter = Counter(packet_times)
    return packet_counter

# Utilizare
try:
    # Capturați pachete timp de 10 secunde (schimbați după necesități)
    captured_packets = capture_packets(duration=20)

    # Calculați frecvența pachetelor
    packet_frequency = calculate_packet_frequency(captured_packets)

    # Afișați rezultatele
    print("Frecvența pachetelor:")
    for timestamp, count in packet_frequency.items():
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}: {count} pachete")

except PermissionError:
    print("Executați acest script cu privilegii de administrator (sudo pe sisteme Unix).")
