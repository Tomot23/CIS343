from scyode_token import Token
from runtime_error import RuntimeError


class Environment:

    def __init__(self, enclosing: Environment = None):
        self.values = {}
        self.enclosing = enclosing

    def get(self, name: Token):
        if name.lexeme in self.values.keys():
            return self.values[name.lexeme]

        if self.enclosing is not None: return self.enclosing.get(name)
        
        raise RuntimeError(name, f"Undefined variable '{name.lexeme}'")

    def assign(self, name: Token, value: object):
        if name.lexeme in self.values.keys():
            self.values[name.lexeme] = value
            return

        if self.enclosing is not None:
            self.enclosing.assign(name, value)
            return
        
        raise RuntimeError(name, f"Undefined variable '{name.lexeme}'")

    def define(self, name: str, value: object):
        self.values[name] = value