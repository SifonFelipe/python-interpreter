from .core import ExpressionAST

class Number(ExpressionAST):
    def __init__(self, value):
        super().__init__(value)

    def __repr__(self):
        return f"Number({self.value})"


class BinaryExpression(ExpressionAST):
    def __init__(self, left, operator, right):
        super().__init__(None)  # No direct value for BinaryExpression
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinaryExpression({self.left}, {self.operator}, {self.right})"
