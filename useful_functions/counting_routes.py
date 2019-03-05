# import the required libraries
import numpy as np
from matplotlib import pyplot as plt
plt.interactive(True)


def count_routes_iterative(m, n):
    # np.array does not allow assignment, use ndarray instead
    # grid = np.ndarray((m + 1, n + 1))
    grid2 = np.zeros((m + 1, n + 1), dtype=int)

    # base case - when m or n equals 0, which the result is always 1
    # for i in range(m + 1):
    #     grid[i][0] = 1
    # for j in range(n + 1):
    #     grid[0][j] = 1

    for i in range(m + 1):
        grid2[i][0] = 1
    for j in range(n + 1):
        grid2[0][j] = 1

    # Print grid to check contents
    # print(grid, '\n')
    # print(grid2, '\n')

    # iterate across all i <= m and j <= n to calculate and storing each result in the array
    # for i in range(1, m + 1):
    #     for j in range(1, n + 1):
    #         grid[i][j] = grid[i-1][j] + grid[i][j-1]
    # setting each cell equal to two adjacent cells
    # print(grid, '\n')

    # iterate across all i <= m and j <= n to calculate and storing each result in the array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            grid2[i][j] = grid2[i - 1][j] + grid2[i][j - 1]
            # setting each cell equal to two adjacent cells
    # print(grid2)

    # return final grid cell
    return grid2[m][n]


print(count_routes_iterative(20, 20))
