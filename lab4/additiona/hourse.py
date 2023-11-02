neighborhood_modificators = [
    (1, -2),
    (2, 1),
    (2, 1),
    (1, 2),
    (-1, 2),
    (-2, 1),
    (-2, -1),
    (-1, -2),
]


def cheack_colisions(i: int, j: int, n) -> bool:
    return 0 <= i < n and 0 <= j < n


def print_matrix(matrix: list[list], zero_value: any = None):
    for i in matrix:
        for j in i:
            print(j if j != zero_value else " ", end=" ")
        print()
    print()


def hourse(n: int, start: tuple, end: tuple) -> int:
    matrix = [[float("inf") for _ in range(n)] for _ in range(n)]
    start_i, start_j = start
    end_i, end_j = end
    matrix[start_i][start_j] = 0

    queue = [(start_i, start_j, 0)]
    while queue:
        i, j, value = queue.pop(0)
        matrix[i][j] = value
        for i_m, j_m in neighborhood_modificators:
            i_n, j_n = i + i_m, j + j_m

            if cheack_colisions(i_n, j_n, n) and matrix[i_n][j_n] == float("inf"):
                queue.append((i_n, j_n, value + 1))

    print_matrix(matrix)
    return matrix[end_i][end_j]


print(hourse(8, (7, 0), (0, 7)))
