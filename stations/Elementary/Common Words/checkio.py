"""Common Words - https://checkio.org/mission/common-words/"""


def checkio(first, second):
    return ",".join(sorted(set.intersection(set(first.split(',')), set(second.split(',')))))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
