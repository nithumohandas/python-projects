class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0,0)


    def remove(self, node):
        """
        This is done to remove the node from the doubly linked list
        :param node:
        :return:
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


    def insert(self,node):
        prev_node = self.tail.prev
        prev_node.next = node
        self.tail.prev = node
        node.prev = prev_node
        node.next = self.tail


    def put(self,key, value):
        new_node = self.Node(key, value)
        if key in self.cache_map:
            node = self.cache_map[key]
            self.remove(node)
        self.cache_map[key] = new_node
        self.insert(new_node)

        if len(self.cache_map) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache_map[lru.key]


    def get(self, key):
        if key in self.cache_map:
            self.remove(self.cache_map[key])
            self.insert(self.cache_map[key])
            return self.cache_map[key].value
        return -1