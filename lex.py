import ply.lex as lex

tokens = [
    'FUNC',
    'INT',
    'FLOAT',
    'STR',
    'OPAREN',
    'CPAREN',
    'BOOL'
]


def t_INT(t):
    """
    0b[01]+|
    0q[0-3]+|
    0o[0-7]+|
    0x[0-9a-f]+|
    0x[0-9A-F]+|
    [0-9]+
    """
    if t.value[:2] == '0b':
        t.value = int(t.value[2:], 2)

    elif t.value[:2] == '0q':
        t.value = int(t.value[2:], 4)

    elif t.value[:2] == '0o':
        t.value = int(t.value[2:], 8)

    elif t.value[:2] == '0x':
        t.value = int(t.value[2:], 16)

    else:
        t.value = int(t.value)

    return t


def t_FLOAT(t):
    """[0-9]+(\.[0-9]+)?"""
    t.value = float(t.value)
    return t


def t_STR(t):
    '''"[^"\\\\]*(?:\\\\.[^"\\\\]*)*"'''
    return t[1:-1]


def t_BOOL(t):
    """[tT](rue|RUE)?|[fF](alse|ALSE)?"""
    return t[0].upper() == 'T'

t_FUNC = r'[^()0-9\s"]+'
t_OPAREN = r'\('
t_CPAREN = r'\)'

t_ignore = ' \t\n'


def t_error(t):
    raise SyntaxError('Invalid character: '+t.value)

lexer = lex.lex()

if __name__ == '__main__':
    lexer.input(input())
    for x in lexer:
        print(x)