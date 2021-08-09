UVSim - Milestone 3
By Roman Meredith, Jarrett Minton, Joshua Peters, and Alan Whitman

UVSim is a simplified machine language simulator written in Python. Intended as an educational tool, UVSim allows 
users to create simple programs using machine-code-like instructions. Internally, UVSim has 100 memory locations,
which hold both 5-digit instructions, as well as user input. It also has an accumulator register, which is designed
to hold intermediate values when doing computations. Integers are the only data type supported by UVSim, although
there is an instruction that will convert an integer to an ASCII (or unicode) value and print it to the screen (see 
Available Instructions below).

Usage

There are three ways to input a program into UVSim:

1.  Run UVSim from the command line with no command line parameters (e.g. "python uvsim.py" or "python3 uvsim.py"). 
    UVSim will provide a brief set of instructions, after which users can input instructions into sequential memory 
    addresses one at a time. Entering "-999999" will stop input, attempt to validate the program, and if the program 
    is valid, run it. If invalid instructions are found in the program, UVSim will alert

2.  Run a complete program using command line parameters. For example, "python uvsim.py 10050 11050 43" is a valid
    program that will prompt a user for an integer, output the integer, then exit. If UVSim is not able to convert,
    any parameter to an integer (if it has non-numeric characters, for instance), it will abort without validating or 
    running the program. Otherwise, it will attempt to validate and then run the program.

3.  Run a complete program from a file. For example, "python uvsim.py myprogram.bml" will attempt to open a file called 
    myprogram.bml and interpret each line of the file as a single instruction. As with running a program from command
    line parameters, if UVSim is not able to convert any instruction to an ingeger, it will abort.


Available Instructions

UVSim instructions are 5-digit numbers consisting of a 2-digit opcode, as well as a 3-digit operand. The available
instructions are as follows:

10 - READ:      
Prompt the user to input an integer between -9999 and 9999, then store is in the location of the operand.
Example: 10050 will prompt the user to input an integer, then store the result in memory location 50.

11 - WRITE:
Write the value of a memory location to the screen.
Example: 10050 will output the value of memory location 50 to the screen.

12 - WRITEASCII: 
Print the ASCII value (or for larger numbers, the unicode value) of a given memory location to the screen.
Example: Assuming that 65 is stored in memory location 50, 12050 will print "A" to the screen.

20 - LOAD:
Load the value of a given memory location into the accumulator register.
Example: Assuming that 100 is stored in memory location 50, 20050 will set the accumulator register to 50

21 - STORE:
Store the value of the accumulator register to a given memory location.
Example: Assuming that the value of the accumulator register is 25, 21050 will store 25 in memory locaiton 50.

22 - SETACCUM:
Explicitly sets the accumulator register to the value of the operand.
Example: 22500 will set the accumulator register to 500.

NOTE: For the following four arithmetic instructions, the value in the accumulator is changed, but the value
in the memory location indicated by the operand will remain unchanged.

30 - ADD:
Add the value stored in the memory location indicated by the operand to the accumulator register, and store
the result in the accumulator register.
Example: If the accumulator register holds a value of 8, and memory location location 50 holds a value of 27, 
30050 will set the accumulator to 35.

31 - SUBTRACT:
Subtract the value in the memory location indicated by the operand from the accumulator register, and store
the result in the accumulator register.
Example: If the accumulator register holds a value of 93, and memory location location 50 holds a value of 30, 
30050 will set the accumulator to 63.

32 - DIVIDE:
Divide the value in the accumulator register by the value held in the memory location indicated by the operand.
Note that because UVSim only supports integers, floor division is performed, discarding any decimals. This also 
means negative division can have unexpected results (e.g. -25 // 6 = -5, not -4). Also note that division by 0 
will result in an error message, and the accumulator being set to 0.
Example: If the accumulator register holds a value of 31, and memory location 50 holds a value of 15, 32050 will
set the accumulator to 2.

33 - MULTIPLY:
Multiply the value stored in the memory location indicated by the operand with the accumulator register, and store
the result in the accumulator register.
Example: If the accumulator register holds a value of 4, and memory location 50 holds a value of 15, 33050 will
set the accumulator to 60.
g
40 - BRANCH:
Branch to the memory location indicated by the operand and continue execution of the program.

41 - BRANCHNEG:
Branch to the memory location indicated by the operand if the accumulator register is less than 0, and continue
execution. If the accumulator register is greater than or equal to 0, execution will continue as normal with the 
next consecutive memory location.

42 - BRANCHZERO:
Branch to the memory location indicated by the operand if the accumulator register is equal to 0, and continue
execution. If the accumulator register is not 0, execution will continue as normal with the 
next consecutive memory location.

43 - HALT:
Halt execution of the program.