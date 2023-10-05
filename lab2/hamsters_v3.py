def concat(element: list[int, int]) -> int:
    return int(f"{element[1]}{element[0]}")


def radix_sort(array: list[list[int, int]]) -> list[list[int, int]]:  # O(nd)
    concated_array = [concat(element) for element in array]  # O(n)
    max_element = max(concated_array)  # O(n)
    len_array = len(array)

    digit = 1
    while max_element // digit != 0:  # O(d)
        concated_output = [0] * (len_array)
        output = [0] * (len_array)
        count = [0] * (10)

        print(f"1 -- { max_element // digit}")
        for i in range(0, len_array):  # O(n)
            index = concated_array[i] // digit
            count[index % 10] += 1
            print(f" 2 -- {i}; {index}; {index % 10}")
        print(count)

        for i in range(1, 10):  # O(1)
            print(f" 3 -- {i}")
            count[i] += count[i - 1]
        print(count)

        i = len_array - 1
        for i in range(len_array - 1, -1, -1):  # O(n)
            index = concated_array[i] // digit
            output[count[index % 10] - 1] = array[i]
            concated_output[count[index % 10] - 1] = concated_array[i]
            count[int((index) % 10)] -= 1
            i -= 1

        for i in range(0, len_array):  # O(n)
            array[i] = output[i]
            concated_array[i] = concated_output[i]

        digit *= 10
    print(array)
    return array


def get_number_of_hamsters(s: int, c: int, hamsters: list[list[int, int]]) -> int:
    def can_feed(total_hamsters: int) -> bool:
        total_food = 0
        print("--", total_hamsters, hamsters[:total_hamsters:])
        for hamster in hamsters[:total_hamsters:]:
            total_food += hamster[0] + hamster[1] * (total_hamsters - 1)
            print(total_food, end=" -- ")
            if total_food > s:
                return False
        return True

    radix_sort(hamsters)

    left, right = 0, c
    total_hamsters = 0
    while left <= right:
        print()
        mid = (left + right) // 2
        if can_feed(mid):
            total_hamsters = mid
            left = mid + 1
        else:
            right = mid - 1

    return total_hamsters


if __name__ == "__main__":
    hamsters = [
        [5, 0],
        [2, 2],
        [1, 4],
        [5, 1],
    ]
    s = 19
    c = 4
    print(
        "result:",
        get_number_of_hamsters(
            hamsters=hamsters,
            s=s,
            c=c,
        ),
    )
    # print(radix_sort(hamsters))
