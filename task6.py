# making list for masks
N = int(input())
masks = []
for i in range(N):
    masks.append(input())
# making list for ip
M = int(input())
ip = []
for i in range(M):
    ip.append(input())

# check if each pair of Ip-addresses belong to each mask
for i in range(M):
    Ip1, Ip2 = map(str,ip[i].split())
    IpCount = 0
    # checking if a pair of Ip belongs to the same subnet
    for mask in masks:
        mask = mask.split(".")
        ip1 = Ip1.split(".")
        ip2 = Ip2.split(".")
        Net1 = []
        Net2 = []
        # getting Net-addresses for two Ips. Network octet = Ip octet & Mask octet
        for k in range(len(mask)):
            Net1.append(int(ip1[k]) & int(mask[k]))
            Net2.append(int(ip2[k]) & int(mask[k]))
        # if Net-addresses for 2 Ips the same - 2 Ips belong to the same subnet
        if Net1 == Net2:
            IpCount += 1
    print(IpCount)


