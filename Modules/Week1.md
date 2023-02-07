# Week 1 - Simple Static Analysis 
Learned how to use VirusTotal and reading the information after the scan. We also learned PEview, PeID, strings, and DependencyWalker. Checked to see if an item was packed. Learned the format of ASCII and Unicode and how to 

# Lab 1-1

## Executive Summary 
The .exe file can be calling the .dll. There is also network connection probably occuring to 127.26.152.13. 

## Indicators of Compromise
Compilation Date: 2010-12-19 16:16:38 UTC

MD5 HASH (EXE):  bb7425b82141a1c0f7d60e5106676bb1 

MD5 HASH (DLL):  290934c61de9176ad682ffdd65f0a669 


## Mitigations 

## Evidence 
Lab 1.1 consisted of two components, a portable executable (EXE) and a dynamically linked library (dll). By using www.Virustotal.com we can see that the .exe and .dll both set off vendors' virus classifiers. 

By using strings with the .exe file we can see suppose activity. Some keywords that stand out is the last statement says "WARNING_THIS_WILL_DESTROY_YOUR_MACHINE". There is also "c:\windows\system32\kerne132.dll" which replaes the l with a 1. Using this same method, the .dll shows the IP address of 127.26.152.13. 

In the .dll the following functions are found using DependencyWalker: KERNEL32.DLL, WS2_32.DLL, NTDLL.DLL.
In the .exe the following functions are found using DependencyWalker: FindClose, CreateFileA, CloseHandle.

# Lab 1-2 

## Executive Summary 
This file is packed and is connecting to the internet. 

## Indicators of Compromise
PEview Time Date Stamp: 2011/01/19 Web 16:10:41 UTC
MD5:  8363436878404da0ae3e46991e355b83 
SHA-1:  5a016facbcb77e2009a01ea5c67b39af209c3fcb 

In strings the following packatages can be seen
  http://wwareanysisbook.com 
  MalService,
  Int6net Expl!r 8FEI,

The DLL files seen were
  LoadLibraryA
  GetProcAddress
  VirtualProtect
  VirtualAlloc
  VirtualFree
  ExitProcess
  CreateServiceA
  InternetOpenA
  
Dropping it into PeID shows that ijt is a UPX 0.89.6-1.02/1.05-2.90 -> Markus & Laszlo  and
EP Section: UPX1 
  
PEview says that the size of Raw Data is 0  and the virtual size is 400 for UPX0

## Mitigations 

## Evidence 
PeID shows that it is packed with UPX. The size of Raw data is 0 which can indicate that it is packed. 
DependencyWalker shows that there are four functions : KERNEL32.DLL, ADVAPI32.DLL, MSVCRT.DLL, WINNET.DLL. With winnet having the functions InternetOpenUrlA, and InternetOpenA. 

# Lab 1-3

## Executive Summary 
After analyzing the file it can be found that it is malicious. The contentst seem to be packed using FSG. 

## Indicators of Compromise
MD5 -  9c5c27494c28ed0b14853b346b113145 

SHA1 -  290ab6f431f46547db2628c494ce615d6061ceb8 

First Seen In The Wild 2011-03-26 06:54:39 UTC 

## Mitigations 

## Evidence
Opening the file with PeID outputed FSG 1.0 -> dulek/xt. By going through PeView the size of raw data is 0. The rest od the data sets seem off. A quick search leads us to seeing that FSG stands for Fast Small Good which can be used to pack. 

VirusTotal also sets off many flags. 

Running strings lets us see three words : KERNEL32.dll, LoadLibraryA, GetProcAddress.
These libraries can also be found to be used in Dependency Walker. 

No Creation Time Stamp Date. 

# Lab 1-4

## Executive Summary 
This file can be found to be malicious. It is probable that it is writing on a file. 
Seems to be aimed for Intel 386 or later procesessors and compatible processors. 

## Indicators of Compromise
MD5 625ac05fd47adc3c63700c3b30de79ab 

Creation Time 2019-08-30 22:26:59 UTC 

## Mitigations 

## Evidence
PeID shows the file uses Microsoft Visual C++. 

VirusTotal sets off many flags and marks it as malicious. 

The date in VirusTotal and in PeView shows to be 2019/08/30,but was first seen in the wild in 2011/07/05. 

Strings shows three executables : \system32\wupdmgr.exe, \winup.exe, \system32\wupdmgrd.exe. 
The address http://www.practicalmalwareanalysis.com/updater.exe can also be seen. 
Among these are also many functions being called and dlls. 
  CloseHandle
  OpenProcess
  GetCurrentProcess
  GetProcAddress
  LoadLibraryA
  WinExec
  WriteFile
  CreateFileA 
  ... 
  KERNEL32.dll
  AdjustTokenPrivileges
  LoopupPrivilegeValueA
  OpenProcessToken
  ADVAPI32.dll
  MSVCRT.dll
  sfc_0os.dll
  ...
 to list a few. 
DependencyWalker helps verify the usage of KERNEL32.DLL, ADVAPI32.DLL, MSVCRT.DLL
