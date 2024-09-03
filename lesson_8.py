


while True:
    val = input('Number:')
    if val.isdigit():
        num = int(val)
        break


while True:
    try:
        val = input('Number:')
        break
    except ValueError:
        print('Invalid input. Please enter a number.')
        continue
