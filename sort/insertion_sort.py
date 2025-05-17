# 從「未排序過的數字」中讀取一個數，把這個讀取的數往前插入到正確位置（依照排序）

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    # 將比 key 大的元素往後移動一格
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    # 插入 key 到正確位置
    arr[j + 1] = key

  return arr
