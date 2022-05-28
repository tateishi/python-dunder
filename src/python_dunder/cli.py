from fire import Fire

from . import core


def hello():
    print("Hello, World.")


def new_test_main():
    a = core.TestNew(1)
    assert a.a == 1


def new_test():
    Fire(new_test_main)


def repr_test_main():
    a1 = core.ReprTest1()
    a2 = core.ReprTest2()
    print(f"a1={a1}, a2={a2}")
    print(f"a1={repr(a1)}, a2={repr(a2)}")


def repr_test():
    Fire(repr_test_main)
