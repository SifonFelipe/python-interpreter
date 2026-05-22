"""
This module defines the Token class, which represents a token in the lexer.
Each token has a type and an optional value (sign cases).
"""

NUMBER = 'NUMBER'
IDENT = 'IDENT'

PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
EQUALS = 'EQUALS'

SIGNS_TOKENS = {
    '+': PLUS,
    '-': MINUS,
    '*': MULTIPLY,
    '/': DIVIDE,
    '(': LPAREN,
    ')': RPAREN,
    '=': EQUALS
}

EOF = 'EOF'
ILLEGAL = 'ILLEGAL'

class UnexpectedTokenError(Exception):
    """ Custom exception for unexpected tokens. """
    def __init__(self, token):
        self.token = token
        super().__init__(f'Unexpected token: {token}')


class Token:
    """
    A class representing a token in the lexer.
    Each token has a type and an optional value.
    """
    def __init__(self, t_type, value=None):
        self.type = t_type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {repr(self.value)})'
