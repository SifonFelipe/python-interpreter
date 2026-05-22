from src import Lexer, Parser
from src.tokens import UnexpectedTokenError
from src.tests import TestCase

tests = [
    TestCase("5 + 4"),
    TestCase("5 + 4 * 3"),
    TestCase("5 * 4 + 3"),
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
                print(expression)
                expressions.append(expression)
                if expression is None:
                    break

        except UnexpectedTokenError as e:
            print(e)

        input("\nPress Enter to continue to the next test...\n")

if __name__ == "__main__":
    main()
