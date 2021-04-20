def shutter(string):
    """If shutter() gets an empty parameter, returns the same.
    Else, the first index value of the parameter is
    multiplied and the remaining values are processed the same way using a recursive call"""
    if not string:
        return string
    first_val = string[0]
    remainder = string[1:]
    return (first_val * 2) + shutter(remainder)


def number(string):
    """If an empty value is sent to the parameter, it returns 0.
    Otherwise, it checks if the first element is an integer,
    if so keeps adding with rest of the elements on a recursive call with the same condition"""
    if not string:
        return 0
    some = string[0]
    value = int(some) if some.isdigit() else 0
    return value + number(string[1:])


if __name__ == '__main__':
    print(shutter(string='Vignesh'))
    print(number(string='v1gn35H'))
