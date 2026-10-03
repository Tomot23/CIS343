import sys
from scanner import Scanner
from error_handler import ErrorHandler


class Scyode:
    def run(self, source):
        ErrorHandler.had_error = False
        for token in Scanner(source).scan_tokens():
            print(token)

    # File reading mode
    def run_file(self, path):
        try:
            if path[-3:] != ".vv": raise TypeError
            with open(path) as f:
                file = f.read()
                self.run(file)
            return 65 if ErrorHandler.had_error else 0
        except FileNotFoundError:
            ErrorHandler.error(0, 'File does not exist')
        except NotImplementedError as ni:
            ErrorHandler.error(0,f"{f.name}\n```\n{file}\n```\n", ni)
        except TypeError:
            ErrorHandler.error(0, "Can only run .vv files")

    # REPL mode
    def run_prompt(self):
        print(">>>>> Interactive Shell <<<<<")
        while True:
            try:
                line_call = input(">>> ")
                if line_call == "quit":
                    raise KeyboardInterrupt
                self.run(line_call)
            except (EOFError, KeyboardInterrupt):
                print("..... Exiting Shell .....")
                return 0
            except Exception as e:
                print(e)

def main():
    if len(sys.argv) > 2:
        ErrorHandler.error(0, "Usage: python scyode.py [script]")
        return 64
    scyode = Scyode()
    return scyode.run_file(sys.argv[1]) if len(sys.argv) == 2 else scyode.run_prompt()


if __name__ == "__main__":
    sys.exit(main())