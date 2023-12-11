from pprint import pprint

def calculate_prefixs(pattern: str) -> int:
    m = len(pattern)
    for i in range(m - 1, 0, -1):
        prefix = pattern[0:i]
        suffix = pattern[m - i : m]
        if prefix == suffix:
            return i
    return 0

def calculate_transition_function(pattern: str):
    m = len(pattern)

    alphabet = list(set(pattern[:]))
    alphabet.sort()

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
    # print("".join([str(i % 10) for i in range(len(haystack))]))
    # print(haystack)
    for i, char in enumerate(haystack[:]):
        if char not in letters:
            stage = 0
            # print(stage, end="")
            continue
        stage = transition_function[stage][letters[char]]
        # print(stage % 10, end="")
        if stage == pattern_lenght:
            result.append(i - stage + 1)
    return result


if __name__ == "__main__":
    haystack = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer tincidunt a felis non bibendum. Nulla vestibulum ipsum nec massa interdum, ut consectetur ipsum porta. In cursus luctus augue, sed blandit massa imperdiet eget. Cras porta ex at tortor porta, sit amet cursus ante lobortis. Cras at pulvinar nibh, in convallis risus. Suspendisse congue nec urna vel fermentum. Cras pulvinar faucibus purus et pellentesque. Phasellus nec finibus diam.Donec semper tortor augue, ut suscipit ex cursus sit amet. Proin diam orci, varius sit amet finibus nec, accumsan sed odio. Nunc in nisl pharetra, commodo nulla sit amet, dignissim augue. Donec vel velit mollis neque ullamcorper mollis. Sed ornare diam a auctor finibus. Vestibulum mollis pulvinar quam, a mollis urna pretium quis. Proin faucibus libero a massa efficitur pretium. Maecenas at pulvinar elit, nec maximus libero. Donec et gravida nulla, at aliquet eros. Fusce rutrum congue maximus. Nam at tincidunt neque.Vivamus tempus nisl sit amet ex semper egestas. Maecenas et purus sed nunc interdum tempor ac et urna. Vivamus aliquet nec sem ut scelerisque. Phasellus ultrices et risus et varius. Aenean efficitur leo tortor, non suscipit arcu varius in. Pellentesque laoreet, libero ac cursus varius, magna nulla convallis justo, sit amet dapibus mauris massa consectetur lacus. Phasellus mollis egestas massa vel vulputate. Vestibulum sodales sit amet lacus id lacinia. In tempor enim vitae nisi fringilla ullamcorper non sit amet est. Pellentesque sed velit diam. In id nisl lectus. Nulla non iaculis ex. Phasellus viverra facilisis turpis eget facilisis. In hac habitasse platea dictumst. Curabitur urna sem, faucibus vehicula tristique sed, laoreet rhoncus augue.Sed ac tristique metus. Maecenas dapibus quis nibh nec ultricies. Nullam a turpis id nulla egestas pretium sed nec nulla. Vestibulum imperdiet tempor malesuada. Morbi laoreet tincidunt diam, eget dapibus justo feugiat rutrum. Integer pellentesque iaculis posuere. Phasellus volutpat purus arcu, at faucibus nunc bibendum vitae. Duis facilisis velit sed nibh malesuada feugiat. Donec malesuada mi at ante sagittis, vitae dictum diam blandit. Ut egestas maximus mauris sit amet mattis. Fusce ut consequat neque, ac tempor dui. Maecenas dignissim tempor velit at ornare. Aenean feugiat hendrerit ex in sagittis. Aenean efficitur sem dui. Curabitur pulvinar elit risus, malesuada ornare sapien sollicitudin a. Etiam ut lectus tempus augue sollicitudin luctus in a odio.Vivamus ut ex sem. Ut sed risus sit amet dui auctor lobortis sed ac eros. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla convallis augue et augue dapibus dignissim. Curabitur quis commodo tortor, nec gravida arcu. Nunc ullamcorper arcu ut odio aliquet mollis. Vivamus posuere venenatis ornare. Duis rutrum feugiat ligula."
    needle = "sit amet,"
    result = find_patern(haystack, needle)
    print(len(haystack))
    for i in result:
        print(i, haystack[i : i + len(needle)])
