from Expr import Expr
from abc import ABC, abstractmethod


class Stmt:
	class Visitor(ABC):
		@abstractmethod
		def visit_expression_stmt(stmt: Stmt.Expression): pass
		@abstractmethod
		def visit_print_stmt(stmt: Stmt.Print): pass

	@abstractmethod
	def accept(vistor: Visitor): pass

	class Expression:
		def __init__(self, expression: Expr):
			self.expression = expression

		def accept(self, visitor: Stmt.Visitor):
			return visitor.visit_expression_stmt(self)

	class Print:
		def __init__(self, expression: Expr):
			self.expression = expression

		def accept(self, visitor: Stmt.Visitor):
			return visitor.visit_print_stmt(self)

