from main import Coordinate, Line


def test_still():
    input_s = "1,1 -> 1,1"
    expected_start = Coordinate(x=1, y=1)
    exepected_end = Coordinate(x=1, y=1)
    result = Line.from_string(input_s=input_s)
    assert result.start == expected_start
    assert result.end == exepected_end


def test_vertical_forward():
    input_s = "1,1 -> 1,3"
    expected_start = Coordinate(x=1, y=1)
    exepected_end = Coordinate(x=1, y=3)
    result = Line.from_string(input_s=input_s)
    assert result.start == expected_start
    assert result.end == exepected_end


def test_vertical_reverse():
    input_s = "1,3 -> 1,1"
    expected_start = Coordinate(x=1, y=1)
    exepected_end = Coordinate(x=1, y=3)
    result = Line.from_string(input_s=input_s)
    assert result.start == expected_start
    assert result.end == exepected_end


def test_horizontal_forward():
    input_s = "9,7 -> 7,7"
    expected_start = Coordinate(x=7, y=7)
    exepected_end = Coordinate(x=9, y=7)
    result = Line.from_string(input_s=input_s)
    assert result.start == expected_start
    assert result.end == exepected_end


def test_horizontal_points():
    input_s = "9,7 -> 7,7"
    expected_points = [
        Coordinate(7, 7),
        Coordinate(8, 7),
        Coordinate(9, 7),
    ]
    line = Line.from_string(input_s)
    assert expected_points == line.points


def test_vertical_points():
    input_s = "1,3 -> 1,1"
    expected_points = [
        Coordinate(1, 1),
        Coordinate(1, 2),
        Coordinate(1, 3),
    ]
    line = Line.from_string(input_s)
    assert expected_points == line.points


def test_diagional_ordering_both_increase():
    input_s = "1,1 -> 3,3"
    expected_start = Coordinate(x=1, y=1)
    exepected_end = Coordinate(x=3, y=3)
    result = Line.from_string(input_s=input_s)
    assert result.start == expected_start
    assert result.end == exepected_end


def test_diagional_ordering_both_reverse():
    input_s = "3,3 -> 1,1"
    expected_start = Coordinate(x=1, y=1)
    exepected_end = Coordinate(x=3, y=3)
    result = Line.from_string(input_s=input_s)
    assert result.start == expected_start
    assert result.end == exepected_end


def test_diagional_ordering_y_decreases():
    input_s = "9,7 -> 7,9"
    expected_start = Coordinate(x=7, y=9)
    exepected_end = Coordinate(x=9, y=7)
    result = Line.from_string(input_s=input_s)
    assert result.start == expected_start
    assert result.end == exepected_end


def test_diagional_ordering_y_decreases_reverse():
    input_s = "7,9 -> 9,7"
    expected_start = Coordinate(x=7, y=9)
    exepected_end = Coordinate(x=9, y=7)
    result = Line.from_string(input_s=input_s)
    assert result.start == expected_start
    assert result.end == exepected_end


def test_diagional_points_x_and_y_increase():
    input_s = "1,1 -> 3,3"
    expected_points = [
        Coordinate(1, 1),
        Coordinate(2, 2),
        Coordinate(3, 3),
    ]
    line = Line.from_string(input_s)
    assert expected_points == line.points


def test_diagional_points_x_and_y_increase_reversed():
    input_s = "3,3 -> 1,1"
    expected_points = [
        Coordinate(1, 1),
        Coordinate(2, 2),
        Coordinate(3, 3),
    ]
    line = Line.from_string(input_s)
    assert expected_points == line.points


def test_diagional_points_x_incr_and_y_decrease():
    input_s = "7,9 -> 9,7"
    expected_points = [
        Coordinate(7, 9),
        Coordinate(8, 8),
        Coordinate(9, 7),
    ]
    line = Line.from_string(input_s)
    assert expected_points == line.points


def test_diagional_points_x_incr_and_y_decrease_reversed():
    input_s = "9,7 -> 7,9"
    expected_points = [
        Coordinate(7, 9),
        Coordinate(8, 8),
        Coordinate(9, 7),
    ]
    line = Line.from_string(input_s)
    assert expected_points == line.points


def test_diagional_0_8_8_0():
    input_s = "8,0 -> 0,8"

    expected_points = [
        Coordinate(0, 8),
        Coordinate(1, 7),
        Coordinate(2, 6),
        Coordinate(3, 5),
        Coordinate(4, 4),
        Coordinate(5, 3),
        Coordinate(6, 2),
        Coordinate(7, 1),
        Coordinate(8, 0),
    ]
    line = Line.from_string(input_s)
    assert expected_points == line.points


def test_diagional_8_0_0_8():
    input_s = "0,8 -> 8,0"

    expected_points = [
        Coordinate(0, 8),
        Coordinate(1, 7),
        Coordinate(2, 6),
        Coordinate(3, 5),
        Coordinate(4, 4),
        Coordinate(5, 3),
        Coordinate(6, 2),
        Coordinate(7, 1),
        Coordinate(8, 0),
    ]
    line = Line.from_string(input_s)
    assert expected_points == line.points


def test_diagional_55_82():
    input_s = "5,5 -> 8,2"

    expected_points = [
        Coordinate(5, 5),
        Coordinate(6, 4),
        Coordinate(7, 3),
        Coordinate(8, 2),
    ]
    line = Line.from_string(input_s)
    assert expected_points == line.points


def test_horizontal_34_14():
    input_s = "3,4 -> 1,4"

    expected_points = [
        Coordinate(1, 4),
        Coordinate(2, 4),
        Coordinate(3, 4),
    ]
    line = Line.from_string(input_s)
    assert expected_points == line.points


def test_diagional_64_20():
    input_s = "6,4 -> 2,0"

    expected_points = [
        Coordinate(2, 0),
        Coordinate(3, 1),
        Coordinate(4, 2),
        Coordinate(5, 3),
        Coordinate(6, 4),
    ]
    line = Line.from_string(input_s)
    assert expected_points == line.points
