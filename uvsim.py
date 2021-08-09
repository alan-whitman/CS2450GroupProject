from basicml import BasicML
import sys

def main():
    bml = BasicML()
    read_from_file = False
    if len(sys.argv) > 1:
        try:
            '''
            for i in range(1, len(sys.argv)):
                bml.memory[i - 1] = int(sys.argv[i])
            bml.instruction_counter = len(sys.argv) - 1'''
            with open(sys.argv[1]) as f:
                lines = f.read().splitlines()
                lines = [line for line in lines if line != ""]
                if len(lines) > 100:
                    print("Too many lines of code.")
                    raise Exception("Too many lines of code") 
                else:
                    for i in range(0, len(lines)):
                        bml.memory[i] = int(lines[i])
                    bml.instruction_counter = len(lines) - 1
                    read_from_file = True

        except:
            '''
            print("Unable to convert command line argument to integer. Aborting.")
            exit()'''
            print("Failed to read file." )
            print("Loading main menu...\n\n")
    if not read_from_file:
        bml.initial_prompt()
        while bml.get_next_instruction():
            pass
    bml.save_file()
    print("*** Loading Program... ***")
    program_is_valid = bml.validate_program()
    
    if program_is_valid:
        print("*** Program loading completed ***\n*** Program execution begins ***\n")
        bml.run_program()
        
    else:
        print("*** Program contains invalid instructions. Unable to execute ***")
    
    bml.dump(print)

if __name__ == "__main__":
    main()
