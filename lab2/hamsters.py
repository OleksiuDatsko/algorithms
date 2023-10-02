def get_hamsters_pacets_of_food(
    hamsters: list[list[int, int]], hamsters_neighborhoods: int
) -> list[int]:
    total_hamsters_feed = []
    for hamster in hamsters:
        total_hamsters_feed.append(hamster[0] + hamster[1] * hamsters_neighborhoods)
    return total_hamsters_feed


def sort_humsters_total_food(hamsters: list[int]) -> list[int]:
    hamsters.sort()
    return hamsters

def get_number_of_hamsters(s: int, c: int, hamsters: list[list[int, int]]) -> int:
    total_hamsters = c
    count = 0
    for total_hamsters in range(c, 0, -1):
        count += 1
        hamsters_pacets = sort_humsters_total_food(
            get_hamsters_pacets_of_food(hamsters, total_hamsters - 1)
        )
        total_pacets = 0
        count_avalible_hamsters = 0
        for hamster in range(total_hamsters):
            if total_pacets + hamsters_pacets[hamster] > s:
                break
            total_pacets += hamsters_pacets[hamster]
            count_avalible_hamsters += 1
                   
        if count_avalible_hamsters == total_hamsters:
            return total_hamsters
        if count >= 100:
            return 0
    return 0
            


if __name__ == "__main__":
    hamsters = [
          [1, 50000],
          [1, 60000],
      ]
    s = 2
    c = 2
    x = get_number_of_hamsters(
          hamsters = hamsters,
          s = s,
          c = c,
      )
    print(x)
