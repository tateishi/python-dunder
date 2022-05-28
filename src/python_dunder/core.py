def foo():
    return "foo"


class TestNew:
    def __new__(cls, *args, **kwarg):
        instance = super().__new__(cls)
        print(f"__new__(cls) called with class {cls} and arguments {args}, {kwarg}")
        instance.a = args[0]

        return instance


class ReprTest1:
    pass


class ReprTest2:
    def __repr__(self):
        return f"repr_test2({id(self):x})"
