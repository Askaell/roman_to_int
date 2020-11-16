import roman_to_int as rToI

class TestCases():
    def test_case1(self):
        s='III'
        expected = 3

        result = rToI.Solution().romanToInt(s)

        assert result == expected, f"Had: {s} ; Expected: {expected} ; Result: {result}"

    # def test_case2(self):
    #     s='IV'
    #     expected = 4
        
    #     result = rToI.Solution().romanToInt(s)

    #     assert result == expected, f"Had: {s} ; Expected value: {expected} ; Result value: {result}"

    # def test_case3(self):
    #     s='IX'
    #     expected = 9
        
    #     result = rToI.Solution().romanToInt(s)

    #     assert result == expected, f"Had: {s} ; Expected value: {expected} ; Result value: {result}"

    # def test_case4(self):
    #     s='LVIII'
    #     expected = 58
        
    #     result = rToI.Solution().romanToInt(s)

    #     assert result == expected, f"Had: {s} ; Expected value: {expected} ; Result value: {result}"

    # def test_case5(self):
    #     s='MCMXCIV'
    #     expected = 1994
        
    #     result = rToI.Solution().romanToInt(s)

    #     assert result == expected, f"Had: {s} ; Expected value: {expected} ; Result value: {result}"