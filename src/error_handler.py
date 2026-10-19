import sys
from scyode_token import Token, TokenType

class ErrorHandler:
    had_error = False

    @staticmethod
    def error(line,message):
        ErrorHandler.report(line,"",message)

    @staticmethod
    def report(line, where, message):
        print(f"[line {line}] Error{where}: {message}")
        ErrorHandler.had_error = True

    @staticmethod
    def error(token: Token, message: str):
        if token.type == TokenType.EOF:
            ErrorHandler.report(token.line, " at end", message)
        else:
            ErrorHandler.report(token.line, " at '" + token.lexeme + "'", message)