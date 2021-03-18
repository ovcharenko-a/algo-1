"""Модуль нахождения щенком пути к человеку"""

import copy


def where_from(field, x, y, memory):
    """
    Рекурсия с 
    """
    if memory[x][y] != "?":
        return memory[x][y]
    if x > 0:
        left_x = x - 1
        left_y = y
        if (left_x, left_y) == (0, 0):
            memory[x][y] = "L"
            return "L"
        if field[left_x][left_y] != "*":
            if where_from(field, left_x, left_y, memory) != "N":
                memory[x][y] = "L"
                return "L"
    if y > 0:
        up_x = x
        up_y = y - 1
        if (up_x, up_y) == (0, 0):
            memory[x][y] = "U"
            return "U"
        if field[up_x][up_y] != "*":
            if where_from(field, up_x, up_y, memory) != "N":
                memory[x][y] = "U"
                return "U"
    memory[x][y] = "N"
    return "N"


def find_path(matrix, x0, y0):
    n = len(matrix)
    path = copy.deepcopy(matrix)
    memory = [["?" for _i in range(n)] for _j in range(0, n)]
    y = x0
    x = y0
    while not (x, y) == (0, 0):
        direction = where_from(matrix, x, y, memory)
        if direction == "N":
            return "Нет такого пути :("
        elif direction == "U":
            path[x][y] = "Y"
            y -= 1
        elif direction == "L":
            path[x][y] = "Y"
            x -= 1
    path[y0][x0] = "Ч"
    print_matrix_with_symbol(path, " ")


def print_matrix_with_symbol(matrix, split_symbol):
    for line in matrix:
        print(split_symbol.join(line))


def main():
    source_string = """Щ - - * * - - - - -
- - - - * - * * - -
- - - * - * - - - *
- * - - - - - - - -
- - - - - - * - - -
- - * - - * - - - -
- - - * - - * * * -
- - - - - - - * - -
- - - - - - - * - -
- - - - - * * - - -"""
    matrix = [line.split() for line in source_string.split("\n")]
    find_path(matrix, 8, 3)


if __name__ == "__main__":
    main()
