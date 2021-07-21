from basicml import BasicML
import sys

def main():
    bml = BasicML()
    if len(sys.argv) > 1:
        try:
            for i in range(1, len(sys.argv)):
                bml.memory[i - 1] = int(sys.argv[i])
            bml.instruction_counter = len(sys.argv) - 1
        except:
            print("Unable to convert command line argument to integer. Aborting.")
            exit()
    else:
        bml.initial_prompt()
        while bml.get_next_instruction():
            pass
    print("*** Loading Program... ***")
    program_is_valid = bml.validate_program()
    if program_is_valid:
        print("*** Program loading completed ***\n*** Program execution begins ***\n")
        bml.run_program()
    else:
        print("*** Program contains invalid instructions. Unable to execute ***")
    bml.dump()

if __name__ == "__main__":
    main()