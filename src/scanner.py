from error_handler import ErrorHandler
from scyode_token import Token
from token_type import TokenType

class Scanner:
    def __init__(self, source):
        self.source = source
        # TODO: initialize the scanner's state.
    
    def scan_tokens(self):
        raise NotImplementedError("Lab 1: implement Scanner.scan_tokens")