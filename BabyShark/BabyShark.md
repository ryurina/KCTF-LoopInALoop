# KCTF-BabyShark

KniightCTF2022 - Reverse Engineering - BabyShark - WriteUp

Challenge Link: https://knightctf.com/challenges#Baby%20Shark-38

Authors: Rina RANARISON (loonatic) https://knightctf.com/users/724

## Step 1
Download the file "babyshark.jar"
## Step 2 
Open it with "JD-GUI" (Download it here: https://java-decompiler.github.io/" if you don't have it)
## Step 3
Look for something interesting like "eg: flag"
![image](https://user-images.githubusercontent.com/45909337/150625335-fd643da2-59bf-41eb-ab69-2d486daa54ec.png)
But unfortunately, it wasn't the flag so we need to look for more interesting stuffs.

I clicked on "constants > strings.class" and found this:
![image](https://user-images.githubusercontent.com/45909337/150625359-9f943e6e-d196-4f59-8da0-45b2b0e48b79.png)

It's base64 so I decode all of them and found out that

```
S0NURns3SDE1X1dANV8zNDVZX1IxNkg3P30=
```
was the flags

I decoded by using https://www.base64decode.org/

And I got the flag: KCTF{7H15_W@5_345Y_R16H7?}
