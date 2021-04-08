from scapy.all import wrpcap, Ether, IP, UDP, Raw, TCP
from random import seed
from random import randint

PATH_FIRST_FILE = "C:\\Users\\משתמש\\Documents\\school\\סייבר\\blackbox\\packet-{0}.pcap"
seed(1)

for i in range(1, 101):
    path = PATH_FIRST_FILE.format(i)
    packet_list = []
    for i in range(randint(0, 10000)):
        ip_dst = "{0}.{1}.{2}.{3}".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))
        ip_src = "{0}.{1}.{2}.{3}".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))
        packet = Ether() / IP(dst=ip_dst, src=ip_src) / TCP(sport=randint(0, 65535), dport=randint(0, 65535), flags='') / Raw(load='NO')
        packet_list.append(packet)

    wrpcap(path, packet_list)


packet_list = []
for i in range(3021):
    ip_dst = "{0}.{1}.{2}.{3}".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))
    ip_src = "{0}.{1}.{2}.{3}".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))
    packet = Ether() / IP(dst=ip_dst, src=ip_src) / TCP(sport=randint(0, 65535), dport=randint(0, 65535), flags='') / Raw(load='NO')
    packet_list.append(packet)

ip_dst = "{0}.{1}.{2}.{3}".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))
ip_src = "{0}.{1}.{2}.{3}".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))
packet = Ether() / IP(dst=ip_dst, src=ip_src) / TCP(sport=10000, dport=10000, flags='S') / Raw(load='https://blackbox-thebaboons-ap-dc.herokuapp.com/')
packet_list.append(packet)

for i in range(2567):
    ip_dst = "{0}.{1}.{2}.{3}".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))
    ip_src = "{0}.{1}.{2}.{3}".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))
    packet = Ether() / IP(dst=ip_dst, src=ip_src) / TCP(sport=randint(0, 65535), dport=randint(0, 65535), flags='') / Raw(load='NO')
    packet_list.append(packet)

wrpcap(PATH_FIRST_FILE.format(78), packet_list)
