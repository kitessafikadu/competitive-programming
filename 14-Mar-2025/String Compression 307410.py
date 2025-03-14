# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:


        left , right = 0 , 0

        while right < len(chars):

            current_char = chars[right]
            count = 0

            while right < len(chars) and chars[right] == current_char :
                right += 1
                count += 1

            chars[left] = current_char 
            left+=1 

            if count > 1:
                for c in str(count):
                    chars[left] = c
                    left += 1
        return left