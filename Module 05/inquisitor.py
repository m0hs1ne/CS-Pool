import argparse
import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in clients_list:
        print(client["ip"] + "\t\t" + client["mac"])
    return clients_list

def main():
    parser = argparse.ArgumentParser(description="wanna poison the ARP?")
    parser.add_argument("-s", "--scan", dest="scan_ip", help="Scan IP")
    parser.add_argument("ipsrc", nargs="?", help="Gateway IP")
    parser.add_argument("marcrc", nargs="?", help="Gateway MAC")
    parser.add_argument("iptarget", nargs="?", help="Target IP")
    parser.add_argument("marctarget", nargs="?", help="Target MAC")
    args = parser.parse_args()

    if args.scan_ip:
        scan(args.scan_ip)
        exit(0)

if __name__ == "__main__":
    main()