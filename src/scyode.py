import sys

def scanner(input):
    print("Scanner Not Implemented")

if __name__ == "__main__":

    # REPL mode
    if len(sys.argv) == 1:
        print(">>>>> Interactive Shell <<<<<")
        try:
            while True:
                line_call = input(">>> ")
                if line_call == "quit":
                    raise KeyboardInterrupt
                scanner(line_call)
        except KeyboardInterrupt:
            print("..... Exiting Shell .....")

    # File reading mode
    elif len(sys.argv) == 2:
        if sys.argv[1][-3:] != ".vv":
            print("Can only run .vv files")
        else:
            try:
                with open(sys.argv[1]) as f:
                    file = f.read()
                    print(f"{f.name}\n```\n{file}\n```")
                    scanner(file)
            except FileNotFoundError:
                print('File does not exist')
    else:
        print("Usage: ph.py [script]")