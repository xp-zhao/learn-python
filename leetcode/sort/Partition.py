def partition_for(arr: list, left: int, right: int) -> int:
    pivot = arr[right]
    i = left
    for j in range(i, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def partition_while(arr: list, left: int, right: int) -> int:
    pivot = arr[right]
    while left < right:
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
    arr[right] = pivot
    return right


if __name__ == '__main__':
    data_1 = [4, 2, 5, 12, 3]
    print(partition_for(data_1, 0, len(data_1) - 1))
    print(data_1)
    data_2 = [4, 2, 5, 12, 3]
    print(partition_while(data_2, 0, len(data_2) - 1))
    print(data_2)
