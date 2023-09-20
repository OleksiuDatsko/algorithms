
def generate_matrix(n: int, m: int, print_matrix: bool = False) -> list[list[int]]:
    result = []
    sub_result = []
    for i in range(n):
        for j in range(m):
            sub_result.append((j + i) % (n + m - 1))
        if print_matrix:
            print(sub_result)
        result.append(sub_result)
        sub_result = []
    return result


def zig_zag_path(matrix: list[list[any]]) -> list[any]:
    if not matrix:
        return []

    n = len(matrix)
    m = len(matrix[0])
    result = []

    diagonals = n + m - 1
    
    for diagonal in range(diagonals):
        if diagonal % 2 == 0:
            if diagonal < n:
                i, j = diagonal, 0
            if diagonal >= n:
                i, j = n - 1, diagonal - n + 1
            while i >= 0 and j <= m - 1:
                result.append(matrix[i][j])
                i -= 1
                j += 1
        if diagonal % 2 == 1:
            if diagonal < m:
                i, j = 0, diagonal
            if diagonal >= m:
                i, j = diagonal - m + 1, m - 1
            while j >= 0 and i <= n - 1:
                result.append(matrix[i][j])
                j -= 1
                i += 1
    return result
