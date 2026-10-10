import sys
sys.path.insert(0, "./src")
from ast_printer import Expr, AstPrinter
from scyode_token import Token, TokenType

expression = Expr.Binary(
    Expr.Unary(
        Token(TokenType.MINUS, "-", None, 1),
        Expr.Literal(123)
    ),
    Token(TokenType.STAR, '*', None, 1),
    Expr.Grouping(
        Expr.Literal(45.67)
    )
)
    
print(AstPrinter().print(expression))