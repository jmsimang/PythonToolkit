def fibonacci(n):
    """
    Function generates the nth number in the fibonacci sequence, using recursion.

    :param n: A whole number
    :return: The nth number in the fibonacci sequence
    """
    try:
        assert n > -1
        return 0 if n == 0 else (1 if n < 3 else (fibonacci(n-1) + fibonacci(n-2)))
    except AssertionError:
        print('Input error: n must be a whole number, i.e., from zero onwards')
