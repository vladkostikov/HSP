def TRC_sort(trc: list) -> list:
    left0 = -1
    right1 = 0
    left2 = len(trc) - 1

    while right1 <= left2:
        if trc[right1] == 0:
            trc[right1], trc[left0 + 1] = trc[left0 + 1], trc[right1]
            left0 += 1
            right1 += 1
        elif trc[right1] == 1:
            right1 += 1
        elif trc[right1] == 2:
            trc[right1], trc[left2] = trc[left2], trc[right1]
            left2 -= 1

    return trc
