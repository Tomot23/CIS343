from Expr import Expr, Token
from abc import ABC, abstractmethod


class Stmt:
	class Visitor(ABC):
		@abstractmethod
		def visit_block_stmt(stmt: Stmt.Block): pass
		@abstractmethod
		def visit_expression_stmt(stmt: Stmt.Expression): pass
		@abstractmethod
		def visit_print_stmt(stmt: Stmt.Print): pass
		@abstractmethod
		def visit_var_stmt(stmt: Stmt.Var): pass

	@abstractmethod
	def accept(vistor: Visitor): pass

	class Block:
		def __init__(self, statements: list[Stmt]):
			self.statements = statements

		def accept(self, visitor: Stmt.Visitor):
			return visitor.visit_block_stmt(self)

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

	class Var:
		def __init__(self, name: Token, initializer: Expr):
			self.name = name
			self.initializer = initializer

		def accept(self, visitor: Stmt.Visitor):
			return visitor.visit_var_stmt(self)

