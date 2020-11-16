class Solution:
     def romanToInt(self, s: str) -> int:
        if len(s) < 1 or len(s) > 15:
            return None
        
        romanAlphabet = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        return 0

print(Solution().romanToInt("1234567891234567"))