import os
import pytest
from session10 import *
from html import escape
from functools import reduce

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_dict_approach():
    *_, = dict_approach()
    assert len(_) > 1, "Returns all the calculation"

def test_named_tuple():
    *_, = named_tuple()
    assert len(_) > 1, "Returns all the calculation"

def test_named_tuple_vs_dict():
    cnt = 0
    for _ in range(10):
        start1 = perf_counter()
        *_, = dict_approach()
        end1 = perf_counter()
        elapsed1 = end1 - start1

        start2 = perf_counter()
        *_, = named_tuple()
        end2 = perf_counter()
        elapsed2 = end2 - start2

        if elapsed2 < elapsed1:
            cnt+=1
    assert cnt >= 4, "checking more than random times the namedtuple is performing better"

def test_stock():
    open1, high, close = stock_price()
    assert open1 < high and high > close, "checking the maximum stock reached"

    