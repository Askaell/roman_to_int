from roman_to_int import Solution

class TestCases():
    def test_case1(self):
        s='III'
        expected = 3

        result = Solution().romanToInt(s)

        assert expected == result, f"Had: {s} ; Expected: {expected} ; Result: {result}"

    def test_case2(self):
        s='IV'
        expected = 4
        
        result = Solution().romanToInt(s)

        assert expected == result, f"Had: {s} ; Expected value: {expected} ; Result value: {result}"

    def test_case3(self):
        s='IX'
        expected = 9
        
        result = Solution().romanToInt(s)

        assert expected == result, f"Had: {s} ; Expected value: {expected} ; Result value: {result}"

    def test_case4(self):
        s='LVIII'
        expected = 58
        
        result = Solution().romanToInt(s)

        assert expected == result, f"Had: {s} ; Expected value: {expected} ; Result value: {result}"

    def test_case5(self):
        s='MCMXCIV'
        expected = 1994
        
        result = Solution().romanToInt(s)

        assert expected == result, f"Had: {s} ; Expected value: {expected} ; Result value: {result}"

    def test_case6(self):
        s=''
        expected = None
        
        result = Solution().romanToInt(s)

        assert expected == result, f"Had: {s} ; Expected value: {expected} ; Result value: {result}"
    
    def test_case7(self):
        s='I'
        expected = 1
        
        result = Solution().romanToInt(s)

        assert expected == result, f"Had: {s} ; Expected value: {expected} ; Result value: {result}"
    
    def test_case8(self):
        s='MMMDCCCCXCIX'
        expected = 3999
        
        result = Solution().romanToInt(s)

        assert expected == result, f"Had: {s} ; Expected value: {expected} ; Result value: {result}"