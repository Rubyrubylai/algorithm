class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def __len__(self):
    return self.size

  def enqueue(self, data):
    node = Node(data)
    if not self.head or not self.tail:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = self.tail.next
    self.size += 1

  def dequeue(self):
    if self.size == 0:
      return None

    head = self.head
    if not head:
      return None

    self.head = head.next
    self.size -= 1
    return head.data


if __name__ == '__main__':
  q = Queue()
  q.enqueue(4)
  q.enqueue(3)
  q.enqueue(5)
  q.enqueue(6)

  print(q.dequeue())
  print(q.dequeue())
  print(q.dequeue())
  print(len(q))
