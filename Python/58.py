class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_of_last_word = 0
        word_list = []
        filtered_word_list = []
        temp_string = ""
        for i in range(0, len(s)):
            # print(f"i | {i} | s[i] | {s[i]}")

            if(s[i] == " "):
                word_list.append(temp_string)
                temp_string = ""

            else:
                temp_string += s[i]
                # print(f"temp_string {temp_string}")

        if(temp_string != ""):
            word_list.append(temp_string)
        print(f"Before filter {word_list}")
        print(len(word_list))
        
        for i in range(0, len(word_list)):
            if word_list[i] != "":
                filtered_word_list.append(word_list[i])
        
        
        print(f"After filter {filtered_word_list}")
        print(len(filtered_word_list))
        
        len_of_last_word = len(filtered_word_list[len(filtered_word_list) - 1])
        print(f"Length of last word | {len_of_last_word}")
        return len_of_last_word

def main():
    solution = Solution()
    test_variable = "hello hello hi hi howareyou         "
    solution.lengthOfLastWord(test_variable)

if __name__ == "__main__":
    main()