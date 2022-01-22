# KCTF-RunTheProgram

KniightCTF2022 - Programming - RunTheProgram - WriteUp

Challenge Link: https://knightctf.com/challenges#Run%20The%20Program-76

Authors: Rina RANARISON (loonatic) https://knightctf.com/users/724

In this challenge, we just need to compile and run this program
```asm
.MODEL SMALL
.DATA
    MAIN PROC
        MOV AH,2
        MOV DL,80
        SUB DL, 5
        INT 21H
        MOV DL, 70
        SUB DL, 3
        INT 21H
        MOV DL, 100
        SUB DL, 16
        INT 21H
        MOV DL, 100
        SUB DL, 30
        INT 21H
        MOV DL, 123
        INT 21H
        MOV DL, 75
        ADD DL, 50
        SUB DL, 60
        INT 21H
        MOV DL, 53
        INT 21H
        MOV DL, 53
        INT 21H
        MOV DL, 147
        SUB DL, 96
        INT 21H
        MOV DL, 80
        SUB DL, 3
        INT 21H
        MOV DL, 255
        MOV DH, 157
        SUB DL, DH
        INT 21H
        MOV DL, 255
        MOV DH, 147
        SUB DL, DH
        INT 21H
        MOV DH, 72
        MOV DL, 17
        ADD DL, DH
        INT 21H

        MOV DL, 130
        SUB DL, 5
        INT 21H


        MOV AH,4CH
        INT 21H

    MAIN ENDP
END MAIN
```

After I google (or duckduckgo) some line of the code, we know that this program is written in MASM (Microsoft Macro Assembler)

### What we need to run this???
- DOSBOX (https://www.dosbox.com/) (or other MS-DOS emulator)
- MASM

### How to run it???
- Rename the file "run.it" to "run.asm"
- Put it into the same folder as MASM
![image](https://user-images.githubusercontent.com/45909337/150626069-86942b8f-2583-4706-a66f-fbc405e0a88e.png)
- Run DOSBOX
- Mount the MASM folder as C: in DOSBOX with the following command:
``` mount c ~/path/to/masm```
- Then type ```c:``` to go to the directory
![image](https://user-images.githubusercontent.com/45909337/150626196-9e860415-dcd9-416d-bbcd-2ec4f8ab01c3.png)
- To compile and run it, type:
```
MASM.EXE RUN.ASM
```
![image](https://user-images.githubusercontent.com/45909337/150626243-76e1c871-2d12-408a-94db-d580ec1b4e2b.png)
- Then enter the following command:
```
LINK.EXE RUN.OBJ
```
Press "Enter"
![image](https://user-images.githubusercontent.com/45909337/150626277-e6ceb94e-794b-4c40-bf73-d013fe24ecf4.png)

- Now run it and get the flag
```RUN.EXE```
![image](https://user-images.githubusercontent.com/45909337/150626288-530c2365-8b33-4be3-9046-bb7d34f2beb5.png)

Flag: KCTF{A553MblY}




