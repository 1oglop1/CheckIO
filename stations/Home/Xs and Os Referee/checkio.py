"""Xs and Os Referee - https://checkio.org/mission/x-o-referee/"""


def checkio(game_result):

    O = 'OOO'
    X = 'XXX'

    game_result.append(game_result[0][0] + game_result[1][1] + game_result[2][2])  # m_diag
    game_result.append(game_result[0][2] + game_result[1][1] + game_result[2][0])  # s_diag
    game_result.append(game_result[0][0] + game_result[1][0] + game_result[2][0])  # c0
    game_result.append(game_result[0][1] + game_result[1][1] + game_result[2][1])  # c1
    game_result.append(game_result[0][2] + game_result[1][2] + game_result[2][2])  # c2

    for row in game_result:
        if row == X:
            return 'X'
        if row == O:
            return 'O'
    return "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

    # Precondition:
    # There is either one winner or a draw.
    # len(game_result) == 3
    # all(len(row) == 3 for row in game_result)
