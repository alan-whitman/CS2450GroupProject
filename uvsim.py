from basicml import BasicML

def main():
    bml = BasicML()
    bml.initial_prompt()
    while bml.get_next_instruction():
        pass
    bml.run_program()
    bml.dump()

if __name__ == "__main__":
    main()