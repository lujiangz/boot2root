
# Initial Access

When I first booted the machine, I couldn't see an IP address as mentioned in the PDF. To establish a connection, I needed to perform a port scan to identify the available ports and determine how to connect to the machine.


```
PS C:\Users\Admin> ipconfig

Windows IP Configuration


Unknown adapter Local Area Connection:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . : TBTNET-TELEKOM
   Link-local IPv6 Address . . . . . : fe80::377f:a9a1:26fe:9665%10
   IPv4 Address. . . . . . . . . . . : 192.168.1.104
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1

Ethernet adapter VMware Network Adapter VMnet1:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::9139:8d26:d933:6bd1%17
   IPv4 Address. . . . . . . . . . . : 192.168.204.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :

Ethernet adapter VMware Network Adapter VMnet8:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::fb43:9fc7:18b0:7d58%12
   IPv4 Address. . . . . . . . . . . : 192.168.193.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :

Ethernet adapter vEthernet (WSL (Hyper-V firewall)):

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::68fe:23eb:4e0f:3731%21
   IPv4 Address. . . . . . . . . . . : 172.17.48.1
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
```


The important part for us here is:

```
Ethernet adapter VMware Network Adapter VMnet8:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::fb43:9fc7:18b0:7d58%12
   IPv4 Address. . . . . . . . . . . : 192.168.193.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :
```

After that, I used nmap to scan the ports:

```
luji~:nmap 192.168.193.0/24
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-17 08:02 +03
Nmap scan report for 192.168.193.128
Host is up (0.18s latency).
Not shown: 994 closed tcp ports (conn-refused)
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
143/tcp open  imap
443/tcp open  https
993/tcp open  imaps

Nmap done: 256 IP addresses (1 host up) scanned in 3.93 seconds
```

