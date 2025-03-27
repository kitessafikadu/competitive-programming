# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = defaultdict(int)
        left, max_count = 0, 0

        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1  

            while len(fruit_count) > 2: 
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]  
                left += 1  

            max_count = max(max_count, right - left + 1)  

        return max_count
