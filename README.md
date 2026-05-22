# Python Interpreter

## Objective
The objective of this project is to implement a simple Python interpreter that can execute basic Python code.


For example, I want to build something that reads:
```python
x = 10 + 5
```
and the computer understands.


The interpreter has to transform the sentences in structures that the computer can understand and execute.
This process involves several stages, including tokenization, parsing, and execution.

## Stages of Interpretation

### Visual
<img width="333" height="1072" alt="interpreter" src="https://github.com/user-attachments/assets/35f3ab85-75ea-4cd8-8c21-06125cc80997" />

### Lexer (Tokenization)
The first stage of the interpretation process is tokenization, which is performed by a component called the
lexer. The lexer takes the raw source code as input and breaks it down into a sequence of tokens.
Each token represents a meaningful unit in the source code, such as keywords, identifiers, literals, operators, and punctuation.


For example:
```python
x = 10 + 5
```

In this line of code, the lexer would produce the following tokens:
```
- x   IDENTIFIER
- =   EQUALS
- 10  NUMBER
- +   PLUS
- 5   NUMBER
NUMBER
```

Only classifies symbols, it does not understand the meaning.


### Parser (Syntax Analysis)
The parser takes the sequence of tokens and understands the structure of the code.
Here appears the idea of: `(10 + 5)` as a mathematical expression.

The parser builds an Abstract Syntax Tree (AST) that represents the hierarchical structure of the code.

```
Assign
├── Variable: x
└── value:
     Add
      ├── Number: 10
      └── Number: 5
```

Now there is a "significance".


### Semantic Analysis
Here you check the language rules.


For example:
```python
x = y + 1
```

* Does `y` exist?
* Can they be summed?
* Did `y` get assigned a value before?

This is language logic.


### Interpreter / Code Generation

2 ways to execute the code:
1. **Interpreter**: Directly executes the AST by traversing it and performing the corresponding
2. **Compile**: Transforms the AST into machine code or bytecode that can be executed by the computer.

