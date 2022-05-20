import math

def roman(value):
    retval = ""
    if value % 500 == 0:
        retval += (value // 500) * "L"
        value -= (value // 500) * 500
    if value % 400 == 0:
        retval += (value // 400) * "CL"
        value -= (value // 400) * 400
    if value % 100 == 0:
        retval += (value // 100) * "C"
        value -= (value // 100) * 100
    if value % 90 == 0:
        retval += (value // 90) * "XC"
        value -= (value // 90) * 90
    if value % 50 == 0:
        retval += (value // 50) * "L"
        value -= (value // 50) * 50
    if value % 40 == 0:
        retval += (value // 40) * "XL"
        value -= (value // 40) * 40
    if value % 10 == 0:
        retval += (value // 10) * "X"
        value -= (value // 10) * 10
    if value % 9 == 0:
        retval += (value // 9) * "IX"
        value -= (value // 9) * 9
    if value % 5 == 0:
        retval += (value // 5) * "V"
        value -= (value // 5) * 5
    if value % 4 == 0:
        retval += (value // 4) * "IV"
        value -= (value // 4) * 4
    if value % 1 == 0:
        retval += (value // 1) * "I"
        value -= (value // 1) * 1
    return retval
    if value < 100:
        if value == 40:
            return "XL"
        if value == 50:
            return "L"
        if value % 10 == 0:
            return (value // 10) * "X"
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
