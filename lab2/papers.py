def get_table_h(n: int, w: int, h: int):
    total = 0
    left, right = 0, w*n if w > h else h*n
    while left < right:  # O(log(n))
        mid = (left + right) // 2
        if (mid//h)*(mid//w) < n:
            left = mid + 1
        else:
            right = mid
        total = mid
    print(total)
    
get_table_h(7, 1, 7)