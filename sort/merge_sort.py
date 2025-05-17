# 拆分
# 把大陣列切一半成為兩個小陣列
# 把切好的兩個小陣列再各自切一半
# 重複步驟二直到每個小陣列都只剩一個元素

def merge_sort(arr):
  # 當一個陣列只有 0 或 1 的元素的時候，它必定已經是排好序的
  if len(arr) <= 1:
    return arr

  # 將陣列分成左右兩半
  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  # 合併左右兩邊排序後的結果
  return merge(left, right)


# 合併
# 排序兩個只剩一個元素的小陣列並合併
# 把兩邊排序好的小陣列合併並排序成一個陣列
# 重複步驟二直到所有小陣列都合併成一個大陣列

def merge(left, right):
  result = []
  i = j = 0

  # 將左右兩個已排序陣列合併為一個
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  # 加入剩下的元素（如果有的話）
  result.extend(left[i:])
  result.extend(right[j:])
  return result
