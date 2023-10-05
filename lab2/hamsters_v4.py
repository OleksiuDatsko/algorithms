import itertools


def get_number_of_hamsters(s: int, c: int, hamsters: list[list[int, int]]) -> int:
    count = 0
    def get_all_combinations(total_hamsters):
        return list(itertools.combinations(hamsters, total_hamsters))

    def get_needed_food_for_each_combiantion(
        combinations: list[tuple[list[int, int]]]
    ) -> list[int]:
        nonlocal count
        total_hamsters = len(combinations[0])
        result = []
        for combination in combinations:
            count += 1
            total_food = 0
            for hamster in combination:
                count += 1
                total_food += hamster[0] + hamster[1] * (total_hamsters - 1)
            result.append(total_food)
        print(result, total_hamsters, combinations)
        return result

    total_hamsters = -1

    while True:
        count += 1
        needed_food = min(
            get_needed_food_for_each_combiantion(
                get_all_combinations(total_hamsters + 1)
            )
        )
        print(needed_food)
        if needed_food > s:
            break
        else:
            print(needed_food, False, total_hamsters + 1)
            total_hamsters += 1
    print(count)
    return total_hamsters


if __name__ == "__main__":
    hamsters = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
    ]
    s = 9
    c = 4

    hamsters = [
        [1, 2],
        [2, 2],
        [3, 1],
    ]
    s = 7
    c = 3
    print(
        "result:",
        get_number_of_hamsters(
            hamsters=hamsters,
            s=s,
            c=c,
        ),
    )
    # print(radix_sort(hamsters))
