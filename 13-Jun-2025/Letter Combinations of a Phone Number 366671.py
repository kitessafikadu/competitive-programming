# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        combinations = [""]
        for digit in digits:
            new_comb = []
            for combo in combinations:
                for letter in d[digit]:
                    new_comb.append(combo+letter)
            combinations = new_comb
        return combinations