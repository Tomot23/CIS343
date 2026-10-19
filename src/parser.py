from scyode_token import Token, TokenType
from Expr import Expr
from error_handler import ErrorHandler

class Parser:
    class ParseError(RuntimeError): pass

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        try:
            return self.expression()
        except Parser.ParseError:
            return None

    def expression(self):
        return self.equality()

    def equality(self):
        expr = self.comparison()

        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Expr.Binary(expr, operator, right)

        return expr

    def comparison(self):
        expr = self.term()

        while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, 
                         TokenType.LESS, TokenType.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = Expr.Binary(expr, operator, right)

        return expr

    def term(self):
        expr = self.factor()

        while self.match(TokenType.PLUS, TokenType.MINUS):
            operator = self.previous()
            right = self.factor()
            expr = Expr.Binary(expr, operator, right)

        return expr

    def factor(self):
        expr = self.unary()

        while self.match(TokenType.SLASH, TokenType.STAR,
                         TokenType.DOUBLE_SLASH, TokenType.PERCENT):
            operator = self.previous()
            right = self.unary()
            expr = Expr.Binary(expr, operator, right)

        return expr

    def unary(self):
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Expr.Unary(operator, right)

        return self.primary()

    def primary(self):
        if self.match(TokenType.FALSE): return Expr.Literal(False)
        if self.match(TokenType.TRUE): return Expr.Literal(True)
        if self.match(TokenType.NIL): return Expr.Literal(None)

        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Expr.Literal(self.previous().literal)

        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression")
            return Expr.Grouping(expr)

        raise self.error(self.peek(), "Expect expression")

    def match(self, *types: TokenType):
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False

    def consume(self, type: TokenType, message: str):
        if self.check(type): return self.advance()

        raise self.error(self.peek(), message)

    def check(self, type: TokenType):
        if self.is_at_end(): return False
        return self.peek().type == type

    def advance(self):
        if not self.is_at_end(): self.current += 1
        return self.previous()

    def is_at_end(self):
        return self.peek().type == TokenType.EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def error(self, token: Token, message: str):
        ErrorHandler.error(token, message)
        return Parser.ParseError()

    def sychronize(self):
        self.advance()

        while not self.is_at_end():
            if self.previous().type == TokenType.SEMICOLON: return

            match self.peek().type:
                case TokenType.CLASS: pass
                case TokenType.FUN: pass
                case TokenType.VAR: pass
                case TokenType.FOR: pass
                case TokenType.IF: pass
                case TokenType.WHILE: pass
                case TokenType.PRINT: pass
                case TokenType.RETURN: return

            self.advance()