## Module 6 Networking with Linux
## TASK 6.1


1. Create virtual machines connection according to figure 1

![Image description](./img/1.png)

2. VM2 has one interface (internal), VM1 has 2 interfaces (NAT and internal). Configure  all network interfaces in order to make VM2 has an access to the Internet (iptables, forward, masquerade).

nat and internal setup:
![Image description](./img/4.png)

ssh connection from host:
![Image description](./img/5.png)  

ip a:
![Image description](./img/2.png)

netplan configuration:
![Image description](./img/3.png)

iptables for vm1:
![Image description](./img/6.png)

internet connection for vm2:
![Image description](./img/7.png)

route:
![Image description](./img/8.png)

nslookup 8.8.8.8:
![Image description](./img/9.png)

epam:
![Image description](./img/10.png)

routing tables:
![Image description](./img/11.png)

gateway default:
![Image description](./img/12.png)

traceroute:
![Image description](./img/13.png)
