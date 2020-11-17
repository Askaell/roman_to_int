class Solution:
     def romanToInt(self, s: str) -> int:
        if (len(s) < 1) or (len(s) > 15):
            return None
        s = s.upper()

        romanNumbers = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        output = 0
        current = 0
        middle = 0

        for key in s[::-1]:
            previous = current
            current = romanNumbers[key]

            if previous == 0:
                middle = current      
            else:
                if previous == current:
                    middle += current

                elif previous > current:
                    output += previous - current
                    current = 0
                    middle = 0
                
                elif previous < current:
                    output += current + middle
                    current = 0
                    middle = 0
        
        if middle != 0:
            output += middle

        return output