from pprint import pprint


def calculate_transition_function(pattern: str):
    m = len(pattern)

    alphabet = list(set(pattern[:]))
    alphabet.sort()

    def calculate_prefixs(pattern: str) -> int:
        m = len(pattern)
        for i in range(m - 1, 0, -1):
            prefix = pattern[0:i]
            suffix = pattern[m - i : m]
            if prefix == suffix:
                return i
        return 0

    transition_function = [[0 for _ in range(len(alphabet))] for _ in range(m + 1)]

    for q in range(m + 1):
        current_pattern = pattern[0:q]
        print(current_pattern, q)
        for key, letter in enumerate(alphabet):
            if q > m - 1 or letter != pattern[q]:
                transition_function[q][key] = calculate_prefixs(
                    current_pattern + letter
                )
            else:
                transition_function[q][key] = q + 1 if q < m else 0

    pprint(transition_function)

    return transition_function, alphabet


def find_patern(haystack: str, needle: str):
    if not needle:
        return list(range(len(haystack)))

    pattern_lenght = len(needle)

    transition_function, alphabet = calculate_transition_function(needle)

    letters = {letter: key for key, letter in enumerate(alphabet)}

    result = []
    stage = 0
    print("".join([str(i % 10) for i in range(len(haystack))]))
    print(haystack)
    for i, char in enumerate(haystack[:]):
        if char not in letters:
            stage = 0
            print(stage, end="")
            continue
        stage = transition_function[stage][letters[char]]
        print(stage%10, end="")
        if stage == pattern_lenght:
            result.append(i - stage + 1)
    return result


if __name__ == "__main__":
    haystack = "йцукенгшщзхїфівапролджєячсмитьбю."
    needle = "ьбю"
    result = find_patern(haystack, needle)
    print()
    for i in result:
        print(i, haystack[i : i + len(needle)])
