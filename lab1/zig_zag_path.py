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
        if diagonal % 2 != 0:
            if diagonal < n:
                i, j = diagonal, 0
            if diagonal >= n:
                i, j = n - 1, diagonal - n + 1
            while i >= 0 and j <= m - 1:
                result.append(matrix[i][j])
                i -= 1
                j += 1
        if diagonal % 2 != 1:
            if diagonal < m:
                i, j = 0, diagonal
            if diagonal >= m:
                i, j = diagonal - m + 1, m - 1
            while j >= 0 and i <= n - 1:
                result.append(matrix[i][j])
                j -= 1
                i += 1
    return result



def buble_sort(input_array: list[int]) -> list[int]:
    i = 0
    count = 0
    swapped = False
    while i < len(input_array):
        j = 0
        count += 1
        swapped = False
        while j < len(input_array) - 1:
            if input_array[j] > input_array[j + 1]:
                swapped = True
                input_array[j], input_array[j + 1] = input_array[j + 1], input_array[j]
            count += 1
            j += 1
        if not swapped:
            break
        i += 1
    print(count)
    return input_array 


if __name__ == "__main__":
    print(buble_sort([i for i in range(5, 0, -1)]))