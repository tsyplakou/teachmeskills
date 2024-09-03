


def sum_of_two(a, b):
    return a + b

sum_of_two = lambda a, b: a + b



map(lambda , [1, 2, 3, 4, 5])







lst = [1, 2, 3, 4, 5, 9, 10, 12, 13]
result = []

for num in lst:
    if num % 2 == 0:
        result.append(num)
print(num)

result = [
    f'{num:.2f}'
    for num, a in zip(lst, lst)
    if (num % 2 == 0 or False)
]

initial_dict = {
    _int: 0
    for _int in range(10)
}

a = {
    key: value
    for key, value in zip(
        [1, 2, 3, 4, 5, 6, 7],
        [-1, -2, -3, -4, -5, -6, -7],
    )
}


data = [
    (1, 'First name', 'Last name'),
    (2, 'First name', 'Last name'),
]

list_of_dicts = [
    {
        'id': row[0],
        'first_name': row[1],
        'last_name': row[2],
    } for row in data
]

list_of_dicts = []
for row in data:
    list_of_dicts.append({
        'id': row[0],
        'first_name': row[1],
        'last_name': row[2],
    })




list(
    filter(
        lambda elem: isinstance(elem, int) and not isinstance(elem, bool),
        [1, 2, 3, 4, 5, 6, 0, None, False, True]
    )
)



















def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Код, который выполняется до вызова исходной функции
        print("Что-то делаем до вызова функции")

        # Вызов исходной функции
        result = func(*args, **kwargs)

        # Код, который выполняется после вызова исходной функции
        print("Что-то делаем после вызова функции")

        # Возвращаем результат вызова исходной функции
        return result

    return wrapper

def memoize(max_size=1000):
    def _memoize(func):
        cache = {}

        def wrapper(*args):
            if args in cache:
                return cache[args]
            else:
                result = func(*args)
                cache[args] = result
                return result

        return wrapper
    return _memoize


@timeit
@memoize
def factorial(n):
    print(f"Calculating factorial of {n}")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
