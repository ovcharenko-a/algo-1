"""Построение идеального биндерева поиска"""


def mark(arr, left, right, level, levels):
    """
    Рекурсивная функция определения уровня элемента в бинарном дереве поиска
    :param arr: входной массив
    :param left: левая граница диапазона
    :param right:правая граница диапазона
    :param level: уровень
    :param levels: массив уровней
    """
    if left == right:
        levels[left] = level
        return
    middle = (left + right) // 2
    levels[middle] = level
    mark(arr, left, middle - 1, level + 1, levels)
    mark(arr, middle + 1, right, level + 1, levels)


def build(arr):
    """
    Функция построения бинарного поиска дерева для входного массива
    :param arr: входной массив
    """
    levels = [0] * len(arr)
    mark(arr, 0, len(arr) - 1, 0, levels)
    for level in range(max(levels) + 1):
        for i in range(len(arr)):
            if levels[i] == level:
                print(arr[i], end="")
            else:
                print("  ", end="")
        print("")


if __name__ == '__main__':
    sample_arr = [10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52]

    build(sample_arr)
