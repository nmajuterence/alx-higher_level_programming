def add_integer(a, b=98):
    # Check if both inputs are integers or floats
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast inputs to integers if they are floats
    a = int(a)
    b = int(b)

    # Perform addition and return the result
    return a + b
