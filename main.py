from src import Lexer, Parser
from src.tokens import UnexpectedTokenError
from src.evaluator import Evaluator
from src.tests import TestCase

tests = [
    TestCase("5 + 4", expected_stdout="9"),
    TestCase("(2 + 3) * (10 - 4) / 2", expected_stdout="15.0"),
    TestCase("(5 + 4) * 3", expected_stdout="27"),
    TestCase("5 * 3 * 4", expected_stdout="60"),
    TestCase("x = 5 + 10"),
    TestCase("my_var = 20 - 4"),
    TestCase("hello123")
]

def main():
    for t in tests:
        print(f"Testing input: {t.sentence}")

        lexer = Lexer(t.sentence)
        tokens = []
        expressions = []

        while True:
            token = lexer.next_token()
            tokens.append(token)
            if token.type == 'EOF':
                break

        print("\nTokens:\n")
        for token in tokens:
            print(token)

        print("\nParsed AST:\n")
        parser = Parser(tokens)
        try:
            while True:
                expression = parser.parse()
                expressions.append(expression)
                if expression is None:
                    break

        except UnexpectedTokenError as e:
            print(e)

        print(expression)

        evaluator = Evaluator()
        result = evaluator.evaluate(expression)  # Result (singular) by now
        print("\nEvaluation results:\n")
        print(result)

        input("\nPress Enter to continue to the next test...\n")

if __name__ == "__main__":
    main()
