def ShopOLAP(_length: int, items_strings: list) -> list:
    items = {}
    for _i, name_and_quantity in enumerate(items_strings):
        name, quantity = name_and_quantity.split(" ")
        old_quantity = items.get(name, 0)
        items[name] = old_quantity + int(quantity)

    # Convert dictionary to tuples.
    items_by_name_and_quantity = list(zip(items.keys(), items.values()))
    # Sort first by quantity and then by name.
    sorted_items = sorted(items_by_name_and_quantity, key=lambda item: [-item[1], item[0]])
    # Convert tuples to lists.
    sorted_items_lists = list(map(lambda item_and_value: list(item_and_value), sorted_items))
    # Convert lists to strings.
    sorted_items_strings = list(map(lambda item_and_value: " ".join(str(el) for el in item_and_value), sorted_items_lists))
    return sorted_items_strings
