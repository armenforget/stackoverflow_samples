from pytest import fixture


class FixtureA:
    def __init__(self):
        self.data = [1, 2, 3]


@fixture(scope="function")
def fixture_a():
    return FixtureA()


class FixtureB:
    def __init__(self):
        self.data = [3, 2, 1]


@fixture(scope="function")
def fixture_b():
    return FixtureB()
