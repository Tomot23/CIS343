import sys
sys.path.insert(0, "./src")
from ast_printer import Expr, AstPrinter
from scyode_token import Token, TokenType

expression = Expr.Binary(
    Expr.Literal("nil"),
    Token(TokenType.BANG_EQUAL, "!=", None, 1),
    Expr.Literal(None)
)

print(AstPrinter().print(expression))