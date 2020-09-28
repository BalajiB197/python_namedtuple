import os
import pytest
from session10 import *
from html import escape
from functools import reduce

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"