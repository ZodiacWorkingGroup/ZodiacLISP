# Note: This file largely draw on Jay Conrod's Parser combinator library, but I wrote some of the code myself
# (though it will look quite similar to his).

# Please don't sue me.


class Result:
    def __init__(self, value, index):
        self.value = value
        self.index = index


class Parser:
    def __init__(self, a, b):
        self.left = a
        self.right = b

    def __add__(self, other):
        return Concat(self, other)

    def __or__(self, other):
        return Alternate(self, other)

    def __mul__(self, other):
        return Exp(self, other)

    def __and__(self, other):
        return (self+other) | (other+self)

    def __call__(self, tokens, args):
        return None


class Reserved(Parser):
    def __init__(self, name):
        self.name = name

    def __call__(self, tokens, pos):
        if pos < len(tokens) and tokens[pos].value == self.name:
            return Result(tokens[pos].value, pos + 1)
        else:
            return None

class Tag(Parser):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, tokens, pos):
        if pos < len(tokens) and tokens[pos].tag == self.tag:
            return Result(tokens[pos].value, pos + 1)
        else:
            return None

class Concat(Parser):
    def __call__(self, tokens, pos):
        left_result = self.left(tokens, pos)
        if left_result:
            right_result = self.right(tokens, left_result.pos)
            if right_result:
                combined_value = (left_result.value, right_result.value)
                return Result(combined_value, right_result.pos)
        return None


class Alternate(Parser):
    def __call__(self, tokens, pos):
        lr = self.left(tokens, pos)
        if lr:
            return lr
        else:
            rr = self.right(tokens, pos)
            if rr:
                return rr
            else:
                return None


class Exp(Parser):
    def __init__(self, parser, separator):
        self.parser = parser
        self.separator = separator

    def __call__(self, tokens, pos):
        result = self.parser(tokens, pos)

        def process_next(parsed):
            (sepfunc, right) = parsed
            return sepfunc(result.value, right)
        next_parser = self.separator + self.parser ^ process_next

        next_result = result
        while next_result:
            next_result = next_parser(tokens, result.pos)
            if next_result:
                result = next_result
        return result


class Opt(Parser):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, tokens, pos):
        result = self.parser(tokens, pos)
        if result:
            return result
        else:
            return Result(None, pos)


class Rep(Parser):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, tokens, pos):
        results = []
        result = self.parser(tokens, pos)
        while result:
            results.append(result.value)
            pos = result.pos
            result = self.parser(tokens, pos)
        return Result(results, pos)


class Lazy(Parser):
    def __init__(self, parser_func):
        self.parser = None
        self.parser_func = parser_func

    def __call__(self, tokens, pos):
        if not self.parser:
            self.parser = self.parser_func()
        return self.parser(tokens, pos)


class Phrase(Parser):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, tokens, pos):
        result = self.parser(tokens, pos)
        if result and result.pos == len(tokens):
            return result
        else:
            return None