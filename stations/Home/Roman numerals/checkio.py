"""Roman numerals - https://checkio.org/mission/roman-numerals/"""

rom_dec = (('M', 1000),
           ('CM', 900),
           ('D', 500),
           ('CD', 400),
           ('C', 100),
           ('XC', 90),
           ('L', 50),
           ('XL', 40),
           ('X', 10),
           ('IX', 9),
           ('V', 5),
           ('IV', 4),
           ('I', 1))


def checkio(data):
    num = data
    result = ''
    for rn in rom_dec:
        times = num // rn[1]
        num = num - (times * rn[1])
        result += rn[0] * times
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
