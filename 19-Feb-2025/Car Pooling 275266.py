# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        length_of_trip = [0] * 1001  
        
        for num_passengers, start, end in trips:
            length_of_trip[start] += num_passengers  
            length_of_trip[end] -= num_passengers    
        
        for passenger in length_of_trip:
            capacity -= passenger 
            if capacity < 0: 
                return False
        
        return True  
        