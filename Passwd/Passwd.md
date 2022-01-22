# KCTF-Passwd

KniightCTF2022 - Cryptography - Passwd - WriteUp

Challenge Link: https://knightctf.com/challenges#Passwd-3

Authors: Rina RANARISON (loonatic) https://knightctf.com/users/724

So it very easy

The flag is the "knight" user's password, we just need to look at the "passwd" file

![image](https://user-images.githubusercontent.com/45909337/150625528-4694307a-79ab-47c0-9bc3-e0cc62083c61.png)

At the bottom of the file we can see the "knight" user's password and as we know it's MD5 hash

I use https://www.md5online.org/md5-decrypt.html to see if we can get the decrypted version of the hash

![image](https://user-images.githubusercontent.com/45909337/150625576-57e94f55-7e81-4e0a-9a8f-a0464ee0e815.png)

As wee can see, this found out that "708697c63f7eb369319c6523380bdf7a = exploit"

Then the flag is : KCTF{exploit}

PS: If you don't know or not sure, what kind of hash it is, you can use https://hashes.com/en/tools/hash_identifier to identify the hash type
![image](https://user-images.githubusercontent.com/45909337/150625632-0a4d9fbf-ef87-44bb-8d6e-51f20d7d1339.png)

