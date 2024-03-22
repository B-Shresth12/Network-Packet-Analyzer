import scapy.all as scapy

def sniff_packets(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto

        print(f"Source IP: {ip_src} --> Destination IP: {ip_dst} Protocol: {protocol}")

        if packet.haslayer(scapy.Raw):
            payload = packet[scapy.Raw].load
            print(f"Payload: {payload.hex()}")

interface = input("Enter interface to sniff (e.g., eth0): ")

print("\nPacket Sniffing started...\n")
sniff_packets(interface)
