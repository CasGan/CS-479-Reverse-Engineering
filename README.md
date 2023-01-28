# CS 479 Reverse-Engineering at NMSU
## Summary
This repo will hold the reports for the class. The reports will be on reverse engineering malware samples from "Practical Malware Analysis" by Michael Sikorski and Andrew Honig. 
pr
## System Setup
Since malware will be analyzed it is important to isolate it. This isolation will allow for the malware to be contained and prevent it from being dangerous to our device and others on the network. In order to limit it from interacting to our hardware, we implemented a usb. Linux was then downloaded into the USB using [rufus](https://rufus.ie/en/). We proceeded to install the type-2 hypervisor, VirtualBox. Alongside this the windows 10 iso was downloaded which will be implemented in the VirtualBox to open Windows 10. It is important to note that the network for the Windows inside the VirtualBox was disconnected. The external VirtualBox will have to be used for any internet searches. This will make sure that the malware is isolated from the network. 
### **Tools Implemented**: 
