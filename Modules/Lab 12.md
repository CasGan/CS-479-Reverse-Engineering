# Detecting DLL Injection 

## 1) Prove that the loader is using DLL injection. (Don't forget a relevant snapshot in Ghidra.)
We believe the loader is using dll injection because it is passing "s_Lab-01.dll". This occurs in an area where the process is being opened, a handle implemented, with allocating virtual memeory and using WriteProcessMemeory with CreateRemoteThread to write the file in. 

![image](https://user-images.githubusercontent.com/89425242/233742308-1841444e-a6d3-4ae7-a2b1-405e91a84cd7.png)


## 2) Identify the process that will be injected into. Seeing a string in Ghidra isn't sufficient -- explain how the process gets selected.


![image](https://user-images.githubusercontent.com/89425242/233481193-e4a12896-4269-4fe6-abfb-a2852dd14828.png)


## 3) Identify the entry point of the DLL injection. Where is DllMain?


![image](https://user-images.githubusercontent.com/89425242/233480263-f81e35df-0799-4998-b10e-b54e719e330a.png)


## 4) This malware does something every ______ seconds. How often, and where is the loop where that waiting happens?
Creates a messabebox that as you to press okay in order to reboot. 

![image](https://user-images.githubusercontent.com/89425242/233745364-dd22307e-16dd-4e8a-b0b2-4ba205ad13fa.png)


## 5) What does the malware do every _______ seconds?
it Sleeps(6000) therefore 60 seconds. 
![image](https://user-images.githubusercontent.com/89425242/233745352-179c2928-c488-4030-88d9-451a1adf597e.png)

