# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.loc=0

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.loc=0
        else:
            self.loc+=1
        return self.loc>=self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)