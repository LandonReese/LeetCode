class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_of_last_word = 0
        print(s)
        test_string = s.split()
        print(test_string)
        len_of_last_word = len(test_string[len(test_string) - 1])
        return len_of_last_word

def main():
    solution = Solution()
    
    test_variable = "hello  hello   hi hi     how   what      "
    solution.lengthOfLastWord(test_variable)

if __name__ == "__main__":
    main()