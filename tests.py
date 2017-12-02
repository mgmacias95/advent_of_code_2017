from Day1.day1 import day_1
from common import read_input_file_integers

def test_day1_part1():
    assert day_1([1,1,2,2], '1') == 3
    assert day_1([1,1,1,1], '1') == 4
    assert day_1([1,2,3,4], '1') == 0
    assert day_1([9,1,2,1,2,1,2,9], '1') == 9
    assert day_1(read_input_file_integers('Day1/input'), '1') == 1216

def test_day1_part2():
    assert day_1([1,2,1,2], '2') == 6
    assert day_1([1,2,2,1], '2') == 0
    assert day_1([1,2,3,4,2,5], '2') == 4
    assert day_1([1,2,3,1,2,3], '2') == 12
    assert day_1([1,2,1,3,1,4,1,5], '2') == 4
    assert day_1(read_input_file_integers('Day1/input'), '2') == 1072
