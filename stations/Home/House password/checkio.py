"""House password - https://checkio.org/mission/house-password/"""


def checkio(data):
    has_digit = False
    has_uppercase = False
    has_lowercase = False
    if len(data) < 10 and data.isalnum():
        return False
    else:

        for c in data:
            if c.isdigit():
                has_digit = True
            if c.islower():
                has_lowercase = True
            if c.isupper():
                has_uppercase = True
    return has_digit and has_lowercase and has_uppercase


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
