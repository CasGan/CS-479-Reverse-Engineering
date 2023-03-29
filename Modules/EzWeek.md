# EZCRACKME1
Running the ezcrackme1 file prompts for a password input. 

The wrong password input will return with: 
  "Your password <pswd input> was incorrect. Time for some more RE ..."
  
To learn more we run the file in strings and went through the ouput. Among the output the string
  "pickklecucumber1337" can be found just above a the string stating "First Password". 
  
  Testing that "picklecucumber1337" as the password we receive the following output: 
  " You cracked me! Now make a keygen!"
  
# EZCRACKME2

# EZCRACKME3
  Running the ezcrackme1 file prompts for a password input.
  To learn more we run the file in strings and went through the ouput. Among the outputs certain strings stand out: strawberry, kiwi, strlen, and strcat. 
  
  With this information an attempt to a password can be made by concatenating the two words: strawberry and kiwi. 
  It was a succes with "strawberrykiwi". The success output shows as : 
    "You cracked me! Now make a keygen!".
  
  
  To learn 
  
# ControlFlow1
  In order to crack Controlflow1 it had to be opened in ghidra. The sink was traced following the input. The functions observed then were Scissor, Paper, Rock. The Rules discovered where: 
  1. 16th char need be * 
  2. 2nd char must be 6
  3. 1st char is A 
  4. 8th char is ‘%’
  5. 4th char must be 2
  6. Pwd length must be >= 16th 

  
  ### Permalink to key generator.
https://github.com/CasGan/CS-479-Reverse-Engineering/blob/main/Modules/keygen/controlflow1/gen.py
  
# ControlFlow2-1
  
   In order to crack Controlflow1 it had to be opened in ghidra. The sink was traced following the input. The functions observed then were Scissor, Paper, Rock. The Rules discovered where: 
  main -> rock -> paper -> scissors->lizard->spock
  1. Pwd length must be > 16th
  2. 11th character must be '*'
  3. 13th character must be '6'
  4. 10th character must be 'A'
  5. 6th character must be 'Y'
  6. 8th character must be '#' 

  ### Permalink to key generator.
  https://github.com/CasGan/CS-479-Reverse-Engineering/blob/a2f733360c8f3a13896182febf37920c78ddccc2/Modules/keygen/controlflow2_1/gen.py
