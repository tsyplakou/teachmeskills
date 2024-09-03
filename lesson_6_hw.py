# 1
def recursive_binary_search(nums, target, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1

    # Базовый случай: если границы пересеклись, элемент не найден
    if left > right:
        return -1

    # Находим середину текущего диапазона
    mid = (left + right) // 2

    # Если элемент найден в середине, возвращаем его индекс
    if nums[mid] == target:
        return mid
    # Если элемент меньше среднего, ищем в левой половине
    elif nums[mid] > target:
        return recursive_binary_search(nums, target, left, mid - 1)
    # Если элемент больше среднего, ищем в правой половине
    else:
        return recursive_binary_search(nums, target, mid + 1, right)


# 2
def decimal_to_binary_iterative(num):
    if num == 0:
        return "0"
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary  # Добавляем остаток в начало строки
        num //= 2
    return binary


# 3
def is_prime(num):
    if num <= 1:
        return False  # Числа 0, 1 и отрицательные числа не являются простыми
    if num == 2:
        return True  # 2 - простое число

    # Проверяем делимость на числа от 2 до квадратного корня из num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 4
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 5
def caesar_cipher_encrypt(text, shift):
    result = ""

    for char in text:
        # Шифрование заглавных символов
        # Деление с остатком учитывает переход за край алфавита
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Шифрование строчных символов
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Если символ не является буквой, просто добавляем его в результат
            result += char

    return result


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# 7
import random

def create_matrix(M, N, min_value=0, max_value=100):
    """Создает матрицу MxN, заполненную случайными числами в диапазоне [min_value, max_value]."""
    matrix = []
    for row_index in range(M):
        matrix.append([])
        # Создаем строку из N случайных чисел и добавляем её в матрицу
        for _ in range(N):
            matrix[row_index].append(random.randint(min_value, max_value))
    return matrix


[
    [1, 2, 3],
    [1, 2, 3],
]


# 8
def find_min_max(matrix):
    _min = _max = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < _min:
                _min = elem
            if elem > _max:
                _max = elem
    return _min, _max


# 9
def sum_and_percentage(matrix):
    _sum = 0
    columns_percentage = []

    for col_index in range(len(matrix[0])):
        column_sum = 0
        for row in matrix:
            column_sum += row[col_index]
        _sum += column_sum
        columns_percentage.append(column_sum)

    for i, percentage in enumerate(columns_percentage):
        columns_percentage[i] = f'{(percentage / _sum) * 100:.2f}%'

    return _sum, columns_percentage


# 12
def check_in_columns(matrix, target):
    for col_index in range(len(matrix[0])):
        for row in matrix:
            if target == row[col_index]:
                print(f'Target {target} found in column {col_index + 1}')
                break
        else:
            print(f'Target {target} not found in column {col_index + 1}')

# 13
def diagonal_sums(matrix):
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    for i in range(min(rows, cols)):
        main_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][cols - 1 - i]

    return main_diagonal_sum, secondary_diagonal_sum

# 14
def make_even(matrix):
    for row in matrix:
        row.append(sum(row) % 2)
    return matrix
