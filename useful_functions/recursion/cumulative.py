def cumulative(n):
    """
    Function calculates the cumulative sum of all positive integers up to n, using recursion.

    :param n: Positive integer
    :return: Sum of all positive integers up to n
    """
    try:
        assert n > 0
        return n if n == 1 else n + cumulative(n - 1)
    except AssertionError:
        print('Input error: n must be positive integer, i.e., greater than zero')

