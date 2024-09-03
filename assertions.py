
def avg(numbers):
    assert len(numbers) != 0, '"numbers" should not be empty'
    assert all(isinstance(n, (int, float)) for n in numbers), (
        '"numbers" should contain only numbers'
    )

    return round(sum(numbers) / len(numbers), 2)

try:
    avg([])
except AssertionError as e:
    raise e

try:
    avg([1, 2, 3, 'asd'])
except AssertionError as e:
    print(e)



values = {}
default_value = 0

send_to_db(values['a'])



def create_order(
    client,
    origin,
    destination,
    incoterms,
    # ... и другие важные параметры
):
    if incoterms == 'DAP':
        assert client.client_company == destination.client_company, (
            'client must be the same as delivery address client'
        )
        if client.client_company != destination.client_company:
            raise AssertionError('client must be the same as delivery address client')
    elif incoterms == 'FCA':
        assert destination == origin, (
            'FCA incoterms means that delivery address is the same as origin'
        )

    # ... и другой важный код



import json

def load_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return "File not found"
    except json.JSONDecodeError:
        return "Invalid JSON format"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Пример использования
print(load_json_file("valid_file.json"))  # Ожидается: содержимое JSON файла в виде словаря
print(load_json_file("invalid_file.json"))  # Ожидается: "Invalid JSON format"
print(load_json_file("missing_file.json"))  # Ожидается: "File not found"



class OwnSTR(str):

    def __add__(self, other):
        if isinstance(other, int):
            return super().__add__(str(other))
        elif isinstance(other, float):
            raise TypeError(f"Cannot add float value {other}")

        return super().__add__(str(other))
