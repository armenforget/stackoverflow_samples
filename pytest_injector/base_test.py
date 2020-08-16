from pytest import fixture


class BaseTest:

    @fixture(autouse=True)
    def injector(self, fixture_a, fixture_b):
        self.a = fixture_a
        self.b = fixture_b
