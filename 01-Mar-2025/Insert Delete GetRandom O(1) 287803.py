# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}  
        self.values = []       

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False 
        self.values.append(val)  
        self.val_to_index[val] = len(self.values) - 1  
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False  
        last_val = self.values[-1]
        idx = self.val_to_index[val]
        self.values[idx] = last_val
        self.val_to_index[last_val] = idx
        
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()