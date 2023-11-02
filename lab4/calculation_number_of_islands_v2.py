import ast

neighborhood_modificators = [
    (1, -3),
    (1, 0),
    (1, 3),
    (0, -3),
    (0, 3),
    (-1, -3),
    (-1, 0),
    (-1, 3),
]


def cheack_colisions(i: int, j: int, rows: int, cols: int) -> bool:
    return 0 <= i < rows and 0 <= j < cols


def convert_file_to_adjacency_list(input_file):
    adjacency_list = {}

    with open(input_file, "r") as f:
        lines = f.readlines()

    rows = len(lines)
    cols = len(lines[0]) - 1
    print(rows, cols)
    for i in range(rows):
        for j in range(cols - 1):
            if lines[i][j] == "1":
                neighbors = []
                for i_m, j_m in neighborhood_modificators:
                    n_i, n_j = i + i_m, j + j_m
                    if (
                        cheack_colisions(n_i, n_j, rows, cols)
                        and lines[n_i][n_j] == "1"
                    ):
                        neighbors.append((n_i, n_j // 3))
                adjacency_list[(i, j // 3)] = neighbors

    for key, value in adjacency_list.items():
        print(key, value)

    return adjacency_list


def number_of_islands() -> int:
    visited = []
    islands = 0
    adjacency_list = convert_file_to_adjacency_list("./input.txt")
    
    count = 0

    def bfs(node):
        nonlocal visited
        nonlocal count
        visited.append(node)
        
        queue = [node]
        while queue:
            count += 1
            current_node = queue.pop(0)
            for neighbor in adjacency_list[current_node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

    for node in adjacency_list:
        if node not in visited:
            islands += 1
            bfs(node)
    print(count)
    return islands


if __name__ == "__main__":
    print("result:", number_of_islands())
