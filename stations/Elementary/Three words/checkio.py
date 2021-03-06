"""Three words - https://checkio.org/https://checkio.org/mission/three-words/"""


def checkio(words):
    cnt = 0
    # x for x in words.split() if x.isalpha()
    for w in words.split():
        if w.isalpha():
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            return True

    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
