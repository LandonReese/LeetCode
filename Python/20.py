import shlex


class Solution:
    def isValid(self, s: str) -> bool:
        removed = True
        while removed:
            print(s)
            removed = False
            if "()" in s:
                s = s.replace("()", "")
                removed = True
            elif "[]" in s:
                s = s.replace("[]", "")
                removed = True
            elif "{}" in s:
                s = s.replace("{}", "")
                removed = True
        if s == "":
            return True
        return False

def Main():
    s = Solution()
    test_variables = ["(){}[]", "", "(}", "({})", "({[})]", "{((([[()]])))}", "[({()})["]
    answers =        [True,     True, False, True, False, True, False]
    for i in range(0, len(test_variables)):
        print(f"{i}: {test_variables[i]} \nAnswer: {s.isValid(test_variables[i])} | Expected: {answers[i]}\n")
        assert answers[i] == s.isValid(test_variables[i])
    # test = "({})"
    # print(s.isValid(test))

if __name__ == Main():
    Main()

# if s == "":
#             return True
        
#         if len(shlex) % 2 != 0:
#             return False
        
#         p_list = []
#         for char in s:
#             p_list.append(char)
#         print(f"{p_list}")

#         removed = True
#         while removed:
#             removed = False
#             print(f"{p_list}")

#             for i in range(0, len(p_list) - 1):
#                 if p_list[i] == '(' and p_list[i+1] == ')':
#                     p_list[i] = ''
#                     p_list[i + 1] = ''
#                     removed = True
#                 elif p_list[i] == '{' and p_list[i+1] == '}':
#                     p_list[i] = ''
#                     p_list[i + 1] = ''
#                     removed = True
#                 elif p_list[i] == '[' and p_list[i+1] == ']':
#                     p_list[i] = ''
#                     p_list[i + 1] = ''
#                     removed = True
            
#             p_list = [char for char in p_list if char != '']

#         if p_list == []:
#             return True
#         return False