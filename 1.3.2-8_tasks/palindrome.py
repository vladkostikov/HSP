def palindrome(string: str, step: int = 0) -> bool:
    if step >= len(string) // 2:
        return True

    first_char_for_step = string[step]
    last_char_for_step = string[-1 - step]
    if first_char_for_step != last_char_for_step:
        return False

    return palindrome(string, step + 1)
