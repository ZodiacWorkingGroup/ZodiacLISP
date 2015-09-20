class Equality:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Result(Equality):
    def __init__(self, val, env):
        self.val = val
        self.env = env


class Num(Equality):
    def __init__(self, val):
        self.val = val

    def eval(self, env):
        return Result(float(self.val), env)