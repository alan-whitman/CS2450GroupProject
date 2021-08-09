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
11 - WRITE:
12 - WRITEASCII:
20 - LOAD:
21 - STORE:
22 - SETACCUM:
30 - ADD:
31 - SUBTRACT:
32 - DIVIDE:
33 - MULTIPLY:
40 - BRANCH:
41 - BRANCHNEG:
42 - BRANCHZERO:
43 - HALT: