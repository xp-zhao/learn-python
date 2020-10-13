def bubble_sort(num_list: list):
    num_len = len(num_list)
    for i in range(num_len):
        swap_flag = False
        for j in range(num_len - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                swap_flag = True
        if not swap_flag:
            break


def insertion_sort(num_list: list):
    num_len = len(num_list)
    for i in range(1, num_len):
        v = num_list[i]
        j = i - 1
        while j >= 0 and v < num_list[j]:
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j + 1] = v


def selection_sort(num_list: list):
    num_len = len(num_list)
    for i in range(num_len):
        min_index = i
        for j in range(i + 1, num_len):
            if num_list[j] < num_list[min_index]:
                min_index = j
        if min_index != i:
            temp = num_list[i]
            num_list[i] = num_list[min_index]
            num_list[min_index] = temp


def merge_sort(num_list: list) -> list:
    if len(num_list) == 1:
        return num_list
    mid_index = int(len(num_list) / 2)
    left = num_list[0:mid_index]
    right = num_list[mid_index:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_list(left, right)


def merge_list(a: list, b: list) -> list:
    merged = []
    ai = bi = 0
    while ai < len(a) and bi < len(b):
        if a[ai] < b[bi]:
            merged.append(a[ai])
            ai += 1
        else:
            merged.append(b[bi])
            bi += 1
    while ai < len(a):
        merged.append(a[ai])
        ai += 1
    while bi < len(b):
        merged.append(b[bi])
        bi += 1
    return merged


def quick_sort(num_list: list, left: int, right: int):
    if left < right:
        pivot = partition(num_list, left, right)
        quick_sort(num_list, left, pivot - 1)
        quick_sort(num_list, pivot + 1, right)


def partition(num_list: list, left: int, right: int) -> int:
    pivot = num_list[left]
    while left < right:
        while left < right and num_list[right] >= pivot:
            right -= 1
        num_list[left] = num_list[right]
        while left < right and num_list[left] <= pivot:
            left += 1
        num_list[right] = num_list[left]
    num_list[left] = pivot
    return left


if __name__ == '__main__':
    data_list = [2, 1, 5, 4, 3, 6]
    # bubble_sort(data_list)
    # insertion_sort(data_list)
    # selection_sort(data_list)
    # print(merge_sort(data_list))
    quick_sort(data_list, 0, len(data_list) - 1)
    print(data_list)
