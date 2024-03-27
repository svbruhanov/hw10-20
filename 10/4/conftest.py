import time
from datetime import datetime
import pytest


@pytest.fixture(scope='class', autouse=True)
def test_time():
    start = datetime.now().microsecond
    yield
    end = datetime.now().microsecond
    print(f"\n START = {start} sec, END = {end} sec.")


@pytest.fixture(scope='function', autouse=True)
def test_time_diff():
    start = time.time()
    yield
    end = time.time()
    print(f"\n TIME  = {round(end - start, 4)} sec.")