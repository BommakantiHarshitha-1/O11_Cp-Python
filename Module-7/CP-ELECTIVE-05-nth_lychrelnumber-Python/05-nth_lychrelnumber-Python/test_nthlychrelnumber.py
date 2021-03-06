import os,sys
sys.path.append(os.getcwd())
from nthlychrelnumber import nthlychrelnumbers
import pytest


@pytest.mark.parametrize('x, result',[
(1, 196), 
(2, 295), 
(3, 394), 
(4, 493), 
(5, 592), 
(6, 689), 
(7, 691), 
(8, 788), 
(9, 790), 
(10, 879), 
(11, 887), 
(12, 978), 
(13, 986), 
(14, 1495), 
(15, 1497), 
(16, 1585), 
(17, 1587), 
(18, 1675), 
(19, 1677), 
(20, 1765), 
(21, 1767), 
(22, 1855), 
(23, 1857), 
(24, 1945), 
(25, 1947), 
(26, 1997), 
(27, 2494), 
(28, 2496), 
(29, 2584), 
(30, 2586), 
(31, 2674), 
(32, 2676), 
(33, 2764), 
(34, 2766), 
(35, 2854), 
(36, 2856), 
(37, 2944), 
(38, 2946), 
(39, 2996), 
(40, 3493), 
(41, 3495), 
(42, 3583), 
(43, 3585), 
(44, 3673), 
(45, 3675), 
])

def test_nthlychrelnumbers(x, result):
    assert nthlychrelnumbers(x) == result
