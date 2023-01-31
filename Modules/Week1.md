# Week 1 - Simple Static Analysis 
Learned about 

## Executive Summary Lab 1–2

Analyze the file Lab02–02.exe
Question

# Lab 1-1

## Indicators of Compromise

## Mitigations 

## Evidence 
Using www.virustotal.com

Using PEview

Using 


# Lab 1-2 

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
