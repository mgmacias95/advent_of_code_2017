from Day1.day1 import day_1
from common import read_input_file_integers

def test_day1():
    assert day_1([1,1,2,2]) == 3
    assert day_1([1,1,1,1]) == 4
    assert day_1([1,2,3,4]) == 0
    assert day_1([9,1,2,1,2,1,2,9]) == 9
    assert day_1(read_input_file_integers('Day1/input')) == 1216
