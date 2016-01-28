from scapy.all import *

# callback for each captured packet
def packet_callback(packet):
    print(packet.show())

# start the sniffer
sniff(prn=packet_callback, count=1)