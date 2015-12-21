from parse import parser
from operator import *
from functools import reduce
from math import *


def evalall(args):
    return [evalsp(arg) for arg in args]


def evalsp(script):
    env = {}

    if type(script) == list:
        com = script[0]
        if len(script) > 1:
            args = script[1:]
        else:
            args = []

        if com == 'S':
            return evalsp(args[0])+1

        elif com == 'P':
            return evalsp(args[0])-1

        elif com == '+':
            return reduce(add, evalall(args))

        elif com == '-':
            return reduce(sub, evalall(args))

        elif com == '*':
            return reduce(mul, evalall(args))

        elif com == '/':
            return reduce(truediv, evalall(args))

        elif com == '%':
            return reduce(mod, evalall(args))

        elif com == '**':
            return reduce(pow, evalall(args))

        elif com == '~':
            return ~evalsp(args[0])

        elif com == '&':
            return reduce(and_, evalall(args))

        elif com == '|':
            return reduce(or_, evalall(args))

        elif com == '^':
            return reduce(xor, evalall(args))

        elif com == '~&':
            return ~reduce(pow, evalall(args))

        elif com == '~|':
            return ~reduce(pow, evalall(args))

        elif com == '~^':
            return ~reduce(pow, evalall(args))

        elif com == '<<':
            return reduce(lshift, evalall(args))

        elif com == '>>':
            return reduce(rshift, evalall(args))

        elif com == 'IF':
            return evalsp(args[1]) if evalsp(args[0]) else evalsp(args[2])

    else:
        return script
