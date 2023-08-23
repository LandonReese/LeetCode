from typing import List  # Import the List type hint

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        test_string = ""
        max_word_len = 0

        for i in range(0, len(strs)):
            if len(strs[i]) > max_word_len:
                max_word_len = len(strs[i])

        for i in range(0, len(strs)):
            if len(strs[i]) < max_word_len:
                extra_characters = max_word_len - len(strs[i])
                for j in range(0, extra_characters):
                    strs[i] += "+"

        letter_tracker = []
        non_similar_letters = 0
        for i in range(0, max_word_len):
            letter_tracker = []
            for j in range(0, len(strs)):
                letter_tracker.append(strs[j][i])

            temp_checker = letter_tracker[0]
            for item in letter_tracker:
                if item != temp_checker:
                    non_similar_letters = non_similar_letters + 1
            
            if non_similar_letters == 0:
                test_string += temp_checker

        return test_string

def main():
    solution = Solution()
    test_variable = ["apple", "aardvark", "applause"]
    print(solution.longestCommonPrefix(test_variable))

if __name__ == "__main__":
    main()