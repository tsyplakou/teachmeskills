#1
my_list = [a for a in range(1, 1000)]


def rec_search(my_num, my_list, low=0, high=len(my_list) - 1):
    if low > high:
        return None
    mid = (low + high) // 2

    if my_num == my_list[mid]:
        index = mid

    elif my_num < my_list[mid]:
        index = rec_search(my_num, my_list, low, mid - 1)

    else:
        index = rec_search(my_num, my_list, mid + 1, high)
    return index


print(rec_search(79, my_list))
print(rec_search(1001, my_list))

#2
def binary_num (num_in_dec):

    if num_in_dec == 0:
        return 0

    res_division = []
    while num_in_dec >= 1:
        res_division.append(num_in_dec % 2)
        num_in_dec //= 2
    """ 
    число в двоичной системе будет выглядеть как строка, 
    образованная из элементов списка res_division в обратном порядке
    """
    num_in_binary = ''.join(map(str, reversed(res_division)))
    return num_in_binary


print(binary_num(79))

#3
def is_num_prime(num):
    if num <= 1:
        print("Числа 0 и 1 не являются простыми")
        return False
    multipliers = []
    for n in range(2, num + 1):
        if num % n == 0:
            multipliers.append(n)
    if len(multipliers) > 2:
        print(f"Число {num} не является простым")
        return False
    else:
        print(f"Число {num}является простым")
        return True

print(is_num_prime(10))

#4
"""
Алгоритм Евклида: если большее из двух чисел делится на меньшее — наименьшее
число и будет их наибольшим общим делителем. Использовать метод Евклида
можно легко по формуле нахождения наибольшего общего делителя.
Формула НОД: НОД (a, b) = НОД (b, с), где с — остаток от деления a на b
"""


def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(nod(1448, 688))

#5
my_str = input("Введите строку для шифрования/дешифрования: ")
step = int(input("Введите размер шага для шифрования/дешифрования: "))

def encrypt (my_str, step):
    encrypt_str = ""

    for symbol in my_str:
        if symbol.isupper():
            encrypt_str += chr((ord(symbol) + step - 1040) % 32 + 1040)
        elif symbol.islower():
            encrypt_str += chr((ord(symbol) + step - 1072) % 32 + 1072)
        else:
            encrypt_str += symbol

    return encrypt_str


def decrypt(my_str, step):
    decrypt_str = encrypt(my_str, -step)

    return decrypt_str


encrypt_decrypt = input("Введите 'шифр' если строку нужно зашифровать, "
                        "или 'дешифр' если нужно дешифровать: "
                        )
if encrypt_decrypt == "шифр":
    print(encrypt(my_str, step))
elif encrypt_decrypt == "дешифр":
    print(decrypt(my_str, step))
else:
    print("Вы указали неверное действие")

#6
my_str = input("Введите строку для шифрования/дешифрования: ")
key_word = input("Введите ключевое слово для шифрования/дешифрования: ")


def encrypt_vigener(my_str, key_word):
    encrypt_str = ""
    key_codes = [ord(key) - 1040 if key.isupper() else ord(key) - 1072
                 for key in key_word
                 ]
    key_code_index = 0
    for symbol in my_str:
        if symbol.isupper():
            encrypt_str += chr(((ord(symbol) - 1040) +
                               key_codes[key_code_index % len(key_word)]) %
                               32 + 1040)
            key_code_index += 1
        elif symbol.islower():
            encrypt_str += chr(((ord(symbol) - 1072) +
                               key_codes[key_code_index % len(key_word)]) %
                               32 + 1072)
            key_code_index += 1
        else:
            encrypt_str += symbol

    return encrypt_str


