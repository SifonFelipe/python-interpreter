from . import ast
from .tokens import PLUS, MINUS, MULTIPLY, DIVIDE

class Evaluator:
    """
    Evaluates expressions represented as an Abstract Syntax Tree (AST).
    It supports basic arithmetic operations (for now).
    """

    def evaluate(self, node):
        if isinstance(node, ast.Number):
            return node.value

        if isinstance(node, ast.BinaryExpression):
            left_value = self.evaluate(node.left)
            right_value = self.evaluate(node.right)

            operator = node.operator.type

            if operator == PLUS:
                return left_value + right_value

            if operator == MINUS:
                return left_value - right_value

            if operator == MULTIPLY:
                return left_value * right_value

            if operator == DIVIDE:
                if right_value == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                return left_value / right_value

        raise ValueError(f"Unsupported AST node: {node}")
