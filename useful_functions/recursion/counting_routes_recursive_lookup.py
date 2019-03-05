from matplotlib import pyplot as plt
plt.interactive(True)


def counting_routes_r(m, n, cache={}):
    """ Function to solve lattice paths using Memoization
    :param m: horizontal grid boxes
    :param n: vertical grid boxes
    :param cache: cached results when inputs occur again
    :return: The number of routes through the given path of m x n grid
    """
    # base/stop case - put everything in brackets or you get RecursionError
    try:
        return 1 if (m == 0) | (n == 0) else cache[(m, n)]
    except KeyError:
        # optimization technique to store results of expensive functions calls returns the cached
        # result when the same inputs occur again.
        cache[(m, n)] = counting_routes_r(m, n - 1, cache) + counting_routes_r(m - 1, n, cache)
        return cache[(m, n)]

