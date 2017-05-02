from algorithms.implementation.matrix_layer_rotation.matrix_layer_rotation import SnakePit


snake_pit_00 = SnakePit(4, 4, [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

snake_pit_01 = SnakePit(6, 4, [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 17],
    [17, 18, 19, 20],
    [21, 22, 23, 24]
])

snake_pit_02 = SnakePit(5, 4, [
    [1, 2, 3, 4],
    [7, 8, 9, 10],
    [13, 14, 15, 16],
    [19, 20, 21, 22],
    [25, 26, 27, 28]
])

snake_pit_03 = SnakePit(2, 2, [
    [1, 1],
    [1, 1]
])

snake_pit_04 = SnakePit(3, 2, [
    [1, 2],
    [5, 6],
    [9, 10]
])

snake_pit_05 = SnakePit(6, 7, [
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40, 41, 42]
])


def test_number_of_snakes():
    assert snake_pit_00.number_of_snakes == 2
    assert snake_pit_01.number_of_snakes == 2
    assert snake_pit_02.number_of_snakes == 2
    assert snake_pit_03.number_of_snakes == 1
    assert snake_pit_04.number_of_snakes == 1
    assert snake_pit_05.number_of_snakes == 3


def test_snake_width():
    assert snake_pit_00.get_snake_width(0) == 4
    assert snake_pit_00.get_snake_width(1) == 2
    assert snake_pit_01.get_snake_width(0) == 4
    assert snake_pit_01.get_snake_width(1) == 2
    assert snake_pit_02.get_snake_width(0) == 4
    assert snake_pit_02.get_snake_width(1) == 2
    assert snake_pit_03.get_snake_width(0) == 2
    assert snake_pit_04.get_snake_width(0) == 2
    assert snake_pit_05.get_snake_width(0) == 7
    assert snake_pit_05.get_snake_width(1) == 5
    assert snake_pit_05.get_snake_width(2) == 3


def test_snake_height():
    assert snake_pit_00.get_snake_height(0) == 4
    assert snake_pit_00.get_snake_height(1) == 2
    assert snake_pit_01.get_snake_height(0) == 6
    assert snake_pit_01.get_snake_height(1) == 4
    assert snake_pit_02.get_snake_height(0) == 5
    assert snake_pit_02.get_snake_height(1) == 3
    assert snake_pit_03.get_snake_height(0) == 2
    assert snake_pit_04.get_snake_height(0) == 3
    assert snake_pit_05.get_snake_height(0) == 6
    assert snake_pit_05.get_snake_height(1) == 4
    assert snake_pit_05.get_snake_height(2) == 2


def test_snake_length():
    assert snake_pit_00.get_snake_length(0) == 12
    assert snake_pit_00.get_snake_length(1) == 4
    assert snake_pit_01.get_snake_length(0) == 16
    assert snake_pit_01.get_snake_length(1) == 8
    assert snake_pit_02.get_snake_length(0) == 14
    assert snake_pit_02.get_snake_length(1) == 6
    assert snake_pit_03.get_snake_length(0) == 4
    assert snake_pit_04.get_snake_length(0) == 6
    assert snake_pit_05.get_snake_length(0) == 22
    assert snake_pit_05.get_snake_length(1) == 14
    assert snake_pit_05.get_snake_length(2) == 6
