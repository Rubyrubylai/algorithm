# 從沒有被其他節點指向開始，一一移除它們對其他節點的指向

from collections import defaultdict, deque


def topological_sort(num_nodes, edges):
  graph = defaultdict(list)
  in_degree = [0] * num_nodes

  for src, dest in edges:
    graph[src].append(dest)
    in_degree[dest] += 1

  queue = deque()
  for i in range(num_nodes):
    if in_degree[i] == 0:  # 找入度為 0 的節點：這些節點可以安全地放在拓撲排序的前面，因為它們不依賴於其他節點
      queue.append(i)

  result = []

  while queue:
    node = queue.popleft()
    result.append(node)

    for neighbor in graph[node]:
      in_degree[neighbor] -= 1
      if in_degree[neighbor] == 0:
        queue.append(neighbor)

  if len(result) != num_nodes:
    raise ValueError(
        "Graph has at least one cycle; topological sort not possible.")

  return result


if __name__ == "__main__":
  num_nodes = 6
  edges = [
      (5, 2),
      (5, 0),
      (4, 0),
      (4, 1),
      (2, 3),
      (3, 1)
  ]
  print("Topological Sort:", topological_sort(num_nodes, edges))
