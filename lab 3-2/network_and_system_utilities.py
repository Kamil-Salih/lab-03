# IP and Hostname Tools
import socket
print(socket.gethostbyname('example.com'))  # print the resolved IP address

# IP Address Math
import ipaddress
net = ipaddress.ip_network('192.168.1.0/24')
print(list(net.hosts())[:3])  # print the first 3 host addresses

# System Info
import platform
print(platform.uname())  # print full system info

# Exercise: print hostname and kernel version
u = platform.uname()
print(f'Hostname: {u.node}, Kernel: {u.release}')
