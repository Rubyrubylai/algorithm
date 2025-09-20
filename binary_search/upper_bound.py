# 第一個 > key
def upper_bound(a, key):
  l, r = 0, len(a) - 1
  ans = len(a)
  while l <= r:
    m = (l + r) // 2
    if a[m] > key:         # 已經嚴格大於：記錄，往左縮
      ans = m
      r = m - 1
    else:                  # a[m] <= key：還不夠，往右找
      l = m + 1
  return ans
