# 最小堆疊、完全二元樹

class Heap:
  def __init__(self):
    self.nodes = []

  # 插入到最後，再上浮
  def push(self, data):
    self.nodes.append(data)
    index = len(self.nodes) - 1
    self._shift_up(index)

  # 跟最後一個節點交換，再下沉
  def pop(self):
    if not self.nodes:
      return None

    return self._remove_index(0)

  def remove(self, data):
    if not self.nodes:
      return None

    if data not in self.nodes:
      return None

    index = self.nodes.index(data)
    return self._remove_index(index)

  def _shift_up(self, index):
    while index > 0:
      parent_index = (index - 1) // 2
      if self.nodes[parent_index] <= self.nodes[index]:
        break
      self.nodes[index], self.nodes[parent_index] = self.nodes[parent_index], self.nodes[index]
      index = parent_index

  def _shift_down(self, index):
    size = len(self.nodes)
    cur_index = index
    while cur_index < size:
      left_index = 2 * cur_index + 1
      right_index = 2 * cur_index + 2

      smallest_index = index
      if self.nodes[left_index] < smallest_index:
        smallest_index = self.nodes[left_index]
      if self.nodes[right_index] < smallest_index:
        smallest_index = self.nodes[right_index]
      if smallest_index == index:
        break

      self.nodes[cur_index], self.nodes[smallest_index] = self.nodes[smallest_index],  self.nodes[cur_index]
      cur_index = smallest_index

  def _remove_index(self, index):
    value = self.nodes[index]
    last_index = len(self.nodes) - 1
    self.nodes[index] = self.nodes[last_index]
    del self.nodes[last_index]

    parent_index = (index - 1) // 2
    if index > 0 and self.nodes[index] < self.nodes[parent_index]:  # 比父節點小，就上浮
      self._shift_up(index)
    else:
      self._shift_down(index)

    return value


if __name__ == '__main__':
  # heap = Heap()
  # heap.push(4)
  # heap.push(1)
  # heap.push(2)
  # heap.push(5)
  # heap.push(6)
  # print(heap.nodes)

  # heap.pop()
  # print(heap.nodes)

  # heap.remove(4)
  # print(heap.nodes)

  # h = Heap()
  # for x in [1, 4, 2, 5, 6, 3]:
  #   h.push(x)

  # print("初始堆:", h.nodes)   # 期待: [1, 4, 2, 5, 6, 3]

  # h.remove(5)  # 移除索引 3 的元素，最後一個元素 3 會被搬到索引 3
  # print("移除 5 之後:", h.nodes)

  h = Heap()
  h.push(42)
  print(h.pop())
