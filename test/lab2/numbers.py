import sys
sys.path.insert(0, "./src")
from ast_printer import Expr, AstPrinter
from scyode_token import Token, TokenType

expression = Expr.Binary(
    Expr.Binary(
        Expr.Literal(10),
        Token(TokenType.PERCENT, "%", None, 1),
        Expr.Literal(3)
    ),
    Token(TokenType.LESS_EQUAL, "<=", None, 1),
    Expr.Binary(
        Expr.Binary(
            Expr.Literal(9),
            Token(TokenType.SLASH, "/", None, 1),
            Expr.Literal(7)
        ),
        Token(TokenType.LESS, "<", None, 1),
        Expr.Binary(
            Expr.Binary(
                Expr.Binary(
                    Expr.Literal(5),
                    Token(TokenType.STAR, "*", None, 1),
                    Expr.Literal(3)
                ),
                Token(TokenType.PLUS, "+", None, 1),
                Expr.Literal(4)
            ),
            Token(TokenType.GREATER, ">", None, 1),
            Expr.Binary(
                Expr.Binary(
                    Expr.Literal(20),
                    Token(TokenType.MINUS, "-", None, 1),
                    Expr.Literal(6)
                ),
                Token(TokenType.GREATER_EQUAL, ">=", None, 1),
                Expr.Binary(
                    Expr.Literal(29),
                    Token(TokenType.DOUBLE_SLASH, "//", None, 1),
                    Expr.Literal(2)
                )
            )
        )
    )
)

print(AstPrinter().print(expression))