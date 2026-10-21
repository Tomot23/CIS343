import sys
from scyode_token import Token, TokenType
from runtime_error import RuntimeError

class ErrorHandler:
    had_error = False
    had_runtime_error = False

    @staticmethod
    def error(line: int, message: str):
        ErrorHandler.report(line,"",message)

    @staticmethod
    def report(line, where, message):
        print(f"[line {line}] Error{where}: {message}")
        ErrorHandler.had_error = True

    @staticmethod
    def errort(token: Token, message: str):
        if token.type == TokenType.EOF:
            ErrorHandler.report(token.line, " at end", message)
        else:
            ErrorHandler.report(token.line, " at '" + token.lexeme + "'", message)

    @staticmethod
    def runtime_error(error: RuntimeError):
        print(str(error) + "\n[line " + str(error.token.line) + "]")
        ErrorHandler.had_runtime_error = True