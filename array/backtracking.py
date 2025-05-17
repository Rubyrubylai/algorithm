def backtracking(num_str):
  if len(num_str) == len(origin_num):
    nums.add(num_str)
    return

  for j in range(len(origin_num)):
    if used[j]:
      continue

    used[j] = True
    backtracking(num_str + origin_num[j])
    used[j] = False


if __name__ == "__main__":
  origin_num = '123'  # 要進行排列組合的字串
  used = [False] * len(origin_num)
  nums = set()
  backtracking('')
  print(nums)

# Time Complexity: O(n!)
