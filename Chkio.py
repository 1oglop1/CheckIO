pyramid = (
    (1,),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    (3, 1, 3, 1, 3),
    (2, 2, 2, 2, 2, 2),
    (5, 6, 4, 5, 6, 4, 3)
)

pyramid2 = (
    (1,),
    (2, 1),
    (1, 2, 1),
    (1, 2, 1, 1),
    (1, 2, 1, 1, 1),
    (1, 2, 1, 1, 1, 1),
    (1, 2, 1, 1, 1, 1, 9)
)

len_pyramid = len(pyramid)

work = list(list(row) for row in pyramid)
maximum = 0

for row in range(len_pyramid - 1, 0, -1):
    print(pyramid[row])
    current_row = pyramid[row]
    try:
        prev_row = pyramid[row + 1]
    except:
        continue

    for idx, num in enumerate(current_row):
        left = num + prev_row[idx]
        right = num + prev_row[idx + 1]

        print('left', num, prev_row[idx], '=', left)
        print('right', num, prev_row[idx + 1], '=', right)
        print(maximum)
        print('----')
    maximum += max(left, right)


    print(maximum)


def one_step(current_row, prev_row):

    pass
