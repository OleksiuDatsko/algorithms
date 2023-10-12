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

        for i in range(0, len_array):  # O(n)
            index = concated_array[i] // digit
            count[index % 10] += 1

        for i in range(1, 10):  # O(1)
            count[i] += count[i - 1]

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


def get_number_of_hamsters(s: int, c: int, hamsters: list[list[int, int]], return_hmsters: bool = True) -> int:
    def can_feed(total_hamsters: int) -> bool:
        total_food = 0
        print("--", total_hamsters, hamsters[:total_hamsters:])
        for hamster in hamsters[:total_hamsters:]:
            total_food += hamster[0] + hamster[1] * (total_hamsters - 1)
            print(total_food, end=" -- ")
            if total_food > s:
                return False
        return True

    radix_sort(hamsters)  # O(dn)

    # left, right = 0, c
    # total_hamsters = 0
    # while left <= right:  # O(log(n))
    #     print()
    #     mid = (left + right) // 2
    #     if can_feed(mid):  # O(n)
    #         total_hamsters = mid
    #         left = mid + 1
    #     else:
    #         right = mid - 1

    # return total_hamsters
    total_food = 0
    print(hamsters[:c:])
    for hamster in hamsters[:c:]:
        total_food += hamster[0] + hamster[1] * (c - 1)
    return total_food
        
    

if __name__ == "__main__":
    hamsters = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
    ]
    s = 33
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
