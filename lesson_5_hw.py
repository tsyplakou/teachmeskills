# 1
# в целом справились, из интересного - вариант спросить сколько знаков точность нужна
# и в цикле смотреть как меняется результат - user-friendly
# вариант с фиксированным количеством повторений тоже рабочий

# 2
def loot_money(price, k) -> int:
    wallet = 0
    days = 0
    while True:
        days += 1

        if days % 7 == 0:
            wallet += k

        if wallet >= price:
            return days


# 3
prev = 1
next = 1

n = 0

print(prev, end=' ')
while n < 10:
    print(next, end=' ')
    prev, next = next, prev + next
    n += 1


# 4
import random

_list = [random.randint(1, 100) for _ in range(100)]

_max = _list[0]
_min = _list[0]
_sum = 0

for elem in _list:
    if elem > _max:
        _max = elem
    if _min < elem:
        _min = elem
    _sum += elem


# 5
def is_unique(lst):
    duplicates = {}
    for elem in lst:
        if elem in duplicates:
            duplicates[elem] += 1
        else:
            duplicates[elem] = 1

    for elem, count in duplicates.items():
        if count > 1:
            print(f'Element {elem} is duplicated {count} times.')


# 6 binary search:
def binary_search(n, l: list) -> int:
    start = 0
    end = len(l) - 1

    while start <= end:
        middle = (start + end) // 2

        if l[middle] == n:
            return middle
        elif l[middle] < n:
            start = middle + 1
        else:
            end = middle - 1

    return -1


# 7
def search_rotated_array(n, l: list) -> int:
    left, right = 0, len(l) - 1

    while left <= right:
        mid = (left + right) // 2

        # Если нашли элемент, возвращаем его индекс
        if l[mid] == n:
            return mid

        # Определяем, какая часть отсортирована
        if l[left] <= l[mid]:
            # Левая часть отсортирована
            if l[left] <= n < l[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Правая часть отсортирована
            if l[mid] < n <= l[right]:
                left = mid + 1
            else:
                right = mid - 1

    # Если элемент не найден, возвращаем -1
    return -1

# Пример использования
l = [5, 6, 7, 1, 2, 3, 4]
n = 3
index = search_rotated_array(l, n)
print(f"Индекс искомого элемента {n} в списке: {index}")
