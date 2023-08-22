class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Data Types
        reversed_number_list = []

        # If number is negative, return false because it can't be a palindrome
        if(x < 0):
            return False
        
        while x:
            reversed_number_list.append(x%10)
            x = int(x/10)

        print(f"Final {reversed_number_list}")

        reversed_reversed_number_list = reversed_number_list[::-1]

        if reversed_reversed_number_list == reversed_number_list:
            return True

        


solution = Solution()
test_int = 5678
solution.isPalindrome(test_int)
        
