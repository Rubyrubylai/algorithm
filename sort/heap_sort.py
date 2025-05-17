def heapify(arr, n, i):
  largest = i        # 假設當前節點是最大值
  left = 2 * i + 1   # 左子節點索引
  right = 2 * i + 2  # 右子節點索引

  # 比較左子節點
  if left < n and arr[left] > arr[largest]:
    largest = left

  # 比較右子節點
  if right < n and arr[right] > arr[largest]:
    largest = right

  # 如果最大值不是 root，就交換，並遞迴 heapify
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)


def heap_sort(arr):
  n = len(arr)

  # 建立最大堆（Max-Heap）
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

  # 一個個從堆中取出最大元素，放到陣列尾端
  for i in range(n - 1, 0, -1):
    # 將目前最大值（根節點）放到最後
    arr[i], arr[0] = arr[0], arr[i]
    # 重新對剩下的堆做 heapify
    heapify(arr, i, 0)

  return arr
