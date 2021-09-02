import os,sys
sys.path.append(os.getcwd())
from nth_happy_number import nth_happy_number
import pytest


@pytest.mark.parametrize('a, result',[
    (1,1),(2,7),(3,10),(4,13),(5,19),(6,23),(7,28),(8,31)
])
def test_nth_happy_number(a, result):
    assert nth_happy_number(a) == result

