def rec_1(i):
    if i == 1:
        return 1
    return i + rec_1(i - 1)


def rec_2(i):  # Sum of squares
    if i == 1:
        return i ** 2
    return i ** 2 + rec_1(i - 1) ** 2


def rec_3(i):  # Reverse text
    if len(i) == 0:
        return
    return i[1:] + i[0]
