from token_type import TokenType


class Token:
    def __init__(self, type: TokenType, lexeme, literal, line):
        # TODO: store type, lexeme, literal, and line as public attributes.
        raise NotImplementedError("Lab 1: implement Token.__init__")

    def __str__(self):
        # TODO: return a string containing the type, lexeme, and literal.
        raise NotImplementedError("Lab 1: implement Token.__str__")