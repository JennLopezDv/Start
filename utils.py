# utils.py
# Validations and reusable tools

def validate_positive_int(value):
    if not value.isdigit():
        raise ValueError("Error: value must be a positive integer.")
    value = int(value)
    if value <= 0:
        raise ValueError("Error: value must be greater than zero.")
    return value


def validate_positive_float(value):
    try:
        value = float(value)
    except ValueError:
        raise ValueError("Error: value must be a positive number.")
    if value <= 0:
        raise ValueError("Error: value must be greater than zero.")
    return value
