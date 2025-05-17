# 從「未排序好的數字」中找到最小值，把最小值丟到「未排序好的數字」的最左邊

def selection_sort(arr):
  n = len(arr)

  for i in range(n):
    # 假設當前的 i 是最小值索引
    min_index = i
    # 找出 i 之後最小值的索引
    for j in range(i + 1, n):
      if arr[j] < arr[min_index]:
        min_index = j

    # 如果找到了更小的，就交換
    if min_index != i:
      arr[i], arr[min_index] = arr[min_index], arr[i]

  return arr
