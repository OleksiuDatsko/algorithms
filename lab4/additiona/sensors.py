matrix = [
#    0  1  2  3  4  5  6  7  8  9
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],  # 0
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 1
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 3
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # 4
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # 7
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 9
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

move_modificators = [
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, 0),
]


def is_danger(i: int, j: int, matrix: list[list]):
    for i_m, j_m in neighborhood_modificators:
        i_n, j_n = i + i_m, j + j_m

        if cheack_colisions(i_n, j_n, matrix) and matrix[i_n][j_n] == 0:
            return True
    return False

def is_end(i: int, j: int, matrix: list[list]):
    return j == len(matrix[0]) - 1


def cheack_colisions(i: int, j: int, matrix: list[list]) -> bool:
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def print_matrix(matrix: list[list[int]], zero_value: any = None):
    for i in matrix:
        for j in i:
            print(j if j != zero_value else " ", end=" ")
        print()
    print()


def sensors(matrix: list[list[int]]):
    adjacency_list = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 and not is_danger(i, j, matrix):
                neighbors = []
                for i_m, j_m in move_modificators:
                    n_i, n_j = i + i_m, j + j_m
                    if (
                        cheack_colisions(n_i, n_j, matrix)
                        and matrix[n_i][n_j] == 1
                        and not is_danger(n_i, n_j, matrix)
                    ):
                        neighbors.append((n_i, n_j))
                adjacency_list[(i, j)] = neighbors

    path = 0
    visited = []
    
    def bfs(node):
        length = 0
        nonlocal visited
        visited.append(node)

        queue = [(node, length)]
        while queue:
            current_node, length = queue.pop(0)
            if is_end(*current_node, matrix):
                return length
            for neighbor in adjacency_list[current_node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append((neighbor, length + 1))
        return None
    
    for key, _ in adjacency_list.items():
        if key[1] == 0:
            print(bfs(key))
    
    return path

sensors(matrix)
