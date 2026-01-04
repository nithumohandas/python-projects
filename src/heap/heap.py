class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child_index(self, index):
        return 2*index + 1

    def _right_child_index(self, index):
        return 2*index + 2

    def _parent_index(self, index):
        return (index-1)//2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        value_index = len(self.heap) - 1

        while True:
            parent_index = self._parent_index(value_index)
            if value_index == 0 or self.heap[value_index] < self.heap[parent_index]:
                break
            self._swap(value_index, parent_index)
            value_index = parent_index

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child_index(index)
            right_index = self._right_child_index(index)

            if (left_index < len(self.heap) and
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value


my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(80)
my_heap.insert(70)
my_heap.insert(67)

print(my_heap.heap)

my_heap.insert(100)

print(my_heap.heap)

my_heap.insert(75)

print(my_heap.heap)