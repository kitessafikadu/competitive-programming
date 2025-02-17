# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        freq = Counter(word)  # Count frequency of each letter
        
        for i in range(len(word)):
            temp_word = word[:i] + word[i+1:]  # Remove one character
            temp_freq = Counter(temp_word)  # Recalculate frequency
            
            # Check if all frequencies are the same
            if len(set(temp_freq.values())) == 1:
                return True
        
        return False
            