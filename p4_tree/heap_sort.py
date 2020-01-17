#-*- coding: UTF-8 -*-


def max_heapify(arr, i, heap_size):
    """维护最大堆。i 表示当期调整第i个堆元素的位置，heap_size表示当前剩余的堆元素个数"""
    end = int((heap_size-1-1) / 2)    # 当前最后一个非叶节点的下标。根节点的下标为0
    while i <= end:
        l = 2*i + 1    # 当前节点的左孩子下标
        r = 2*i + 2    # 当前节点的右孩子下标
        max_index = r if r < heap_size and arr[r] >= arr[l] else l
        if arr[i] >= arr[max_index]:
            break
        else:
            arr[i], arr[max_index] = arr[max_index], arr[i]
            i = max_index


def min_heapify(arr, i, heap_size):
    """维护最小堆。i 表示当期调整第i个堆元素的位置，heap_size表示当前剩余的堆元素个数"""
    end = int((heap_size-1-1) / 2)    # 当前最后一个非叶节点的下标。根节点的下标为0
    while i <= end:
        l = 2*i + 1    # 当前节点的左孩子下标
        r = 2*i + 2    # 当前节点的右孩子下标
        min_index = r if r < heap_size and arr[r] <= arr[l] else l
        if arr[i] <= arr[min_index]:
            break
        else:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            i = min_index


def heap_sort(arr):
    """升序排序使用最大堆；降序排序使用最小堆"""
    if not arr or len(arr) < 1:
        return
    heap_size = len(arr)
    start = int((heap_size-1-1) / 2)    # 当前最后一个非叶节点的下标。根节点的下标为0
    # 初始化最大堆。从最后一个非叶节点开始调整
    for i in range(start, -1, -1):
        # max_heapify(arr, i, heap_size)
        min_heapify(arr, i, heap_size)

    # 循环heap_size-1次，每次选出一个当前最大值
    for i in range(heap_size - 1):
        # 堆顶最大值 与 堆内最后一个元素交换位置
        arr[0], arr[heap_size - 1] = arr[heap_size - 1], arr[0]
        heap_size -= 1
        # 若堆内少于2个元素，则排序结束
        if heap_size < 2:
            break
        # 重新构造最大堆，调整堆顶元素的位置
        # max_heapify(arr, 0, heap_size)
        min_heapify(arr, 0, heap_size)


if __name__ == "__main__":
    arr = [7, 95, 73, 65, 60, 77, 28, 62, 43]
    # arr = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
    print(arr)
    heap_sort(arr)
    print(arr)
