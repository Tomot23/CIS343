 # Lab 2

 ### Expression Grammar
 ```
 expression → literal
            | unary
            | binary
            | grouping ;
literal    → NUMBER | STRING | "true" | "false" | "nil" ;
grouping   → "(" expression ")" ;
unary      → ( "-" | "!" ) expression ;
binary     → expression operator expression ;
operator   → "==" | "!=" | "<" | "<=" | ">" | ">="
            | "+" | "-" | "*" | "/" | "//" | "%" ;
 ```
 This expression grammar is identical to Lox's with the exception of the extra operators (// for floor division and % for modulo) that are added to the operator grammar. I also changed the AST printer slightly so it puts string literals in quotes to differentiate them from other literals.

 ### Setup/ Run Instructions
 There are no required dependancies to run Scyode (other than Python). Once you have downloaded the source code and are in your parent directory, you can use ```python test\lab2\[test_file]``` to test the AST Printer. The files to repoduce test results are in the test folder. You can also regenerate the expression class using ```python tool\generate_ast.py src\```.

 ### Test Cases

 1. example.py
    
    This test shows that the implemented AST works with the example AST given in the lab description. 

    AST:
    ```
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
    ```
    Expected output: ```(* (- 123) (group 45.67))```

    Actual printer output: ```(* (- 123) (group 45.67))```

    Matches Expected: ✔

2. boolean.py

    This test covers the supported boolean literals and associated operators.

    AST:
    ```
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
    ```
    Expected output: ```(== (! true) (!= false false))```

    Actual printer output: ```(== (! true) (!= false false))```

    Matches Expected: ✔

3. numbers.py

    This test covers the supported number literal and associated operators.

    AST:
    ```
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
    ```
    Expected output: ```(<= (% 10 3) (< (/ 9 7) (> (+ (* 5 3) 4) (>= (- 20 6) (// 29 2)))))```

    Actual printer output: ```(<= (% 10 3) (< (/ 9 7) (> (+ (* 5 3) 4) (>= (- 20 6) (// 29 2)))))```

    Matches Expected: ✔

4. string.py

    This test covers the supported string and nil literals.

    AST:
    ```
    expression = Expr.Binary(
        Expr.Literal("nil"),
        Token(TokenType.BANG_EQUAL, "!=", None, 1),
        Expr.Literal(None)
    )
    ```
    Expected output: ```(!= "nil" nil)```

    Actual printer output: ```(!= "nil" nil)```

    Matches Expected: ✔

### Known Limitations
There are no known limitations of the implemented AST printer, as well as no failing tests.


# Extra Credit

### Node Class Metaprogramming
A Node Class Metaprogrammer was implemented to reduce tedium in the future when more Expression subclasses must be implemented. The metaprogrammer automatically generates a structure for the defined grammar, complete with abstract vistor class methods that aid in later printer definition. 

Input: ```python tool\generate_ast.py src\```

Output:
```
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


```