# 第一個 >= key
def lower_bound(a, key):
  l, r = 0, len(a) - 1
  ans = len(a)               # 預設插到最後
  while l <= r:
    m = (l + r) // 2
    if a[m] >= key:        # 命中或過頭：記錄，往左縮找更早的
      ans = m
      r = m - 1
    else:                  # a[m] < key：還不夠，往右找
      l = m + 1
  return ans                  # 插入點
