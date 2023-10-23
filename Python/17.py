from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Creates a list of possible letter combinations from an input of digits

        Args:
            digits - String of digits

        Returns:
            return_list - A list of all possible letter combinations created from each 'digit'
        """
        if digits == "":
            return []
        print(digits)
        digits = sorted(digits)
        print(digits)
        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        letter_combinations = []
        
        def recurse(combination, remaining_digits):
            # If the word has been completely cycled through
            if len(remaining_digits) == 0:
                letter_combinations.append(combination)
            # else, create the combination
            else:

                for letter in letter_map[remaining_digits[0]]:
                    recurse(combination + letter, remaining_digits[1:])

        if digits:
            recurse('', digits)
        
        return letter_combinations
    
def Main():
    s = Solution()
    # Digits can be 0-4 numbers long
    test_variable = "264" # This is the 'digits' input
    answer = s.letterCombinations(test_variable)
    print(answer)

Main()


# return_list = []

#     letter_map = {
#         #Key: "Value", - letter_map.keys(), letter_map.value()
#         "2": "abc",
#         "3": "def",
#         "4": "ghi",
#         "5": "jkl",
#         "6": "mno",
#         "7": "pqrs",
#         "8": "tuv",
#         "9": "wxyz",
#     }

#     letter_combinations = []
#     for key, value in letter_map.items():
#         if key in digits:
#             letter_combinations.append(value)

#     if len(letter_combinations) == 0:
#         return []
    
#     elif len(letter_combinations) == 1:
#         for word in letter_combinations:
#             for letter in word:
#                 return_list.append(letter)

#     elif len(letter_combinations) == 2:
#         for i in range(0, len(letter_combinations) - 1):
#             for j in range(1, len(letter_combinations)): 
#                 return_list.append(self.append_digits(letter_combinations[i], letter_combinations[j]))

#     elif len(letter_combinations) == 3:
#         for i in range(0, len(letter_combinations) - 2):
#             for j in range(1, len(letter_combinations) - 1): 
#                 for k in range(1, len(letter_combinations)): 
#                     return_list.append(self.append_digits(letter_combinations[i], letter_combinations[j]))


#     elif len(letter_combinations) == 4:
#         for i in range(0, len(letter_combinations) - 1):
#             for j in range(1, len(letter_combinations)): 
#                 return_list.append(self.append_digits(letter_combinations[i], letter_combinations[j]))

#     print(f"LC {letter_combinations} | RL {return_list}")
#     return return_list

# def append_digits(self, word1: str, word2: str) -> List[str]:
#     """
    
#     Args:
#         word1: (String) Combination of all letters from a single digit "abc"
#         word2: (String) Combination of letters, but from another digit
#     Returns:
#         return_list: (List of strings) This list contains the combinations of all letters
#                         from two distinct digits
#     """
#     return_list = []
#     for i in range(0, len(word1)):
#         for j in range(0, len(word2)):
#             combination = ""
#             combination += word1[i] + word2[j]
#             return_list.append(combination)

#     return return_list