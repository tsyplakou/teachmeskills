
EXIT_INPUT = 'exit'


def read_data_line():
    print("Input 'exit' to stop.")

    def _read_age():
        while True:
            try:
                value = input("Enter your age: ")
                age = int(value)
                break
            except ValueError:
                if value.lower() == EXIT_INPUT:
                    return
                print("Invalid input. Please enter a valid integer.")

        if age < 18:
            print("Invalid input. Please enter a valid integer.")


    while True:
        try:
            salary = float(input("Enter your salary: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid float.")



def read_data_line():
    values = []
    while True:
        try:
            if len(values) == 0:
                values.append(float(input("Enter your salary: ")))
            if len(values) == 1:
                values.append(int(input("Enter your age: ")))
            if len(values) == 2:
                values.append(float(input("Enter your ИМТ: ")))
        except ValueError as e:
            print(f"Invalid input. Please enter a valid float: {e}")
            print(f"Invalid input. Please enter a valid int: {e}")


def validate_data(values):
    pass



class ReportValidationError(Exception):
    pass

