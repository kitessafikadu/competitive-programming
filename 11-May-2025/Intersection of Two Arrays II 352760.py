# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1=Counter(nums1)
        res=[]
        for num in nums2:
            if count1[num]>0:
                res.append(num)
                count1[num]-=1
        return res