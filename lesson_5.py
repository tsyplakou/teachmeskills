# factorial

n = input('Enter a number: ')

while not n.isnumeric():
    print('Invalid input. Please enter a numeric value.')
    n = input('Enter a number: ')
else:
    n = int(n)


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
    return result

sorted
#
# a = 0
# while a < 100:
#     a += 1
#
# line = ''
# while 'wow' not in line:
#     read_next_line()
#
#
# for a in 100:
#     pass
#
# a = [1, 2, 3]
#
#
# # 4! = 4 * 3! = 4 * 3 * 2 * 1 = 24
#
#
# """
# 4. Дана строка. Замените в этой строке все появления буквы h на
# букву H, кроме первого и последнего вхождения.
# Подсказка: использовать метод replace с параметрами.
# Например, дано: ‘hhhabchghhh’, должно быть: ‘hHHabcHgHHh’
# """
#
# test_data = 'adhvhhabchghhas;mfhs'
# #'adhvhhabchghhas;mfhs'
# #'adhvHHabcHgHHas;mfhs'
# #'a' 'd' 'h' vHHabcHgHHas;mfhs'
#
# current_index = 0
# first_h_index = test_data.index('h')
# last_h_index = test_data.rindex('h')
#
# result = ''
#
# for elem in test_data:
#     if current_index not in (first_h_index, last_h_index):
#         result += elem.replace('h', 'H')
#     else:
#         result += elem
#
#     current_index += 1
#
# print(result)
#
# while
#
# x = a + b
#
# for i in range(x):
#     pass


some_string = 'abc'

index = 0
while index < len(some_string):
    print(some_string[index])
    index += 1
else:
    print('Else')

for index in range(len(some_string)):
    print(some_string[index])
else:
    print('Else')


for number in range(1, 100):
    if number == 33:
        break
    print(number)
else:
    print('Loop completed without breaking')

# asflsaf


def abc():
    return

list_of_numbers = [1, 2, 3, 5]
if sum_not_null := sum(list_of_numbers):
    print(sum_not_null)


friuts = ['banana', 'apple', 'cherry']

for nr, element in enumerate(friuts, start=1):
    print(f'{nr}: {element}')