def decrypt_vigener(my_str, key_word):
    decrypt_str = ""
    key_codes = [ord(key) - 1040 if key.isupper() else ord(key) - 1072
                 for key in key_word
                 ]
    key_code_index = 0
    for symbol in my_str:
        if symbol.isupper():
            decrypt_str += chr(((ord(symbol) - 1040) -
                               key_codes[key_code_index % len(key_word)]) %
                               32 + 1040)
            key_code_index += 1
        elif symbol.islower():
            decrypt_str += chr(((ord(symbol) - 1072) -
                               key_codes[key_code_index % len(key_word)]) %
                               32 + 1072)
            key_code_index += 1
        else:
            decrypt_str += symbol

    return decrypt_str


encrypt_decrypt = input("Введите 'шифр' если строку нужно зашифровать, "
                        "или 'дешифр' если нужно дешифровать: "
                        )
if encrypt_decrypt == "шифр":
    print(encrypt_vigener(my_str, key_word))
elif encrypt_decrypt == "дешифр":
    print(decrypt_vigener(my_str, key_word))
else:
    print("Вы указали неверное действие")


#7
from random import randint


def create_random_array(m, n):
    array = []
    for i in range(m):
        new_row = []
        for j in range(n):
            new_row.append(randint(-100, 100))
        array.append(new_row)
    return array


random_matrix = create_random_array(3, 3)
for row in random_matrix:
    print(row)


# то же самое с использованием генератора списков

def create_random_array(m, n):
    array = [[randint(-100, 100) for row in range(n)] for i in range(m)]
    return array


random_matrix = create_random_array(3, 3)
for row in random_matrix:
    print(row)


#8
from random import randint


def create_random_array(m, n):
    array = [[randint(-100, 100) for row in range(n)] for i in range(m)]
    return array

random_matrix = create_random_array(3, 3)
print("Сгенерированная матрица:")
for row in random_matrix:
    print(row)

def min_max_index(random_matrix):
    min_value = random_matrix[0][0]
    max_value = random_matrix[0][0]
    min_index = (0, 0)
    max_index = (0, 0)

    for row in range(len(random_matrix)):
        for column in range(len(random_matrix[row])):
            value = random_matrix[row][column]

            if value < min_value:
                min_value = value
                min_index = [row, column]

            if value > max_value:
                max_value = value
                max_index = [row, column]

    print(f"Минимальное значение: {min_value}, Индекс значения: {min_index}")
    print(f"Максимальное значение: {max_value}, Индекс значения: {max_index}")

    return min_index, max_index

min_max_index(random_matrix)


#9
from random import randint

def create_random_array(m, n):
    array = [[randint(-100, 100) for row in range(n)] for i in range(m)]
    return array

random_matrix = create_random_array(3, 3)
print("Сгенерированная матрица:")
for row in random_matrix:
    print(row)


def sum_of_elem(random_matrix):
    sum_all_elem = 0
    all_columns_sum = []
    for column in range(len(random_matrix[0])):
        column_sum = 0
        for row in random_matrix:
            column_sum += row[column]
        all_columns_sum.append(column_sum)
        sum_all_elem += column_sum
    print(f"Сумма элементов матрицы составляет: {sum_all_elem}")
    for ind, column_sum in enumerate(all_columns_sum):
        share = column_sum / sum_all_elem * 100 if sum_all_elem != 0 else 0
        print(f"Индекс столбца: {ind}, сумма его элементов: {column_sum}, "
          f"процент от суммы элементов матрицы: {share:.2f}%")
    return sum_all_elem, share
sum_of_elem(random_matrix)


#10
from random import randint

def create_random_array(m, n):
    array = [[randint(-100, 100) for row in range(n)] for i in range(m)]
    return array

random_matrix = create_random_array(3, 3)
print("Сгенерированная матрица:")
for row in random_matrix:
    print(row)

k = int(input("Введите индекс столбца, на элементы которого следует "
                  "умножить элемент каждого столбца матрицы: "))

