
# Week 3  Basic Dynamic Analysis

Analysing malware after execution is Dynamic Analysis, which helps us understand what the malware is doing. In order to do this, it is important that the envirionment that the malware is being run on is secure and separated from the network(sandbox). Static Analysis is still complete first before attempting dynamic.  
# Lab 3-1

## Executive Summary 
 Lab03-01.exe has been found to be malware. Running the .exe file wil replicate itself to another file. The replicated file has network functionality. 

## Indicators of Compromise

C:\Windows\System32\vmx32to64.exe 
Reg Key: HKLM\Software\Microsoft\Windows\CurrentVersion\Run\VideoDriver

## Mitigations 
Unsure of how to remove. 

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
 Lab03-02 has been found to be malware. Installs as a service: IPRIP. Communicates with practicalmalwareanalysis.com/serve.html. 


## Indicators of Compromise

Reg Key: %CurrentDirectory%\Lab03-02.dll. 
File: serve.html
String: Intranet Network Awareness (INA+). 
## Mitigations 

Unsure of how to remove. 
## Evidence 
### Static Analysis 
File is packed and requiers deeper analysis. 

### Dynamic Analysis 
Comparing both shots of the regshot revealed that 6 keys had been added. : HKLM\System\ControlSet001\Services\IPRIP, HKLM\System\ControlSet001\Services\IPRIP\Parameters, HKLM\System\ControlSet001\Services\IPRIP\Security,HKLM\System\CurrentControlSet\Services\IPRIP,HKLM\System\CurrentControlSet\Services\IPRIP\Parameters, HKLM\System\CurrentControlSet\Services\IPRIP\Security. 
Procmon shows many readfiles and RegOpenKey for PID 1080 connected to svchost.exe. 
Many of the strings located can be seen in the comparison of the remshot. 
Below it can be seen that the ImagePath was set to "%SystemRoom%\System32\svchost.exe -k netsvcs". As well as a DisplayName: stating "Intranet Network Awareness (INA+)".  Using the command line we can run C:\WINDOWS\system32\svhost.exe -k netsvcs or [net start IPRIP]  after running rundll32.exe Lab03-02, InstallA.
Wireshark shows connections leading to http://practicalmalwareanalysis.com/serve.htmll. 

# Lab 3-3

## Executive Summary 
Lab 03-03 has been found to be malware. Creates the log file : practicalmalwareanalysis.log. Found to be keylogger. 


## Indicators of Compromise
A svchost.exe file that has no parent or the parent of Lab03-03.exe. 
File: practicalmalwareanalysis.log


## Mitigations 

Unsure of how to remove. 

## Evidence 
### Static Analysis
PeID only shows kernel32.dll. And running strings does not show anything useful, mostly a bunch of A's. 

### Dynamic Analysis 
When running Lab03-03 the file executed alongside with a svchost.exe. This svchost.exe was left behind after Lab3 was executed.  
RegShot shows 6 added keys: \Software\Sysinternals\Process Explorer\ : ending with DllColumnMap, Dllcolumns, HandleColumnMap , HandleColumns, ProcessColumnMap, ProcessColumns. a DbgHelpPat: "C:\WINDOWS\system32\dbghelp.dll" was also found. 
Strings inside Process Explorer reveals some intereting characters: practicalmalwareanalysis.log , [SHIFT],[ENTER], [BACKSPACE],BACKSPACE, [TAB], [CTRL], [DEL],and [CAPS LOCK]. These were found in the Memory. The Image revelase nothing suspicious.
Wireshark reveals a request to http://sa.windows.com/sasearch / lclsrch.smll. 

Since we know the PID (1476)  of svchost.exe we'll filter for it in Wirshark. We located a WriteFile with that PID. Following the path led to the .log file that was revealed in the strings. The .log file located on the desktop revealed that it was loggint the keys that were inputted as well as stating where they were inputted.

