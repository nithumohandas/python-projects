class HashTable:
    def __init__(self, size: int = 7):
        self.data_map = [None] * size
        self.size = size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)* 23) % self.size
        return my_hash

    def print_ht(self):
        for i, val in enumerate(self.data_map):
            print(f"{i} : {val}")

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                return self.data_map[index][i][1]

my_ht = HashTable(7)
my_ht.print_ht()
my_ht.set_item("bolts", 140)
my_ht.set_item("washers", 70)
my_ht.set_item("lumbar", 18)
my_ht.print_ht()
print(my_ht.get_item("lumbar"))