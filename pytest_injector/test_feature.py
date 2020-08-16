from python.pytest_injector.base_test import BaseTest


class TestFeature(BaseTest):

    def test_something(self):
        assert self.a.data == [1, 2, 3]
        assert self.b.data == [3, 2, 1]
