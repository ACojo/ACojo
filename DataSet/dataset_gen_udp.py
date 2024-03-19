import csv
import random


def usual_traffic(id_class=0):
    traffic = []
    weights = [0.7, 0.3]  # the weights for the IP source/destination
    weights_flags = [0.3, 0.3, 0.1, 0.3]
    traffic.append(random.randint(12, 25))  # the time
    traffic.append((random.randint(500, 1500)))  # the required space

    # the method choices returns a list
    traffic.append(random.choices([0, 1], weights)[0])  # the  IP destination
    traffic.append(random.choices([0, 1], weights)[0])  # the  IP source
    for index in range(0, 8):  # the destination port
        traffic.append(random.choices([250, 500, 750, 0], weights_flags)[0])  # usual traffic

    for index in range(0, 8):  # the traffic type in/out
        traffic.append(random.choice([0, 750]))

    traffic.append(id_class)  # the class for the normal traffic

    return traffic

# medium pachets but with the same destination port
def gen_amplification_attack( id_class= 3):
    traffic = []
    traffic.append(random.randint(3, 15))  # the time
    traffic.append((random.randint(2500, 6000)))  # the required space
    traffic.append(1)  # the  IP destination
    traffic.append(random.choice([0, 1]))  # the  IP source
    dest_port = random.randint(1, 4)
    for index in range(0, 8):  # the flags
        if dest_port ==1:
            traffic.append(0)  # only a certain port destination 
        elif dest_port ==2:
            traffic.append(250)  # only a certain port destination
        elif dest_port == 3:
            traffic.append(500) # only a certain port destination
        elif dest_port == 4:
            traffic.append(750)  # only a certain port destination
    for index in range(0, 8):  # the traffic type in/out
        traffic.append(random.choice([500, 750]))

    traffic.append(id_class)  # the class for the DoS attack
    return traffic


# for the smurf attack ( same IP source but very huge pachets with the inside
def gen_insider_attack(id_class=2):
    traffic = []
    traffic.append(random.randint(1, 10))  # the time
    traffic.append((random.randint(7500, 9000)))  # the required space
    traffic.append(random.choice([0, 1]))  # the same IP destination
    traffic.append(1)  # the same IP source
    for index in range(0, 8):  # the flags
        traffic.append(random.choice([0, 250, 500, 750]))  # only random destination ports

    for index in range(0, 8):  # the IN method
        traffic.append(0)

    traffic.append(id_class)  # the class for the DoS attack
    return traffic


# function to generate Dos attack
def gen_dos_attack(id_class=1):
    traffic = []
    traffic.append(random.randint(1, 8))  # the time
    traffic.append((random.randint(6000, 9000)))  # the required space
    traffic.append(1)  # the same IP destination
    traffic.append(random.choice([0, 1]))  # the same IP source
    for index in range(0, 8):  # the flags
        traffic.append(500)  # only Syn packets

    for index in range(0, 8):  # the TCP method
        traffic.append(0)

    traffic.append(id_class)  # the class for the DoS attack
    return traffic


with open('udp_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # the header
    writer.writerow(["time_mean", "dimension_mean", "IP_destination", "IP_source", "dest_port1", "dest_port2", "dest_port3",
                     "dest_port14", "dest_port5", "dest_port6", "dest_port7", "dest_port8", "traffic_type1", "traffic_type2", 
                     "traffic_type3", "traffic_type4", "traffic_type5", "traffic_type6", "traffic_type7", "traffic_type8", "class"])

    # ACK = 250
    # SYN = 500
    # ECHO_REQ = 750
    # RESET = 0

    # GET = 250
    # POST = 500
    # PUT = 750
    # DELETE = 0

    for index in range(0, 1000):
        if index % 30 == 0:  # adding the noise
            traffic = gen_insider_attack(1)
            writer.writerow(traffic)
        elif index % 40 == 0:
            traffic = usual_traffic(1)
            writer.writerow(traffic)
        elif index % 50 == 0:
            traffic = gen_amplification_attack(1)
            writer.writerow(traffic)
        else:
            traffic = gen_dos_attack()
            writer.writerow(traffic)

    for index in range(0, 1000):
        if index % 30 == 0:  # adding the noise
            traffic = gen_insider_attack(2)
            writer.writerow(traffic)
        elif index % 40 == 0:
            traffic = usual_traffic(2)
            writer.writerow(traffic)
        elif index % 50 == 0:
            traffic = gen_amplification_attack(2)
            writer.writerow(traffic)
        else:
            traffic = gen_insider_attack()
            writer.writerow(traffic)

    for index in range(0, 1000):
        if index % 30 == 0:  # adding the noise
            traffic = gen_insider_attack(3)
            writer.writerow(traffic)
        elif index % 40 == 0:
            traffic = usual_traffic(3)
            writer.writerow(traffic)
        elif index % 50 == 0:
            traffic = gen_amplification_attack(3)
            writer.writerow(traffic)
        else:
            traffic = gen_amplification_attack()
            writer.writerow(traffic)

    for index in range(0, 2000):
        if index % 30 == 0:  # adding the noise
            traffic = gen_insider_attack(0)
            writer.writerow(traffic)
        elif index % 40 == 0:
            traffic = usual_traffic(0)
            writer.writerow(traffic)
        elif index % 50 == 0:
            traffic = gen_amplification_attack(0)
            writer.writerow(traffic)
        else:
            traffic = usual_traffic()
            writer.writerow(traffic)
    # writer.writerow(lst)
