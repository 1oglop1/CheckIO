"""The end of other - https://checkio.org/mission/end-of-other/"""

import itertools


def checkio(ws):
    """Return True if pair of words in set, such that one word is the end of another (a suffix of another)"""
    comb = itertools.combinations(ws, 2)
    ws = sorted(w[::-1] for w in ws)
    print(ws)
    for c in comb:
        if len(c[0]) >= len(c[1]):
            ret = c[0].endswith(c[1])
        else:
            ret = c[1].endswith(c[0])

        if ret:
            return ret

    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"

    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
