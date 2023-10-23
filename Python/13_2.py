class Solution:
    def romanToInt(self, s: str) -> int:
        """Takes a string of roman numerals, and converts it into a number

        Args:
            s (str): String containing onyl Roman Numerals

        Returns:
            int: The integer equivalent of the Roman Numeral
        """
        final_value = 0
        roman_dict = {
            # Two digit numbers need to be checked first...
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,

            #... then one digit numbers can be checked
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        
        s = s[::-1]
        
        last_value = 0
    
        for char in s:
            if roman_dict.get(char) < last_value:
                final_value -= roman_dict.get(char)
            else:
                final_value += roman_dict.get(char)
            last_value = roman_dict.get(char)
                

        
        print(final_value)          
        return final_value
           
# I, 1
# V, 5
# X, 10
# L, 50
# C, 100
# D, 500
# M, 1000
        
        
def main():
    solution = Solution()
    test_variable = "MCDXCII"
    result = solution.romanToInt(test_variable)
    print(f"Result {result}")

if __name__ == "__main__":
    main()