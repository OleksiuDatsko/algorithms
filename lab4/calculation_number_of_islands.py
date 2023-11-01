matrix = [
    [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
]

neighborhood_modificators = [
    (1, -1),
    (1, 0),
    (1, 1),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]


def cheack_colisions(i: int, j: int, matrix: list[list]) -> bool:
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def print_matrix(matrix: list[list[int]], zero_value: any = None):
    for i in matrix:
        for j in i:
            print(j if j != zero_value else " ", end=" ")
        print()
    print()


def number_of_islands(matrix: list[list[int]]) -> (int, list[list[int]]):
    def bfs(i: int, j: int, island: int) -> None:
        queue = [(i, j)]

        while queue:
            c_i, c_j = queue.pop(0)
            matrix[c_i][c_j] = island

            for i_m, j_m in neighborhood_modificators:
                i_n, j_n = c_i + i_m, c_j + j_m

                if cheack_colisions(i_n, j_n, matrix) and matrix[i_n][j_n] == 1:
                    queue.append((i_n, j_n))

    num_island = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                num_island += 1
                bfs(i, j, num_island)

    return num_island, matrix


if __name__ == "__main__":
    print("result:", number_of_islands(matrix)[0], "\n")
    print_matrix(matrix, 0)
