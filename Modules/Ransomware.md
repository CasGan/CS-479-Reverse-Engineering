# ransomeware1 

This file is a ransomware. Analyzing it with ghidra the string "lumpy_cactus_fruit" can be seen.
Inputting that string reveals it to be the password to decrypt the encryption. 
By further analysing the file we can see the function decrypt(). Which informs us that it is xor-ing each 
char in the file by "0x34". 

![Image of Ransomware1](Modules/Resources/ransomware1.png)


# rasomware2




