# 归并排序
# 1. 将原数组分割成两个子数组
# 2. 对子数组执行相同的算法进行排序(递归)
# 3. 将排好序的子数组合并成一个


# 方法一: 开辟新的空间存储子数组
def merge_sort(arr: list) -> None:
    # 边界值判断
    if len(arr) <= 1:
        return
    # 分割子数组
    mid = len(arr) // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    # 对子数组进行排序
    merge_sort(arr1)
    merge_sort(arr2)
    # 合并排好序的子数组
    merge(arr1, arr2, arr)


def merge(arr1: list, arr2: list, arr: list) -> None:
    # 子数组下标
    i, j = 0, 0
    for idx in range(0, len(arr)):
        if i == len(arr1):
            arr[idx] = arr2[j]
            j += 1
        elif j == len(arr2):
            arr[idx] = arr1[i]
            i += 1
        elif arr1[i] <= arr2[j]:
            arr[idx] = arr1[i]
            i += 1
        else:
            arr[idx] = arr2[j]
            j += 1


# 方法二: 不单开开辟空间存储子数组, 使用变量存储子数组下标
def merge_sort0(arr: list):
    merge_sort1(arr, 0, len(arr) - 1)


def merge_sort1(arr: list, left: int, right: int) -> None:
    # 边界值判断
    if left >= right:
        return
    # 分割子数组
    mid = (left + right) // 2
    # 对子数组进行排序
    merge_sort1(arr, 0, mid)
    merge_sort1(arr, mid + 1, right)
    # 合并排好序的子数组
    merge1(arr, left, mid, right)


def merge1(arr: list, left: int, mid: int, right: int) -> None:
    # 备份原数组
    temp = [e for e in arr]
    # 子数组下标
    i, j = left, mid + 1
    for idx in range(left, right + 1):
        if i == mid + 1:
            arr[idx] = temp[j]
            j += 1
        elif j == right + 1:
            arr[idx] = temp[i]
            i += 1
        elif arr[i] <= arr[j]:
            arr[idx] = temp[i]
            i += 1
        else:
            arr[idx] = temp[j]
            j += 1


if __name__ == '__main__':
    a = [1, 3, 5, 7, 6, 4, 2]
    merge_sort0(a)
    print(a)
