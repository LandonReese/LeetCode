class Solution:
    def romanToInt(self, s: str) -> int:
        """Takes a string of roman numerals, and converts it into a number

        Args:
            s (str): String containing onyl Roman Numerals

        Returns:
            int: The integer equivalent of the Roman Numeral
        """
        print(f"s | {s}")
        
        
        subset_list = []
        
        if not s:
            print(f"not s")
            return 0
        
        if len(s) == 1:
            print(f"return {self.letterToValue(s)}")
            return self.letterToValue(s)
        
        for i in range(0, len(s)):
            subset_list.append(self.letterToValue(s[i]))
        
        print(f"subset_list {subset_list}")
        sum = 0
        for i in range(1, len(subset_list)): 
            if subset_list[i-1] == subset_list[i]:
                sum += subset_list[i-1]
                print(f"=={sum}")
                
            elif subset_list[i-1] > subset_list[i]:
                sum += subset_list[i - 1]
                print(f">{sum}")
                
            elif subset_list[i-1] < subset_list[i]:
                sum += subset_list[i] - subset_list[i - 1]
                i += 1
                print(f"<{sum}")
                
            if i == len(subset_list) - 1:
                sum += subset_list[i]
                print(f"{i} == {len(subset_list)} - 1 || {sum}")
        
                
        print("Final", sum)
                    

    def letterToValue(self, s: str) -> int:
        value = 0
        if s == "I":
            value = 1
        elif s == "V":
            value = 5
        elif s == "X":
            value = 10
        elif s == "L":
            value = 50
        elif s == "C":
            value = 100
        elif s == "D":
            value = 500
        elif s == "M":
            value = 1000
        return value
           
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
        
        
def main():
    solution = Solution()
    test_variable = "MCMXCIV"
    solution.romanToInt(test_variable)

if __name__ == "__main__":
    main()