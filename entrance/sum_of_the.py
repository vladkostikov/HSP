def SumOfThe(_length: int, data: list) -> int:
    for i, number in enumerate(data):
        data_without_current_number = data[:i] + data[i+1:]
        sum_of_numbers = sum(data_without_current_number)
        if number == sum_of_numbers:
            return number
    # Return None if not found
    return None
