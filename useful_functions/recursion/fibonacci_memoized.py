# Note: Memoized recursion often requires more memory
def fibonacci_memoized(n, cache={}):
    """
    Function generates the nth number in the fibonacci sequence, using recursion and
    memoization to handle numbers that occur more than once.
    :param cache: The results cache
    :param n: The whole number
    :return: The nth number in the fibonacci sequence
    """
    try:
        if n < 0:
            raise ValueError('Input error: n must be a whole number, i.e., from zero going up')
        return 0 if n == 0 else (1 if n < 3 else cache[n])
    except ValueError as ve:
        print(str(ve))
    except KeyError:
        cache[n] = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
        return cache[n]



