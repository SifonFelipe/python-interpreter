class TestCase:
    def __init__(self, sentence, expected_stdout=""):
        self.sentence = sentence
        self.expected_tokens = expected_stdout

    def evaluate(self, result):
        assert result == self.expected_tokens, f"Expected: {self.expected_tokens}, Got: {result}"

