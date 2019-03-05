def binary_search(elements, value):
    """
    User-defined binary search function.
    :param elements: List of iterable items.
    :param value: The item being search for.
    :return: The index of the searched item or None
    """
    if len(elements) == 1:
        return 0 if elements[0] == value else None
    mid = len(elements) // 2
    if elements[mid] == value:
        return mid
    return binary_search(elements[:mid], value) if elements[mid] > value else mid + binary_search(elements[mid:], value)
