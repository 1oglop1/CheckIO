"""The Most Wanted Letter - https://checkio.org/mission/most-wanted-letter/"""


def checkio(text):
    mw = {}
    for letter in text.lower():
        if letter in mw and letter.isalpha():
            mw[letter] += 1
        else:
            mw[letter] = 1
    print(mw)
    m = ['', 0]
    # ch = False
    for k, v in mw.items():
        print(k, v)
        if v > m[1]:
            m[1] = v
            m[0] = k
    b = {}
    for k, v in mw.items():
        if mw[k] == m[1] and k.isalpha():
            b[k] = v
    print(b)
    return min(b)
    # replace this for solution


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
