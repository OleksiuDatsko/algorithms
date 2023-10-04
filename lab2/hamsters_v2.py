def get_number_of_hamsters(s: int, c: int, hamsters: list[list[int, int]]) -> int:
    """
    o(c*log(c))

    sort(c) = c*log(c)
    log(c)*(c*log(c) + c) = c*log(c)*(log(c) + 1) = c*(log(c))^2 = 2c*log(c) = c*log(c)
    """

    def can_feed(neighbors: int) -> bool:
        hamsters_sorted = hamsters.copy()
        hamsters_sorted.sort(key=lambda h: h[0] + h[1] * neighbors, reverse=True)
        total_food_needed = 0
        for i in range(neighbors):
            food_needed = hamsters_sorted[i][0] + neighbors * hamsters_sorted[i][1]
            total_food_needed += food_needed
            if total_food_needed > s:
                return False
        return True

    left, right = 0, c
    total_hamsters = 0
    while left <= right:
        mid = (left + right) // 2
        if can_feed(mid):
            total_hamsters = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return total_hamsters


if __name__ == "__main__":
    hamsters = [
        [1, 50000],
        [1, 60000],
    ]
    s = 2
    c = 2
    print(
        get_number_of_hamsters(
            hamsters=hamsters,
            s=s,
            c=c,
        )
    )
