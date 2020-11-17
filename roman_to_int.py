class Solution:
     def romanToInt(self, s: str) -> int:
        if (len(s) < 1) or (len(s) > 15):
            return None
        s = s.upper()

        romanAlphabet = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        output = 0
        currentValue = 0
        middleValue = 0
        
        for key in s[::-1]:
            previousValue = currentValue
            currentValue = romanAlphabet[key]

            if previousValue == 0:
                middleValue = currentValue       
            else:
                if previousValue == currentValue:
                    middleValue += currentValue

                elif previousValue > currentValue:
                    output += previousValue - currentValue
                    currentValue = 0
                    middleValue = 0
                
                elif previousValue < currentValue:
                    output += currentValue + middleValue
                    currentValue = 0
                    middleValue = 0
        
        if middleValue != 0:
            output += middleValue

        return output