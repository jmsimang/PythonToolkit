def exponential(a, n):
    """
    Mathematical exponential function, using recursion.

    :param a: The constant/base of the function
    :param n: An integer variable representing the exponent
    :return: The exponential value of a (n times)
    """
    # calculate e
    e = 1 if (n == 0 and a != 0) else \
        (a if n == 1 else (a * exponential(a, n - 1) if n > 1
                           else 1 / (a * exponential(a, (n * -1) - 1))))
    return e
