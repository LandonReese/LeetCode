class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If number is negative, return false because it can't be a palindrome
        if(x < 0):
            return False

        # Cast int to String
        string_number = str(x)

        # Reversed String
        reversed_string_number = string_number[::-1]

        # Print debugging
        print(f"String {string_number}")
        print(f"reversed {reversed_string_number}")

        # If reversed is equal to original, return True
        if string_number == reversed_string_number:
            return True
        
        return False

solution = Solution()
test_int = -9
print(f"Answer {solution.isPalindrome(test_int)}")