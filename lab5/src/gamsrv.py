"""
O(n^3)
"""

import os
import heapq

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


def dijkstra(graph, start):
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def get_shortest_paths(graph, clients):
    shortest_paths = {}
    for client in clients:
        shortest_paths[client] = dijkstra(graph, client)
    return shortest_paths


def gamsrv(input_filename: str, output_filename: str):
    (_, _), clients, graph = get_input_data(input_filename, "L")
    shortest_paths = get_shortest_paths(graph, clients)
    result = []
    for not_client in [not_client for not_client in graph if not_client not in clients]:
        sub_result = []
        for client in clients:
            sub_result.append(shortest_paths[client][not_client])
        result.append(max(sub_result))

    min_delay = min(result) or None
    with open(output_filename, "w") as output_file:
        output_file.write(str(min_delay))

    return min_delay


if __name__ == "__main__":
    input_filename = os.path.join(MAIN_DIR, "gamsrv.in")
    output_filename = os.path.join(MAIN_DIR, "gamsrv.out")
    print(gamsrv(input_filename, output_filename))
