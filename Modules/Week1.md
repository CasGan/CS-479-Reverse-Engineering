# Week 1 - Simple Static Analysis 
Learned about 

Analyze the file Lab02–02.exe
Question

# Lab 1-1

## Executive Summary 


## Indicators of Compromise
Compilation Date: 2010-12-19 16:16:38 UTC

MD5 HASH (EXE):  bb7425b82141a1c0f7d60e5106676bb1 

MD5 HASH (DLL):  290934c61de9176ad682ffdd65f0a669 


## Mitigations 

## Evidence 
Lab 1.1 consisted of two components, a portable executable (EXE) and a dynamically linked library (dll). By using www.Virustotal.com we can see that the .exe and .dll both set off vendors' virus classifiers. 

By using strings with the .exe file we can see suppose activity. Some keywords that stand out is the last statement says "WARNING_THIS_WILL_DESTROY_YOUR_MACHINE". There is also "c:\windows\system32\kerne132.dll" which replaes the l with a 1. 


# Lab 1-2 

## Executive Summary 

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
