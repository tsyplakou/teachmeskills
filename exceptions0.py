

def safe_division(dividend, divisor):
    if divisor == 0:
        return 0
    return dividend / divisor


def safe_division(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return 0


result = safe_division(2, 0)
print(result)


