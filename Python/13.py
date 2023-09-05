class Solution:
    def romanToInt(self, s: str) -> int:
        """Takes a string of roman numerals, and converts it into a number

        Args:
            s (str): String containing onyl Roman Numerals

        Returns:
            int: The integer equivalent of the Roman Numeral
        """
        final_value = 0
        roman_dict = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev_val = 0
        curr_val = 0
        
        # IV 4 | VI 6
        for numeral in reversed(s):
            value = roman_dict[numeral]
            
            if value < prev_val:
                final_value -= value
            else:
                final_value += value
            prev_val = value
        
                    
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
    test_variable = "MCMXCIV"
    result = solution.romanToInt(test_variable)
    print(f"Result {result}")

if __name__ == "__main__":
    main()