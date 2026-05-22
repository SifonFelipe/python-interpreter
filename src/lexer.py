"""
Lexer module for tokenizing input strings.
The Lexer class reads characters from the input string and produces tokens
"""

from .tokens import (
    Token, SIGNS_TOKENS, NUMBER,
    IDENT, EOF, ILLEGAL
)

SIGNS = set(SIGNS_TOKENS.keys())

class Lexer:
    """
    A simple lexer for tokenizing input strings.
    The lexer reads characters from the input string and
    produces tokens based on the defined rules.
    """
    def __init__(self, u_input):
        self.input = u_input
        self.position = 0
        self.read_position = 0
        self.read_char()

    def read_char(self):
        """ Reads the next character from the input and advances the positions. """
        if self.read_position >= len(self.input):
            self.ch = None
        else:
            self.ch = self.input[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def read_identifier(self):
        """ Reads an identifier (a sequence of letters) from the input. """
        start_position = self.position
        while (self.ch is not None and self.ch.isalnum()) or self.ch == '_':
            self.read_char()

        return self.input[start_position:self.position]

    def read_number(self):
        """ Reads a number (a sequence of digits) from the input. """
        start_position = self.position
        while self.ch is not None and self.ch.isdigit():
            self.read_char()
        return self.input[start_position:self.position]

    def peek_char(self):
        """ Peeks at the next character without advancing the positions. """
        if self.read_position >= len(self.input):
            return None

        return self.input[self.read_position]

    def skip_whitespace(self):
        """ Skips any whitespace characters in the input. """
        while self.ch is not None and self.ch.isspace():
            self.read_char()

    def next_token(self):
        """ Returns the next token from the input. """
        self.skip_whitespace()

        if self.ch is None:
            return Token(EOF)

        if self.ch.isalpha():
            identifier = self.read_identifier()
            return Token(IDENT, identifier)

        if self.ch.isdigit():
            number = self.read_number()
            return Token(NUMBER, int(number))

        if self.ch in SIGNS:
            token = Token(SIGNS_TOKENS[self.ch], self.ch)
            self.read_char()
            return token

        # If we reach here, it is an unknown token
        token = Token(ILLEGAL, self.ch)
        self.read_char()
        return token
