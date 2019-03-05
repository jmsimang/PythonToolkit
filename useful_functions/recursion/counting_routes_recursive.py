# Recursive routes count function
def counting_routes_recursive(m, n):
    """ Function to solve lattice paths using normal Recursion
    :param m: horizontal grid boxes
    :param n: vertical grid boxes
    :return: The number of routes through the given path of m x n grid
    """
    return 1 if (m == 0) | (n == 0) else counting_routes_recursive(m, n - 1) + counting_routes_recursive(m - 1, n)
