# 快速排序
# 1. 找到一个基准点, 并放到数组正确的位置上(左边的元素都不大于基准点, 右边的元素都不小于基准点)
# 2. 对基准点左右两边分别进行排序
def quick_sort(arr: list) -> None:
    quick_sort1(arr, 0, len(arr) - 1)


def quick_sort1(arr: list, left: int, right: int) -> None:
    # 边界值判断
    if left >= right:
        return
    # 基准点下标
    mid = partition(arr, left, right)
    # 对基准点左边数组排序
    quick_sort1(arr, left, mid - 1)
    # 对基准点右边数组排序
    quick_sort1(arr, mid + 1, right)


def partition(arr: list, left: int, right: int) -> int:
    # 选取第一个元素为基准点
    pivot = arr[left]
    i, j = left + 1, right
    while i <= j:
        if arr[i] > pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        else:
            i += 1
    arr[left], arr[j] = arr[j], arr[left]
    return j

if __name__ == '__main__':
    a = [1, 3, 5, 7, 6, 4, 2]
    quick_sort(a)
    print(a)