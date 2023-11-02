from enum import Enum

from termcolor import colored

class Colors(Enum):
    Y="yellow"
    G="green"
    X="black"
    W="white"
    R="red"
    B="blue"

matrix = [
    [Colors.Y, Colors.Y, Colors.Y, Colors.G, Colors.G, Colors.G, Colors.G, Colors.G, Colors.G, Colors.G],
    [Colors.Y, Colors.Y, Colors.Y, Colors.Y, Colors.Y, Colors.Y, Colors.G, Colors.X, Colors.X, Colors.X],
    [Colors.G, Colors.G, Colors.G, Colors.G, Colors.G, Colors.G, Colors.G, Colors.X, Colors.X, Colors.X],
    [Colors.W, Colors.W, Colors.W, Colors.W, Colors.W, Colors.G, Colors.G, Colors.G, Colors.G, Colors.X],
    [Colors.W, Colors.R, Colors.R, Colors.R, Colors.R, Colors.R, Colors.G, Colors.X, Colors.X, Colors.X],
    [Colors.W, Colors.W, Colors.W, Colors.R, Colors.R, Colors.G, Colors.G, Colors.X, Colors.X, Colors.X],
    [Colors.W, Colors.B, Colors.W, Colors.R, Colors.R, Colors.R, Colors.R, Colors.R, Colors.R, Colors.X],
    [Colors.W, Colors.B, Colors.B, Colors.B, Colors.B, Colors.R, Colors.R, Colors.X, Colors.X, Colors.X],
    [Colors.W, Colors.B, Colors.B, Colors.X, Colors.B, Colors.B, Colors.B, Colors.B, Colors.X, Colors.X],
    [Colors.W, Colors.B, Colors.B, Colors.X, Colors.X, Colors.X, Colors.X, Colors.X, Colors.X, Colors.X],
]

neighborhood_modificators = [
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, 0),
]



def cheack_colisions(i: int, j: int, matrix: list[list]) -> bool:
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def print_matrix(matrix: list[list[Colors]], zero_value: any = None):
    for i in matrix:
        for j in i:
            print(colored(j.name, j.value) if j != zero_value else " ", end=" ")
        print()
    print()

def colors(start: tuple, color_change_to: str):
    i, j = start
    queue = [(start)]
    current_color = matrix[i][j]
    while queue:
        c_i, c_j = queue.pop(0)
        matrix[c_i][c_j] = color_change_to

        for i_m, j_m in neighborhood_modificators:
            i_n, j_n = c_i + i_m, c_j + j_m

            if cheack_colisions(i_n, j_n, matrix) and matrix[i_n][j_n] == current_color:
                queue.append((i_n, j_n))
    return matrix


print_matrix(matrix)
print_matrix(colors((3, 9), Colors.Y), )
