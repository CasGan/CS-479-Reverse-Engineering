# Week 4 

## Questions 

   #### - What is the difference between machine code and assembly?
   Machine code tells the processor what to do with hexadecimal digits known as opcodes. When a high level language is compiled by a program it creates the machine code. 
   Assembly is a human-readable version of the intruction set given to the computer.  
   Assembly langugage tends to be a reliable way to recover from machine code. Since machine code is too difficult to understand assembly is used. 
    
   #### - If the ESP register is pointing to memory address 0x001270A4 and I execute a `push eax` instruction, what address will ESP now be pointing to?
   Pushing that instruction to the stack will change the stack pointer (ESP) to the memory address of 0x001270A0. This is since a the instruction pushed a 4-byte value the pointer needs to decrement to use the next location on the stack. 
    
  #### - What is a stack frame?
  The stack is a datastructure where items are pushed on the stack and popped off the stack. It has a last in, first out (LIFO) strucutre. It is used for short term storage with the primary use of managing data echanges between function calls. The stack is the memory for functions, local variables, parameters, flow control, and return address. The stack pointer is ESP and it contains the memory address of the top of the stack. The base pointer is EBP which the program uses as a placeholder to track the local variables and parameters. 
  
  #### - What would you find in a data section?
  Data section is composed of static and global values that are placed when a program is loaded. 
    
  #### - What is the heap used for?
  The heap, also known as dynamic memory, is used for dynamic memory. It creates new values and frees the values that are no longer needed. 
  
   #### - What is in the code section of a program's virtual memory space?
   The code section controls what the program will do and how the tasks will be done. This is what the CPU fetches when the program is executed in order to execute them. 
   
   #### - What does the `inc` instruction do, and how many operands does it take?
   The inc  instruction increments the value of a register or memory location by 1. Thi instruction is ran by inc reg_name and therefore only has one operand. It increments the register/memory location and does not need to store the result in a separate destination operand. 
   
   #### - If I perform a `div` instruction, where would I find the remainder of the binary division (modulo)?
   After the division of EDX and EAX by 'value' the remainder is stored in EDX. EAX gets to store the result of the division operation. To use the remainder use the operation: modulo.
   
   ####  - How does `jz` decide whether to jump or not?
    
  ####  - How does `jne` decide whether to jump or not?
    
  #### - What does a `mov` instruction do?
  The mov instruction moves data from one location to another. It can move the data into registers or the RAM. It is the instruction for reading and writing to memory. 
  
  #### - What does the `TF` flag do and why is it useful for debugging?
  TF stands for trap flag and is used in debugging. What it does is that when the flag is placed then instructioins can only be executed one at a time.
    
  #### - Why would an attacker want to control the EIP register inside a program they want to take control of?
  EIP register (found in x86 architecture) is known as the instruction pointer/program counter. This register contains the memory address of the nex program to be execued. Basically, tells the processor what to do next. 
    An attacker would want to control it because they would gain control of what the CPU executes.
     
    
  #### - What is the AL register and how does it relate to EAX?
   AL references the lower 8 bit (1 byte) of the 32 full bit EAX general register. Note: EAX generally contains the return value of a function call.  
  
  #### - What is the result of the instruction `xor eax, eax` and where is it stored? 
  The instruction : xor eax, eax [bitwise exclusive OR] (XOR) : is for setting the EAX register to zero. The result of zero is stord in the eax register.  
