from . import ast
from .tokens import (
    UnexpectedTokenError,
    PLUS, MINUS, MULTIPLY, DIVIDE, NUMBER, LPAREN, RPAREN
)

class Parser:
    """
    This parser is recursive descent, which means that each function parses
    a specific part of the grammar.

    Builds an Abstract Syntax Tree (AST) from the list of tokens provided by the lexer.
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def peek(self):
        """ Returns the current token without consuming it. """
        if self.position < len(self.tokens):
            return self.tokens[self.position]

        return None

    def consume(self):
        """ Returns the current token and advances the position. """
        token = self.peek()
        if token is not None:
            self.position += 1

        return token

    def parse_factor(self):
        """
        Parses a factor, which can be a number or an expression in parentheses.
        """
        token = self.consume()

        if token.type == NUMBER:
            return ast.Number(token.value)

        # Precedence for parentheses is handled by recursively calling parse_expression :)
        if token.type == LPAREN:
            expr = self.parse_expression()
            if self.peek() is None or self.peek().type != RPAREN:
                raise UnexpectedTokenError(self.peek())

            self.consume()  # Consumes the RPAREN
            return expr

        raise UnexpectedTokenError(token)

    def parse_term(self):
        """
        Parses a term, including two factors.
        """
        left = self.parse_factor()

        while True:
            token = self.peek()
            if token is None or token.type not in (MULTIPLY, DIVIDE):
                break

            self.consume()  # Consume the operator
            right = self.parse_factor()

            left = ast.BinaryExpression(left, token, right)

        return left

    def parse_expression(self):
        """
        Parses an expression, including two terms.
        """
        left = self.parse_term()

        while True:
            token = self.peek()
            if token is None or token.type not in (PLUS, MINUS):
                break

            self.consume()  # Consume the operator
            right = self.parse_term()

            left = ast.BinaryExpression(left, token, right)

        return left

    def parse(self):
        return self.parse_expression()

