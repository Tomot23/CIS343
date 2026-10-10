from scyode_token import Token
from abc import ABC, abstractmethod


class Expr:
	class Visitor(ABC):
		@abstractmethod
		def visit_binary_expr(expr: Expr.Binary): pass
		@abstractmethod
		def visit_grouping_expr(expr: Expr.Grouping): pass
		@abstractmethod
		def visit_literal_expr(expr: Expr.Literal): pass
		@abstractmethod
		def visit_unary_expr(expr: Expr.Unary): pass

	@abstractmethod
	def accept(vistor: Visitor): pass

	class Binary:
		def __init__(self, left: Expr, operator: Token, right: Expr):
			self.left = left
			self.operator = operator
			self.right = right

		def accept(self, visitor: Expr.Visitor):
			return visitor.visit_binary_expr(self)

	class Grouping:
		def __init__(self, expression: Expr):
			self.expression = expression

		def accept(self, visitor: Expr.Visitor):
			return visitor.visit_grouping_expr(self)

	class Literal:
		def __init__(self, value: object):
			self.value = value

		def accept(self, visitor: Expr.Visitor):
			return visitor.visit_literal_expr(self)

	class Unary:
		def __init__(self, operator: Token, right: Expr):
			self.operator = operator
			self.right = right

		def accept(self, visitor: Expr.Visitor):
			return visitor.visit_unary_expr(self)

