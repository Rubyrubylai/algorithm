def quick_sort(arr):
  # 當一個陣列只有 0 或 1 的元素的時候，它必定已經是排好序的
  if len(arr) <= 1:
    return arr

  # 選一個基準值（這裡選最右邊一個）
  pivot = arr[-1]
  left = []
  right = []
  equal = []

  # 將元素根據基準值分類
  for x in arr:
    if x < pivot:
      left.append(x)
    elif x > pivot:
      right.append(x)
    else:
      equal.append(x)

  # 遞迴排序左右兩邊，再合併
  return quick_sort(left) + equal + quick_sort(right)
