# Week 5: 

## Decryptme#1 

In order to run the EXE file we'll need to download wine. After executing Decryptme#1.exe a 
pop up was presented asking for a key as input. 
Input: 12234567899
Output: ennUoheU.U;ohgtvunvaohkUUU [weird output]
Going through the code we find two instances where MessageBoxA can be seen. The second one is interesting. It contains local_14, local_c, local_8, and local_10. However, local__8 is the only one that has int FUN_00013c94(char * param_1). 
Following local_8 we notice it references twice. Going to the first reference we can see LEA (Load Effective Address). Leading us to believe that the address was computed and register changed. We will be assuming that FUN_00013c94 to be the function that is encrypting. 
By looking inside the function we can see that iVar2 is set to FUN_000130f0((int)param_1). Now we have to go take a look at that function to see what is happening inside our encrypting function. Looking into that function, it doesn't seem to push or change anything. 
