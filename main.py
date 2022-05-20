
def roman(value):
    if value >= 10:
        return "X" + roman(value-10)
    elif value == 1:
        return 'I'
    elif value == 10:
        return "X"
    elif value == 7:
        return "VII"
