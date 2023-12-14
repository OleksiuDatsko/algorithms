def get_input_data(
    input_filename: str,
) -> list[list[int]]:
    with open(input_filename, "r") as input_file:
        (w, h) = tuple(int(i) for i in input_file.readline().strip().split())
        data = input_file.readlines()

    tiles = []

    for line in data:
        tiles.append([tile for tile in line.strip()])

    return (w, h), tiles


def ijones(input_filename: str, output_filename: str):
    counter = 0
    (w, h), tiles = get_input_data(input_filename)
    s_tiles = [[0 for _ in range(w)] for _ in range(h)]

    alphabet: dict = {}

    for i in range(h):
        counter += 1
        s_tiles[i][0] = 1
        if tiles[i][0] not in alphabet:
            alphabet[tiles[i][0]] = 0
        alphabet[tiles[i][0]] += 1
        j = 0
        print(tiles[i][j],s_tiles[i][j], alphabet, i, j)

    print()
    for j in range(1, w):
        sub_alphabet: dict = {}
        for i in range(h):
            counter += 1
            s_tiles[i][j] = alphabet.get(tiles[i][j], 0)
            if tiles[i][j] != tiles[i][j - 1]:
                s_tiles[i][j] += s_tiles[i][j - 1]

            if tiles[i][j] not in sub_alphabet:
                sub_alphabet[tiles[i][j]] = 0
            sub_alphabet[tiles[i][j]] += s_tiles[i][j]
            print(tiles[i][j], s_tiles[i][j], alphabet, i, j, sub_alphabet)
        for key, val in sub_alphabet.items():
            if key not in alphabet:
                alphabet[key] = val
            else:
                alphabet[key] += val
        print()

    print(alphabet)
    print(s_tiles)

    result = s_tiles[0][w - 1] + s_tiles[h - 1][w - 1]
    if h == 1:
        result //= 2
    print(result, counter)
    with open(output_filename, "w") as output_file:
        output_file.write(str(result))


if __name__ == "__main__":
    ijones("data/ijones.in", "data/ijones.out")
