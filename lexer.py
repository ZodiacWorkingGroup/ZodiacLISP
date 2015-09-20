from UtopiaLexer import *

PAREN = 'PAREN'
BRACK = 'BRACK'
CBRACK = 'CBRACK'
SEP = ','
STRING = 'STR'
NUM = 'NUM'
NAME = 'NAME'
OP = 'OP'


def lexscript(script):
    lex = lexer()

    lex.add_token_expr(r'^[\s]*', None)  # Whitespace
    lex.add_token_expr(r'^#.*', None)  # Comments
    lex.add_token_expr(r'^\(', PAREN)
    lex.add_token_expr(r'^\)', PAREN)
    lex.add_token_expr(r'^\[', BRACK)
    lex.add_token_expr(r'^\]', BRACK)
    lex.add_token_expr(r'^\{', CBRACK)
    lex.add_token_expr(r'^\}', CBRACK)
    lex.add_token_expr(r'^,', SEP)
    lex.add_token_expr(r'^(\+|-)?[0-9]+(\.[0-9]*)?', NUM)
    lex.add_token_expr(r'^".*"', STRING, (1, -1, 0))
    lex.add_token_expr(r'^[a-zA-Z_][a-zA-Z0-9_]*', NAME)
    lex.add_token_expr(r'^[^\s]', OP)

    return lex.lex(script)

if __name__ == '__main__':
    try:
        print(lexscript(input()))
    except Exception as e:
        print(e)
    input()
