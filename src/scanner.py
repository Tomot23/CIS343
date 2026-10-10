from error_handler import ErrorHandler
from scyode_token import Token
from token_type import TokenType

class Scanner:

    def __init__(self, source: str):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []
        self.keywords = {
            "and": TokenType.AND,
            "class": TokenType.CLASS,
            "else": TokenType.ELSE,
            "false": TokenType.FALSE,
            "for": TokenType.FOR,
            "fun": TokenType.FUN,
            "if": TokenType.IF,
            "nil": TokenType.NIL,
            "or": TokenType.OR,
            "print": TokenType.PRINT,
            "return": TokenType.RETURN,
            "super": TokenType.SUPER,
            "this": TokenType.THIS,
            "true": TokenType.TRUE,
            "var": TokenType.VAR,
            "while": TokenType.WHILE
        }

    def at_source_end(self):
        return self.current >= len(self.source)

    def advance(self):
        adv = self.source[self.current]
        self.current += 1
        return adv

    def match(self, expected):
        if self.at_source_end(): return False
        if self.source[self.current] != expected: return False

        self.current += 1
        return True

    def peek(self, length: int = 1, end: bool = False):
        if self.at_source_end(): return '\0'
        if self.current + length - 1 >= len(self.source):
            if end: return '\0'
            return self.source[self.current:]
        if end: return self.source[self.current + length - 1]
        return self.source[self.current: self.current + length]

    def skip(self, length: int):
        for _ in range(length): 
            if not self.at_source_end(): 
                self.advance() 

    def string(self):
        s = ""
        while (self.peek() != '"' and not self.at_source_end()):
            if self.peek() == '\n': self.line += 1
            if self.peek() == '\\':
                match self.peek(2):
                    case '\\t': s += "\t"
                    case '\\n': s += "\n"
                    case '\\\\': s += "\\"
                    case '\\"': s += "\""
                    case _:ErrorHandler.error(self.line, "Unrecognized escape sequnce")
                self.skip(2)
            else:
                s += self.advance()

        if self.at_source_end():
            ErrorHandler.error(self.line, "Unterminated string")
            return

        self.advance()
        self.add_token(TokenType.STRING, s)

    def number(self):
        while self.is_digit(self.peek()): self.advance()

        if (self.peek() == '.' and self.peek(2, True)):
            self.advance()
            while self.is_digit(self.peek()): self.advance()

        self.add_token(TokenType.NUMBER, float(self.source[self.start:self.current]))

    def identifier(self):
        while self.is_alphanumberic(self.peek()): self.advance()

        text = self.source[self.start: self.current]
        if text in self.keywords:
            type = self.keywords[text]
        else:
            type = TokenType.IDENTIFIER
        self.add_token(type)
    
    def is_digit(self, c):
        return '0' <= c <= '9'

    def is_alpha(self, c):
        return ('a' <= c <= 'z' or
                'A' <= c <= 'Z' or
                c == '_')

    def is_alphanumberic(self, c):
        return self.is_alpha(c) or self.is_digit(c)

    def add_token(self, type: TokenType, literal: object = None):
        text = self.source[self.start: self.current]
        self.tokens.append(Token(type, text, literal, self.line))
    
    def scan_tokens(self):
        while not self.at_source_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()
        match c:
            # Single character
            case '(': self.add_token(TokenType.LEFT_PAREN)
            case ')': self.add_token(TokenType.RIGHT_PAREN)
            case '{': self.add_token(TokenType.LEFT_BRACE)
            case '}': self.add_token(TokenType.RIGHT_BRACE)
            case ',': self.add_token(TokenType.COMMA)
            case '.': self.add_token(TokenType.DOT)
            case '-': self.add_token(TokenType.MINUS)
            case '+': self.add_token(TokenType.PLUS)
            case ';': self.add_token(TokenType.SEMICOLON)
            case '*': self.add_token(TokenType.STAR)
            case '%': self.add_token(TokenType.PERCENT)

            # Possible multi-characters
            case '!':
                self.add_token(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
            case '=':
                self.add_token(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
            case '<':
                self.add_token(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
            case '>':
                self.add_token(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
            case '/':
                self.add_token(TokenType.DOUBLE_SLASH if self.match('/') else TokenType.SLASH)
            case '@':
                if self.match('=') and self.match('='): 
                    while (not self.at_source_end() and self.peek(3) != '==@'):
                        if self.match('\0'): print(1)
                        elif self.match('\n'): self.line += 1
                        else: self.advance()
                    if self.peek(3) == '==@':
                        self.skip(3)
                    else: ErrorHandler.error(self.line, "Unterminated comment")
                else:
                    while (self.peek() != '\n' and not self.at_source_end()): 
                        self.advance()

            # Whitespace
            case ' '|'\r'|'\t': pass
            case '\n': self.line += 1

            # Literals
            case '"': self.string()
            case _: 
                if self.is_digit(c):
                    self.number()
                elif self.is_alphanumberic(c):
                    self.identifier()
                else:
                    ErrorHandler.error(self.line, "Unexpected character")