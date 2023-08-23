class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_of_last_word = 0
        word_list = []
        temp_string = ""
        for i in range(0, len(s)):
            print(f"i | {i} | s[i] | {s[i]}")

            if(s[i] == " " and temp_string != ""):
                word_list.append(temp_string)
                temp_string = ""

            else:
                temp_string += s[i]
                print(f"temp_string {temp_string}")

        word_list.append(temp_string)
        print(word_list)
        print(len(word_list))

        if(word_list[len(word_list) - 1] != ""):
            len_of_last_word = len()

        return len_of_last_word

def main():
    solution = Solution()
    test_variable = "hello hello hi hi ho"
    solution.lengthOfLastWord(test_variable)

if __name__ == "__main__":
    main()