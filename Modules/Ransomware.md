# ransomeware1 

This file is a ransomware. Analyzing it with ghidra the string "lumpy_cactus_fruit" can be seen.
Inputting that string reveals it to be the password to decrypt the encryption. 
By further analysing the file we can see the function decrypt(). Which informs us that it is xor-ing each 
char in the file by "0x34". 

![Image of Ransomware1](Modules/Resources/ransomware1.png)

A Decryptor has been made in order to not have to pay the ransom. 
https://github.com/CasGan/CS-479-Reverse-Engineering/blob/ac3dfe41d187d7f75e9f413e2f943ed1d1a9a44f/Modules/decryptor/ransomware1_decryptor.py

In order to run it, pass two files 1) the secret.txt (encrypted file) and 2) no_secret.txt (empty file for writting). Make sure these files are in the same directory. 


# rasomware2
This file is a ransomware and has locked important files. 
Upon executing a password is requested and a failed input prompts the user to pay the ransom. 
Expecting this program in ghidra we find the password which is "delicious". 





