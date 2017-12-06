from Day1.day1 import day_1
from Day2.day2 import day_2
from Day3.day3 import day_3
from common import read_input_file_integers, read_input_file_matrix

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

def test_day2_part1():
    assert day_2([[5,1,9,5],
                  [7,5,3],
                  [2,4,6,8]], '1') == 18
    
    assert day_2(read_input_file_matrix('Day2/input'), '1') == 34581

def test_day2_part2():
    assert day_2([[5,9,2,8],
                 [9,4,7,3],
                 [3,8,6,5]], '2') == 9

    assert day_2(read_input_file_matrix('Day2/input'), '2') == 214

def test_day3_part1():
    assert day_3(1, '1') == 0
    assert day_3(12, '1') == 3
    assert day_3(23, '1') == 2
    assert day_3(1024, '1') == 31
    assert day_3(312051, '1') == 430
