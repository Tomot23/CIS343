from scyode_token import Token

class RuntimeError(RuntimeError):

    def __init__(self, token: Token, message: str):
        super().__init__(message)
        self.token = token