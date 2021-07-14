from basicml import BasicML

def main():
    bml = BasicML()
    bml.initial_prompt()
    while bml.get_next_instruction():
        pass
    print("*** Loading Program... ***")
    program_is_valid = bml.validate_program()
    if program_is_valid:
        print("*** Program loading completed ***\n*** Program execution begins ***")
        bml.run_program()
    else:
        print("*** Program contains invalid instructions. Unable to execute ***")
    bml.dump()

if __name__ == "__main__":
    main()