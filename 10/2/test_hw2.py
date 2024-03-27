import pytest

# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test1():
    assert all_division(10, 5) == 2


@pytest.mark.smoke
def test2():
    assert all_division(100, 5) == 20


@pytest.mark.smoke
def test3():
    assert all_division(10, 0.5, 4) == 5


def test4():
    assert all_division(36, 2, 6) == 3


def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)

# 1.Все тесты
#   pytest
# 2.Только с маркером smoke
#   pytest -m smoke -v
# 3.По маске
#   pytest -k "not test3 and not test2"
