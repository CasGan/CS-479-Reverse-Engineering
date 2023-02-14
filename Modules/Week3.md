
# Week 3  Basic Dynamic Analysis

Summary of week learning

# Lab 3-1

## Executive Summary 
 ---- Most Important Takeaway ----


## Indicators of Compromise

---- What to look for if you're infected -----

## Mitigations 

---- how you discovered anything that could be used to fix this infection ------

## Evidence 
### Static Analysis
Running strings we find suspicious strings to indicate network activity. For example, CONNECT %s:%i HTTP/1/0, www.practicalmalwareanalysis.com ,SOFTWARE\Classes\http\shell\open\commandU, Software\Mircrosoft\Active\Installed Components\test and kernal32.dll. More interesting strings include: VideoDriver, WinUMX32-, vmx32to64.exe, SOFTWARE\Mircrosoft\Windows\CurrentVersion\Run
Leading us to believe that it is connecting to the network and running some form of program. 
Kernal32.dll also makes an appearance in DependencyWalker. 
PeID reveals that it has been packed with PEncrypt 3.1 Final -> junkcode. 
With a timestamp of 2008/01/06 shown by PeView. 

### Dynamic Analysis 
Using ProcMon we can locate that Lab03-01.exe : WriteFile C:\\WINDOWS\system32\vmx32to64.exe : SUCCESS. Where vmx32to64 was found usings strings. SOFTWARE\Mircrosoft\Windows\CurrentVersion\Run was also located along with one that is running VideoDriver. 
Closer examination of the 
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\VideoDriver and WINDOWS\system32\vmx32to64.exe reveal they both have the same thread, parent PID, and PID. 
Using Prcoess Explorer and going through the handle we can located another string WinVMX32 which is showing as a mutant : \BaseNamedObjects\WinVMX32. 
WireShark reveals queries being made to www.practicalmalwareanalysis.com.
 

# Lab 3-2

## Executive Summary 
 ---- Most Important Takeaway ----


## Indicators of Compromise

---- What to look for if you're infected -----

## Mitigations 

---- how you discovered anything that could be used to fix this infection ------

## Evidence 
### Static Analysis


### Dynamic Analysis 
Comparing both shots of the regshot revealed that 6 keys had been added. : HKLM\System\ControlSet001\Services\IPRIP, HKLM\System\ControlSet001\Services\IPRIP\Parameters, HKLM\System\ControlSet001\Services\IPRIP\Security,HKLM\System\CurrentControlSet\Services\IPRIP,HKLM\System\CurrentControlSet\Services\IPRIP\Parameters, HKLM\System\CurrentControlSet\Services\IPRIP\Security. 
Below it can be seen that the ImagePath was set to "%SystemRoom%\System32\svchost.exe -k netsvcs". As well as a DisplayName: stating "Intranet Network Awareness (INA+)". 

Procmon shows many readfiles and RegOpenKey for PID 1148 connected to svchost.exe. 

# Lab 3-3

## Executive Summary 
 ---- Most Important Takeaway ----


## Indicators of Compromise

---- What to look for if you're infected -----

## Mitigations 

---- how you discovered anything that could be used to fix this infection ------

## Evidence 
### Static Analysis


### Dynamic Analysis 
----- How do you find each of the above? ( the steps/work to get there ) 
