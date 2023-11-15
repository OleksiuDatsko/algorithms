"""
O(n^3)
"""

import os

MAIN_DIR = "src/data"


def get_input_data(
    input_filename: str, output_type: str
) -> tuple[tuple[int, int], tuple[int], dict[int, int] | list[list[int]]]:
    with open(input_filename, "r") as input_file:
        data = input_file.readlines()

    (m, n) = tuple(int(i) for i in data[0].strip().split())
    clients = tuple(int(i) for i in data[1].strip().split())

    if output_type == "L":
        graph: dict[int, list[tuple[int, int]]] = {}

        for line in data[2::]:
            line = [int(i) for i in line.strip().split()]
            if line[0] not in graph:
                graph[line[0]] = []
            graph[line[0]].append((line[1], line[2]))

            if line[1] not in graph:
                graph[line[1]] = []
            graph[line[1]].append((line[0], line[2]))

    if output_type == "M":
        graph: list[list[int]] = [[float("inf") for _ in range(m)] for _ in range(m)]

        for line in data[2::]:
            line = [int(i) - 1 for i in line.strip().split()]
            graph[line[0]][line[1]] = line[2] + 1
            graph[line[1]][line[0]] = line[2] + 1

    return (m, n), clients, graph


def floyd_warshall(matrix: list[list[int]]):
    distance = matrix.copy()
    n = len(distance)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance


def gamsrv(input_filename: str, output_filename: str):
    (n, _), clients, graph = get_input_data(input_filename, "M")
    not_clients = [i for i in range(1, n) if i not in clients]

    roud_matrix = floyd_warshall(graph)
    result = []
    for not_client in not_clients:
        sub_result = []
        for client in clients:
            sub_result.append(roud_matrix[client - 1][not_client - 1])
        result.append(max(sub_result))

    with open(output_filename, "w") as output_file:
        output_file.write(str(min(result)))

    return result


if __name__ == "__main__":
    input_filename = os.path.join(MAIN_DIR, "gamsrv.in")
    output_filename = os.path.join(MAIN_DIR, "gamsrv.out")
    print(gamsrv(input_filename, output_filename))
