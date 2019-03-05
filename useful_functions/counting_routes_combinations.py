
def count_routes_combinations(n):
    """
    Combinatorics to calculate the number of routes to solve the lattice problem
    :param n: Grid size
    :return: The number of routes in the given grid
    """
    result = 1
    for i in range(n):
        result *= (n + i + 1) / (i + 1)
    return result
