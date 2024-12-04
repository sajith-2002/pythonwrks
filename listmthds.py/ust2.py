arr = [100, 200, 300, 400, 500, 600, 700, 800]


odd_index_elements = [arr[i] for i in range(1, len(arr), 2)]  # [200, 400, 600, 800]


odd_index_elements.reverse()  # [800, 600, 400, 200]


for i in range(1, len(arr), 2):
    arr[i] = odd_index_elements.pop(0)


print(arr)
