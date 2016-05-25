"""Pawn Brotherhood - https://checkio.org/mission/pawn-brotherhood/"""


def safe_pawns(pawns):
    pawn_indexes = set()

    for p in pawns:
        r = int(p[1]) - 1
        c = ord(p[0]) - 97
        pawn_indexes.add((r, c))
    cnt = 0
    for r, c in pawn_indexes:
        left = (r - 1, c - 1) in pawn_indexes
        right = (r - 1, c + 1) in pawn_indexes
        if left or right:
            cnt += 1

    return cnt


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # safe_pawns({"a1", "d4", "f4", "c3", "e3", "g5", "d2"})

    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