def multiply_column(random_matrix, k):
    result = []

    for column in range(len(random_matrix[0])):
        column_result = []
        for row in range(len(random_matrix)):
            column_result.append(random_matrix[row][column] *
                                 random_matrix[row][k]
                                 )
        result.append(column_result)
    print(f"В результате умножения элементов столбцов матрицы на элементы "
          f"столбца с индексом {k} получаем матрицу: ")
    for row in result:
        print(row)
    return result


multiply_column(random_matrix, k)


#11
from random import randint

def create_random_array(m, n):
    array = [[randint(-100, 100) for row in range(n)] for i in range(m)]
    return array

random_matrix = create_random_array(3, 3)
print("Сгенерированная матрица:")
for row in random_matrix:
    print(row)

l = int(input("Введите индекс строки, с элементами которой следует "
              "сложить элементы каждой строки матрицы: "
              ))

def sum_row(random_matrix, l):
    result = []

    for row in range(len(random_matrix)):
        row_result = []
        for column in range(len(random_matrix[0])):
            row_result.append(random_matrix[row][column] +
                              random_matrix[l][column]
                              )
        result.append(row_result)
    print(f"В результате сложения элементов строк матрицы с элементами "
          f"строки с индексом {l} получаем матрицу: ")
    for row in result:
        print(row)
    return result


sum_row(random_matrix, l)


#12
from random import randint


def create_random_array(m, n):
    array = [[randint(-100, 100) for row in range(n)] for i in range(m)]
    return array


random_matrix = create_random_array(3, 3)
print("Сгенерированная матрица:")
for row in random_matrix:
    print(row)


h = int(input("Введите значение, наличие которого мы будем проверять "
              "в столбцах матрицы: h = "))


def check_columns(random_matrix, h):
    columns_with_h = []  # Список столбцов, содержащих h
    columns_without_h = []  # Список столбцов, не содержащих h

    for column in range(len(random_matrix[0])):
        column_elements = set()
        for row in random_matrix:
            column_elements.add(row[column])
        if h in column_elements:
            columns_with_h.append(column)
        else:
            columns_without_h.append(column)

    print("Индексы столбцов, содержащих h: ", columns_with_h)
    print("Индексы столбцов, не содержащих h: ", columns_without_h)
    return columns_with_h, columns_without_h


check_columns(random_matrix, h)


#13
from random import randint


def create_random_array(m, n):
    array = [[randint(-100, 100) for row in range(n)] for i in range(m)]
    return array


random_matrix = create_random_array(3, 3)
print("Сгенерированная матрица:")
for row in random_matrix:
    print(row)

def diagonals_sums(random_matrix):
    main_diagonal_sum = 0
    side_diagonal_sum = 0
    # количество элементов диагонали
    elems_in_diagonal = min(len(random_matrix), len(random_matrix[0]))

    for row in range(elems_in_diagonal):
        main_diagonal_sum += random_matrix[row][row]
        side_diagonal_sum += random_matrix[row][(len((random_matrix[0])) -
                                                 1 - row
                                                 )]

    print("Сумма элементов главной диагонали: ", main_diagonal_sum)
    print("Сумма элементов побочной диагонали: ", side_diagonal_sum)

    return main_diagonal_sum, side_diagonal_sum

diagonals_sums(random_matrix)


#14
my_matrix = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 0, 0, 0]
]

def make_even_column(my_matrix):

    new_column = []  # Новый столбец для хранения значений

    # Обходим каждую строку матрицы
    for row in my_matrix:
        count_of_ones = sum(row)  # Считаем количество единиц в строке
        if count_of_ones % 2 == 0:
            new_column.append(0)  # Если четное, добавляем 0
        else:
            new_column.append(1)  # Если нечетное, добавляем 1

    # Добавляем новый столбец к исходной матрице
    for i in range(len(my_matrix)):
        my_matrix[i].append(new_column[i])
    for row in my_matrix:
        print(row)
    return my_matrix
print("Новая мтарица:")
make_even_column(my_matrix)