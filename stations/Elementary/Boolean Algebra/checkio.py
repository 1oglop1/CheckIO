"""Boolean Algebra - https://checkio.org/https://checkio.org/mission/boolean-algebra/"""


def boolean(x, y, operation):
    op = {
        "conjunction": x and y,
        "disjunction": x or y,
        "implication": int(not x or y),
        "exclusive": x ^ y,
        "equivalence": int(not (x ^ y))
    }

    return op[operation]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
