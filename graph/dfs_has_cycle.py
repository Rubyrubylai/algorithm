def has_cycle(graph):
  visited = set()
  path = set()

  def dfs(node):
    if node in path:
      # 回到目前的遞迴路徑上 => cycle
      return True
    if node in visited:
      # 已經完整搜尋過，不會形成 cycle
      return False

    visited.add(node)
    path.add(node)

    for neighbor in graph.get(node, []):
      if dfs(neighbor):
        return True

    path.remove(node)  # 結束這條路徑的遞迴
    return False

  for node in graph:
    if dfs(node):
      return True

  return False
