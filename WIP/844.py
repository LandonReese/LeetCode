class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Args:
            s: String 1, may contain backspace characters
            t: String 2, may contain backspace characters

        Returns:
            True, if s and t are the same after they have been parsed
        """
        print(f"Before: {s} | {t}")
        s = self.string_parse(s)
        t = self.string_parse(t)
        print(f"After:  {s} | {t}")
        if s == t:
            return True
        return False
    
    def string_parse(self, s: str) -> str:
        """
        Args:
            s: String to remove backspaces '#' from

        Returns:
            String that has been reformatted without backpace chars
        """
        total_backspaces = 0
        backspace = '#'
        backspace_visualiser = []
        for letter in s:
            if letter == backspace:
                total_backspaces += 1
            else:
                total_backspaces = 0
            backspace_visualiser.append(total_backspaces)
        
        print(f"BV1: {backspace_visualiser}")

        for i in range(0, len(backspace_visualiser) - 1):
            if backspace_visualiser[i] != 0 and backspace_visualiser[i + 1] > backspace_visualiser[i]:
                backspace_visualiser[i] = -1

        print(f"BV2:  {backspace_visualiser}")

        # Purge -1 from all parts
        while -1 in backspace_visualiser:
            backspace_visualiser.remove(-1)
        print(f"BV3:  {backspace_visualiser}")

        # Correct the deletion count
        total_backspaces = 0
        for i in range(0, len(backspace_visualiser)):
            if backspace_visualiser[i] == 0:

        return s

def Main():
    s = Solution()
    test_variable_1 = "abc##########################c#asdasd"
    test_variable_2 = "ad#c"
    answer = s.backspaceCompare(test_variable_1, test_variable_2)
    print(answer)

Main()

# First Attempt
# def backspaceCompare(self, s: str, t: str) -> bool:
#     """
#     Args:
#         s: String 1, may contain backspace characters
#         t: String 2, may contain backspace characters

#     Returns:
#         True, if s and t are the same after they have been parsed
#     """
#     print(f"Before: {s} | {t}")
#     s = self.string_parse(s)
#     t = self.string_parse(t)
#     print(f"After:  {s} | {t}")
#     if s == t:
#         return True
#     return False

# def string_parse(self, s: str) -> str:
#     """
#     Args:
#         s: String to remove backspaces '#' from

#     Returns:
#         String that has been reformatted without backpace chars
#     """
#     backspaces = 0
#     s_list = list(s)
    
#     # Delete initial backspaces because they're irrelevant
#     while s_list[0] == '#':
#         s_list = s_list[1::]
    
#     # Count the amount of backspace characters
#     for i in range(1, len(s_list)):
#         if s_list[i] == '#':
#             # s_list[i-1] = '#'
#             backspaces += 1

#     print(backspaces)
#     # s = s.replace('#', '')
#     s = ''.join(s_list)
    
#     return s