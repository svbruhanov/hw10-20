import pytest

# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
@pytest.mark.parametrize("arg1,expected", [((100, 5), 20), ((10, 0.5, 4), 5), ((80, 8), 10)])
def test1(arg1, expected):
    assert all_division(*arg1) == expected


@pytest.mark.skip
def test2():
    assert all_division(100, 5) == 20
