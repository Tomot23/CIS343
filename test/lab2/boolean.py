import sys
sys.path.insert(0, "./src")
from ast_printer import Expr, AstPrinter
from scyode_token import Token, TokenType

expression = Expr.Binary(
    Expr.Unary(
        Token(TokenType.BANG, "!", None, 1),
        Expr.Literal("true")
    ),
    Token(TokenType.EQUAL_EQUAL, "==", None, 1),
    Expr.Binary(
        Expr.Literal("false"),
        Token(TokenType.BANG_EQUAL, "!=", None, 1),
        Expr.Literal("false")
    )
)

print(AstPrinter().print(expression))