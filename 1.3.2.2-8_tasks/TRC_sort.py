def TRC_sort(trc: list) -> list:
    return trc_sort(trc, -1, 0, len(trc) - 1)


def trc_sort(trc: list, left0: int, right1: int, left2: int) -> list:
    if right1 > left2:
        return trc

    if trc[right1] == 0:
        trc[right1], trc[left0 + 1] = trc[left0 + 1], trc[right1]
        left0 += 1
        right1 += 1
    elif trc[right1] == 1:
        right1 += 1
    elif trc[right1] == 2:
        trc[right1], trc[left2] = trc[left2], trc[right1]
        left2 -= 1

    return trc_sort(trc, left0, right1, left2)
