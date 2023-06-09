def build_heap(data):
    swaps = []
    n = len(data)
    
    def scan(index):
        min_index = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < n and data[left_index] < data[min_index]:
            min_index = left_index

        if right_index < n and data[right_index] < data[min_index]:
            min_index = right_index

        if index != min_index:
            swaps.append((index, min_index))

            data[index], data[min_index] = data[min_index], data[index]
            scan(min_index)

    for index in range(n // 2, -1, -1):
        scan(index)

    return swaps


def main():
    text = input("choose 'I' for input or 'F' for file")
    if "F" in text:
        file_name = input("Enter file name: ")
        if "a" not in file_name:
            path = './tests/' + file_name
            with open(path, 'r', encoding='utf-8') as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
    elif "I" in text:
        n = int(input())
        data = list(map(int, input().split()))

    assert data is not None and len(data) == n

    swaps = build_heap(data)

    assert len(swaps) <= n*4

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
