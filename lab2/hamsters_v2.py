def get_number_of_hamsters(s: int, c: int, hamsters: list[list[int, int]]) -> int:
    """
    sort(c) = c*log(c) => o(c*log(c))
    log(c)*(c*log(c) + c) = c*log(c)*(log(c) + 1) = c*(log(c))^2 = 2c*log(c) = c*log(c)

    sort(c) = c^2 => o(c^2*log(c))
    log(c)*(c^2 + c) = c*log(c)*(2c) = 2*c^2*log(c) = c^2*log(c)
    """
    count = 0
    resulted_hamsters = []

    def can_feed(hamsters_count: int) -> bool:
        nonlocal count
        nonlocal resulted_hamsters
        neighbors = hamsters_count - 1
        hamsters_sorted = hamsters.copy()
        hamsters_sorted.sort(key=lambda h: h[0] + h[1] * neighbors)
        total_food_needed = 0
        for i in range(neighbors):
            count += 1
            food_needed = hamsters_sorted[i][0] + neighbors * hamsters_sorted[i][1]
            total_food_needed += food_needed
            resulted_hamsters.append(hamsters_sorted[i])
            print(hamsters_sorted[i], food_needed)
            if total_food_needed >= s:
                return False
        return True

    left, right = 0, c
    total_hamsters = 0
    while left <= right:
        resulted_hamsters = []
        print()
        count += 1
        mid = (left + right) // 2
        if can_feed(mid):
            total_hamsters = mid
            left = mid + 1
        else:
            right = mid - 1
    print(count, c, s)
    print(resulted_hamsters)
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
    print(
        "result:",
        get_number_of_hamsters(
            hamsters=hamsters,
            s=s,
            c=c,
        ),
    )
