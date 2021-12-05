from collections import Counter

from main import count
from main import keep
from main import transpose


INPUT_S = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def test_length_transpose():
    transposed = transpose(INPUT_S)
    assert len(transposed) == 5


def test_transposed():
    expected = [
        ("0", "1", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0"),
        ("0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "1"),
        ("1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0"),
        ("0", "1", "1", "1", "0", "1", "1", "0", "0", "0", "1", "1"),
        ("0", "0", "0", "1", "1", "1", "1", "0", "0", "1", "0", "0"),
    ]
    actual = transpose(INPUT_S)
    assert expected == actual


def test_count():
    expected = {
        0: Counter({"1": 7, "0": 5}),
        1: Counter({"0": 7, "1": 5}),
        2: Counter({"1": 8, "0": 4}),
        3: Counter({"1": 7, "0": 5}),
        4: Counter({"0": 7, "1": 5}),
    }
    actual = count(transpose(INPUT_S))
    assert expected == actual


def test_keep_most_common():
    expected = {0: "1", 1: "0", 2: "1", 3: "1", 4: "0"}
    counter = count(transpose(INPUT_S))
    actual = keep(counter=counter, condition="most_common")
    assert expected == actual


def test_keep_least_common():
    expected = {0: "0", 1: "1", 2: "0", 3: "0", 4: "1"}
    counter = count(transpose(INPUT_S))
    actual = keep(counter=counter, condition="least_common")
    assert expected == actual


def test_keep_most_common_with_even():
    expected = {0: "1", 1: "0", 2: "1", 3: "1", 4: "0", 5: "1"}
    transposed = [
        "011110011100",
        "010001010101",
        "111111110000",
        "011101100011",
        "000111100100",
        "100111100100",
    ]
    counter = count(transposed)
    actual = keep(counter=counter, condition="most_common")
    assert expected == actual


def test_keep_least_common_with_even():
    expected = {0: "0", 1: "1", 2: "0", 3: "0", 4: "1", 5: "0"}
    transposed = [
        "011110011100",
        "010001010101",
        "111111110000",
        "011101100011",
        "000111100100",
        "100111100100",
    ]
    counter = count(transposed)
    actual = keep(counter=counter, condition="least_common")
    assert expected == actual
