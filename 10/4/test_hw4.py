# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.


def plus(a, b):
    return a + b


class Test:

    def test1(self, test_time):
        assert plus(10, 5) == 15

    def test2(self, test_time_diff):
        assert plus(4, 5) == 9

    def test3(self, test_time_diff):
        assert plus(11, 2) == 13

    def test4(self):
        assert plus(624, 2) == 626
