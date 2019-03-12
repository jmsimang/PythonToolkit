def linear_merge(list1, list2):
    """
    Combines elements from two lists and sorts them in ascending order, in linear time.
    :param list1: The first list.
    :param list2: The second list.
    :return: The sorted list with elements from both initial lists.
    """
    # Checks if given lists have more than 1 element. Returns the lists if not.
    if len(list1 + list2) < 2:
        return list1 + list2
    new_list = []
    while (len(list1) > 0) and (len(list2) > 0):
        if min(list1) <= min(list2):
            new_list.append(min(list1))
            del list1[list1.index(min(list1))]
        else:
            new_list.append(min(list2))
            del list2[list2.index(min(list2))]
    for i in list1:
        new_list.append(i)
    for i in list2:
        new_list.append(i)
    return new_list


A = ['f', 'b', 'd']
B = ['c', 'e', 'a', 'a', 'g']
print(linear_merge(A, B))
