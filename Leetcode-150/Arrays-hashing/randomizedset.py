import random


class RandomizedSet:

    def __init__(self):
        self.index_to_val = {}
        self.value = []

    def insert(self, val: int) -> bool:
        if val in self.index_to_val:
            return False
        self.index_to_val[val] = len(self.value)
        self.value.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.index_to_val:

            index = self.index_to_val[val]
            last_val = self.value[-1]

            # replace the element to be removed with last ele
            # and update the map
            self.value[index] = last_val
            self.index_to_val[last_val] = index

            # remove the val from the map
            # remove the last ele from the map
            del self.index_to_val[val]
            self.value.pop()

            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.value)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
