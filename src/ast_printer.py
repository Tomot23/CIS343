from Expr import Expr
from scyode_token import Token, TokenType

class AstPrinter(Expr.Visitor):

    def print(self, expr: Expr):
        return expr.accept(self)

    def visit_binary_expr(self, expr: Expr.Binary):
        return AstPrinter.parenthesize(self, expr.operator.lexeme,
                                       expr.left, expr.right)

    def visit_grouping_expr(self, expr: Expr.Grouping):
        return AstPrinter.parenthesize(self, "group", expr.expression)

    @staticmethod
    def visit_literal_expr(expr: Expr.Literal):
        if expr.value is None: return "nil"
        if type(expr.value) is str: return '"' + expr.value + '"'
        return str(expr.value)

    def visit_unary_expr(self, expr: Expr.Unary):
        return AstPrinter.parenthesize(self, expr.operator.lexeme, expr.right)

    def parenthesize(self, name: str, *exprs: Expr):
        s = ""
        s += f"({name}"
        for expr in exprs:
            s += " "
            s += expr.accept(self)
        s += ")"
        return s