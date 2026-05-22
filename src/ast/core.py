class NodeAST:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"NodeAST({self.value})"


class StatementAST(NodeAST):
    """
    Statements do actions.
    For example: x = 5 is a statement that assigns the value 5 to the variable x.
                 if x > 10:, for ... actions of flow control
                 imports is bringing a library
    """
    def __init__(self, value):
        super().__init__(value)


class ExpressionAST(NodeAST):
    """
    Expressions evaluate to a value.
    For example: 5 + 3 is an expression that evaluates to 8.
                 "Hello" + " World" is an expression that evaluates to "Hello World".
    """
    def __init__(self, value):
        super().__init__(value)
