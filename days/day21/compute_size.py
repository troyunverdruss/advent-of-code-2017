size = 3

for _ in range(18):
    if size % 2 == 0:
        size = size / 2 * 3
    else:
        size = size / 3 * 4

    if size % 2 == 0:
        subdivisible_squares = (size / 2) * (size / 2)
    else:
        subdivisible_squares = (size / 3) * (size / 3)

    print('Size: {}, area: {}, subdivisible squares: {}'.format(size, size * size, subdivisible_squares))
