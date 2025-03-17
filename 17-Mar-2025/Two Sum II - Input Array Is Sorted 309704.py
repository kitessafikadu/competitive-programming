# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            current_sum = numbers[i] + numbers[j]

            if current_sum == target:
                return [i + 1, j + 1]
            elif current_sum < target:
                i += 1
            else:
                j -= 1