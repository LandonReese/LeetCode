class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        
        return_numeral = ''
        for key, value in roman_numerals.items():
            while num >= key:
                    num -= key
                    return_numeral += value

        return return_numeral
    
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

def Main():
    s = Solution()
    test_variable = 2999 #"MCMXCIV"
    roman_numeral = s.intToRoman(test_variable)
    print(f"\n{roman_numeral}")
    print("MCMXCIV")

Main()
