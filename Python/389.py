class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = {}
        return_string = ""

        # Add all letters to the dictionary
        for letter in s:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] = letters[letter] + 1
        print(f"1: {letters}")  

        for letter in t:
            if letter not in letters:
                return_string += letter
            elif letter in letters and letters[letter] == 0:
                return_string += letter
            else:
                letters[letter] = letters[letter] - 1
        print(f"2: {letters}")  

        for letter in letters:
            if letters[letter] != 0:
                return_string += letter
                letters[letter] = letters[letter] - 1
        print(f"3: {letters}")      
        
        print(s)
        print(letters)        
        return return_string
    
def Main():
    s = Solution()
    test_variable_s = "abcddd"
    test_variable_t = "ddddcba"
    difference = s.findTheDifference(test_variable_s, test_variable_t)
    print(f"Difference: {difference}")

Main()