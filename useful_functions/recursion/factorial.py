def factorial(n):
    """
    Calculates the factorial of n

    :param n: The number n
    :return: The factorial of n
    """
    try:
        assert n >= 1
        return n if n == 1 else n * factorial(n - 1)
    except AssertionError:
        print('Error: n must be a positive integer')
