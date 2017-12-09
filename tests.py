from Day1.day1 import day_1
from Day2.day2 import day_2
from Day3.day3 import day_3
from Day4.day4 import day_4
from Day5.day5 import day_5
from Day6.day6 import day_6
from common import read_input_file_integers, read_input_file_matrix, read_input_file_words

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

def test_day3_part2():
    assert day_3(20, '2') == 23
    assert day_3(100, '2') == 122
    assert day_3(200, '2') == 304
    assert day_3(500, '2') == 747
    assert day_3(312051, '2') == 312453

def test_day4_part1():
    assert day_4(['aa bb cc dd ee'], '1') == 1
    assert day_4(['aa bb cc dd aa'], '1') == 0
    assert day_4(['aa bb cc dd aaa'], '1') == 1
    assert day_4(read_input_file_words('Day4/input'), '1') == 466

def test_day4_part2():
    assert day_4(['abcde fghij'], '2') == 1
    assert day_4(['abcde xyz ecdab'], '2') == 0
    assert day_4(['a ab abc abd abf abj'], '2') == 1
    assert day_4(['iiii oiii ooii oooi oooo'], '2') == 1
    assert day_4(['oiii ioii iioi iiio'], '2') == 0
    assert day_4(read_input_file_words('Day4/input'), '2') == 251

def test_day5_part1():
    assert day_5([0,3,0,1,-3], '1') == 5
    assert day_5(read_input_file_matrix('Day5/input', True), '1') == 373543

def test_day5_part2():
    assert day_5([0,3,0,1,-3], '2') == 10
    assert day_5(read_input_file_matrix('Day5/input', True), '2') == 27502966

def test_day6_part1():
    assert day_6([0,2,7,0], '1') == 5
    assert day_6(read_input_file_matrix('Day6/input', True), '1') == 11137
