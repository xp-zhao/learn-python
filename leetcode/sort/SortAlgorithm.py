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


if __name__ == '__main__':
    data_list = [2, 1, 5, 4, 3, 6]
    # bubble_sort(data_list)
    # insertion_sort(data_list)
    selection_sort(data_list)
    print(data_list)
