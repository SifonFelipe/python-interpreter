from . import ast
from .tokens import UnexpectedTokenError, PLUS, MINUS, MULTIPLY, DIVIDE

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def peek(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]

        return None

    def consume(self):
        token = self.peek()
        if token is not None:
            self.position += 1

        return token

    def parse_factor(self):
        token = self.consume()

        if token.type == 'NUMBER':
            return ast.Number(token.value)

        raise UnexpectedTokenError(token)

    def parse_term(self):
        left = self.parse_factor()

        while True:
            token = self.peek()
            if token is None or token.type not in (MULTIPLY, DIVIDE):
                break

            self.consume()  # Consume the operator
            right = self.parse_factor()

            left = ast.BinaryExpression(left, token.value, right)
            # token.value is the operator string ('*' or '/')
            # token.type is the token type (MULTIPLY or DIVIDE)

        return left

    def parse_expression(self):
        left = self.parse_term()

        while True:
            token = self.peek()
            if token is None or token.type not in (PLUS, MINUS):
                break

            self.consume()  # Consume the operator
            right = self.parse_term()

            left = ast.BinaryExpression(left, token.value, right)
            # token.value is the operator string ('+' or '-')
            # token.type is the token type (PLUS or MINUS)

        return left

    def parse(self):
        return self.parse_expression()
