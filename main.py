
def roman(value):
    if value >= 10:
        return "X" + roman(value-10)
    if value > 7:
        return roman(value - 8) + roman(10)
    elif value == 1:
        return 'I'
    elif value == 2:
        return "II"
    elif value == 10:
        return "X"
    elif value == 7:
        return "VII"
    elif value == 0:
        return ""
