# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, arr: List[int]) -> int:
        arr.sort() 
        n = len(arr) 
        targetSum = sum(arr) // (n / 2) 
        left, right = 0, n - 1 
        answer = 0 
        counter = 0 

        while left < right: 
            currrentSum = arr[left] + arr[right] 
            
            if currrentSum == targetSum: 
                answer += arr[left] * arr[right] 
                left += 1 
                right -= 1 
                counter += 1 
            elif currrentSum < targetSum: 
                left += 1 
            else: 
                right -= 1 
        if counter == n / 2: 
            return answer 
        else: 
            return -1
        