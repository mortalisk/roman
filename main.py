import math

def roman(value):
    if value < 10:
        if value % 10 == 0:
            return (value % 10) * "X"
        if value == 9:
            return "IX"
        if value == 4:
            return "IV"
        if value == 5:
            return "V"
        return value * "I"

    if value >= 10:
        return "X" + roman(value-10)
    if value > 8:
        return roman(10 - value) + roman(10)
    elif value == 1:
        return 'I'
    elif value == 2:
        return "II"
    elif value == 7:
        return "VII"
    elif value == 8:
        return "VIII"
    elif value == 0:
        return ""
