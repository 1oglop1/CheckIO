"""Count Neighbours - https://checkio.org/mission/count-neighbours/"""


def count_neighbours(grid, row, col):
    n_col = len(grid[0])
    n_row = len(grid)
    neigh = 0

    for r in range(-1, 2):
        for c in range(-1, 2):
            rog = row + r
            cog = col + c
            # print (r,c,'len', g_len, (rog,cog), 0<= cog < g_len)
            # print ('len', g_len, (rog,cog))
            # print(rog, cog)
            if c == 0 and r == 0:
                continue
            if (0 <= rog < n_row) and (0 <= cog < n_col):
                neigh += grid[rog][cog]
    print("neigh", neigh)

    return neigh


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
