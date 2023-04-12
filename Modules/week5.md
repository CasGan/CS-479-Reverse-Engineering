# Week 5: 


## Crackme05

Going through the file in ghidra we find 4 functions that are being called: paper(), scissors(), cracker(), rock(). These functions contain statements that if true will go in and trigger a bomb. The bomb is not where we want to arrive therefore we have to get arround the conditions. 

### paper
key[10] ^ key[8] +0x30
key[13] ^ key[5] +0x30

they must be > 0x3a

key[3] != key[10] ^ key[8] +0x30
key[15] !=key[10] ^ key[8] +0x30
### scissors
 key[1 +2] have to be > 0xab 
 key;17 + 16 also have to be > 0xab

### cracker
 key[14],key[4],key[9] != 0x87
### rock
must be 19 characters long 
```
import random

def con_ran(cond, chars):
    stri = ''
    for c in chars:
        if cond(ord(c)):
            stri += c
    return random.choice(stri)

char_options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZY1234567890-"
valid_chars = char_options.encode('ascii')
serial = bytearray(random.getrandbits(8) for _ in range(19))

for i in range(len(serial)):
    if serial[i] < 0:
        serial[i] = -serial[i]
    serial[i] = valid_chars[serial[i] % len(valid_chars)]

serial[4] = 0x2d
serial[9] = 0x2d
serial[14] = 0x2d

serial[8] = con_ran(lambda c: (c ^ serial[10]) <= 9, char_options).encode('ascii')[0]
serial[5] = con_ran(lambda c: (c ^ serial[13]) <= 9, char_options).encode('ascii')[0]

var1 = (serial[10] ^ serial[8]) + 0x30
var2 = (serial[13] ^ serial[5]) + 0x30

serial[3] = var1
serial[15] = var1
serial[0] = var2
serial[18] = var2

serial[1] = con_ran(lambda c: (c + serial[2]) > 170, char_options).encode('ascii')[0]
serial[16] = con_ran(lambda c: (c + serial[17]) > 170 and serial[1] + serial[2] != c + serial[17], char_options).encode('ascii')[0]

print(serial.decode('ascii'))

```
https://github.com/CasGan/CS-479-Reverse-Engineering/blob/529ed26472b71d299c85b89433edd6dcbf1a9d6f/Modules/Resources/Screenshot%20from%202023-04-12%2008-16-07.png


## Decryptme#1 

In order to run the EXE file we'll need to download wine. After executing Decryptme#1.exe a 
pop up was presented asking for a key as input. 
Input: 12234567899
Output: ennUoheU.U;ohgtvunvaohkUUU [weird output]
Going through the code we find two instances where MessageBoxA can be seen. The second one is interesting. It contains local_14, local_c, local_8, and local_10. However, local__8 is the only one that has int FUN_00013c94(char * param_1). 
Following local_8 we notice it references twice. Going to the first reference we can see LEA (Load Effective Address). Leading us to believe that the address was computed and register changed. We will be assuming that FUN_00013c94 to be the function that is encrypting. 
By looking inside the function we can see that iVar2 is set to FUN_000130f0((int)param_1). Now we have to go take a look at that function to see what is happening inside our encrypting function. Looking into that function, it doesn't seem to push or change anything. 
