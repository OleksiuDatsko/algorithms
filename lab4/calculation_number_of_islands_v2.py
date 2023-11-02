import ast

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


def convert_file_to_adjacency_list(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
        matrix = [list(ast.literal_eval(row)) for row in lines]

    adjacency_list = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                neighbors = []
                for i_m, j_m in neighborhood_modificators:
                    n_i, n_j = i + i_m, j + j_m
                    if cheack_colisions(n_i, n_j, matrix) and matrix[n_i][n_j] == 1:
                        neighbors.append((n_i, n_j))
                adjacency_list[(i, j)] = neighbors

    return adjacency_list


def number_of_islands() -> int:
    visited = []
    islands = 0
    adjacency_list = convert_file_to_adjacency_list("./input.txt")

    def bfs(node):
        nonlocal visited
        visited.append(node)

        queue = [node]
        while queue:
            current_node = queue.pop(0)
            for neighbor in adjacency_list[current_node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

    for node in adjacency_list:
        if node not in visited:
            islands += 1
            bfs(node)

    return islands


if __name__ == "__main__":
    print("result:", number_of_islands())

