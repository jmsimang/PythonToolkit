def combine(l, s, m, e):
    # Using the a and b previously defined in the merge function as it was
    # causing recursion depth errors.
    a = l[s: m]
    b = l[m: e]
    start_index = s
    item_a = 0
    item_b = 0
    # New while loop to test if I'm iterating over both a and b simultaneously.
    # It stops when the condition is false, then I will check the arrays
    # individually.
    while (s + item_a < m) and (m + item_b < e):
        if a[item_a] <= b[item_b]:
            l[start_index] = a[item_a]
            item_a += 1
        else:
            l[start_index] = b[item_b]
            item_b += 1
        start_index += 1
    if s + item_a < m:
        while start_index < e:
            l[start_index] = a[item_a]
            item_a += 1
            start_index += 1
    else:
        while start_index < e:
            l[start_index] = b[item_b]
            item_b += 1
            start_index += 1


def merge(l, s, e):
    if (e - s) > 1:
        mid = (s + e) // 2
        merge(l, s, mid)
        merge(l, mid, e)
        return combine(l, s, mid, e)


def linear_merge(list1, list2):
    if len(list1 + list2) < 2:
        return list1 + list2
    list_combined = list1 + list2
    merge(list_combined, 0, len(list_combined))
    return list_combined
