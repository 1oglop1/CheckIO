"""Non-unique Elements - https://checkio.org/mission/non-unique-elements/"""


def checkio(data):
    non_unique = [x for x in data if data.count(x) != 1]
    return non_unique


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
