from Expr import Expr
from scyode_token import TokenType, Token
from runtime_error import RuntimeError
from error_handler import ErrorHandler

class Interpreter(Expr.Visitor):

    def interpret(self, expression: Expr):
        try:
            value = self.evaluate(expression)
            print(self.stringify(value))
        except RuntimeError as e:
            ErrorHandler.runtime_error(e)

    def visit_binary_expr(self, expr: Expr.Binary):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        match expr.operator.type:
            case TokenType.BANG_EQUAL:
                return not self.is_equal(left, right)
            case TokenType.EQUAL_EQUAL:
                return self.is_equal(left, right)
            case TokenType.GREATER:
                self.check_number_operands(expr.operator, left, right)
                return float(left) > float(right)
            case TokenType.GREATER_EQUAL:
                self.check_number_operands(expr.operator, left, right)
                return float(left) >= float(right)
            case TokenType.LESS:
                self.check_number_operands(expr.operator, left, right)
                return float(left) < float(right)
            case TokenType.LESS_EQUAL:
                self.check_number_operands(expr.operator, left, right)
                return float(left) <= float(right)
            case TokenType.MINUS:
                self.check_number_operands(expr.operator, left, right)
                return float(left) - float(right)
            case TokenType.PLUS:
                if type(left) is float and type(right) is float:
                    return float(left) + float(right)
                if type(left) is str and type(right) is str:
                    return str(left) + str(right)
                raise RuntimeError(expr.operator, "Operands must be two numbers or two strings")
            case TokenType.SLASH:
                self.check_number_operands(expr.operator, left, right)
                return float(left) / float(right)
            case TokenType.DOUBLE_SLASH:
                self.check_number_operands(expr.operator, left, right)
                return float(left) // float(right)
            case TokenType.PERCENT:
                self.check_number_operands(expr.operator, left, right)
                return float(left) % float(right)
            case TokenType.STAR:
                self.check_number_operands(expr.operator, left, right)
                return float(left) * float(right)

        return None

    def visit_grouping_expr(self, expr: Expr.Grouping):
        return self.evaluate(expr.expression)

    def visit_literal_expr(self, expr: Expr.Literal):
        return expr.value

    def visit_unary_expr(self, expr: Expr.Unary):
        right = self.evaluate(expr.right)

        match expr.operator.type:
            case TokenType.BANG:
                return not self.is_truthy(right)
            case TokenType.MINUS:
                self.check_number_operand(expr.operator, right)
                return -float(right)

        return None

    @staticmethod
    def check_number_operand(operator: Token, operand: object):
        if type(operand) is float: return
        raise RuntimeError(operator, "Operand must be a number")

    @staticmethod
    def check_number_operands(operator: Token, left: object, right: object):
        if type(left) is float and type(right) is float: return
        raise RuntimeError(operator, "Operands must be numbers")

    @staticmethod
    def is_truthy(object: object):
        if object == None: return False
        if type(object) is bool: return bool(object)
        return True

    @staticmethod
    def is_equal(a: object, b: object):
        if a == None and b == None: return True
        if a == None: return False
        return a == b

    @staticmethod
    def stringify(object: object):
        if object == None: return "nil"

        if type(object) is float:
            text = str(object)
            if text.endswith(".0"):
                text = text[0:len(text) - 2]
            return text

        return str(object)

    def evaluate(self, expr: Expr):
        return expr.accept(self)