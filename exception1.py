# ValueError, TypeError, SyntaxError, IndexError, IndentationError, KeyError, ...

#excel report



def c():
    raise Exception('WOW')
    print('c')


def b():
    print('b')
    c()
    print('b1')



def a():
    print('a')
    b()
    print('a1')


def main():
    try:
        a()
    except Exception as e:
        print(f'Error: {e}')


try:
    pass
except (IndexError, AssertionError) as a:
    print(a)
    print('Invalid value')
except ValueError:
    pass
else:
    pass
finally:
    pass



class ValidationError(Exception):
    pass


def validate_price(price):
    try:
        price = int(price)
    except TypeError:
        raise ValidationError(f'Invalid value: {price}.')

    if price <= 0:
        raise ValidationError(f'Price can\'t be zero or negative: {price}')

    if price > 1000:
        raise ValidationError(f'Price can\'t be more than 1000: {price}')

    return price


def validate_report():
    COLUMNS = {
        2: validate_price,
    }

try:
    price = validate_price('a10')
except ValidationError as e:
    send_answer_to_client(str(e))
else:
    set_price_to_db(price)


try:
    pass
except Exception as e:
    print(str(e))
    raise e
except ValueError as ve:
    print(str(ve).split('\'')[1])

