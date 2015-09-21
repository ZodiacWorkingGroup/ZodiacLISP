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


class String(Equality):
    def __init__(self, val):
        self.val = val

    def eval(self, env):
        return Result(self.val, env)


class SExpr(Equality):
    def __init__(self, *values):
        self.values = values

    def eval(self, env):
        values = [x.eval(env) for x in self.values]

        com = values[0]
        args = values[1:]

        if com in env['builtin-functions']:
            return env['builtin-functions'][com](*args)
        elif com in env['variables']:
            funcenv = {}
            for x in range(len(env['variables'][com]['args'])):
                funcenv[env['variables'][com]['args'][x]] = args[x]

            return 
