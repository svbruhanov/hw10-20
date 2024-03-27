import pytest


# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3


@pytest.mark.id_check(1, 2, 3)
def test():
    marks = test.pytestmark[0].args
    print(f'\n{marks}')
