def find_bigger(books, size_book):
    """место в массиве, где слева от него будут элементы меньше или равны, а справа строго больше."""
    left_i = 0
    right_i = len(books) - 1
    center_i = 0
    while left_i < right_i:
        center_i = (right_i + left_i) // 2
        if books[center_i] <= size_book:
            left_i = center_i + 1
        elif books[center_i] > size_book:
            right_i = center_i - 1
    # Костыль?
    if left_i == 0:
        center_i = 0
    elif right_i == len(books) - 1:
        center_i = len(books)
    return len(books) - center_i


def main():
    """Основное задание и проверка граничных значений"""
    books = [14, 16, 19, 32, 32, 32, 56, 69, 72]
    size_1 = 32
    size_2 = 60
    print(find_bigger(books, size_1))
    print(find_bigger(books, size_2))
    print(find_bigger(books, 7))
    print(find_bigger(books, 80))


if __name__ == "__main__":
    main()
