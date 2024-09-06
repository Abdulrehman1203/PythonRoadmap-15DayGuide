try:
    try:
        raise ValueError("ValueError")
    except ValueError as e1:
        raise TypeError("TypeError") from e1
except TypeError as e2:
    print("The exception was", repr(e2))
    print("Its __context__ was", repr(e2.__context__))
    print("Its __cause__ was", repr(e2.__cause__))
