class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = s
        s = s.lower()
        print(f"Lowered: {s}")
        
        for i in range(0, len(s)):
            if not s[i].isalnum():
                s = s.replace(s[i],' ')
                
        print(f"Formatted: {s}")
        
        s = s.replace(" ", "")
        print(f"Spaces rem: {s}")
        
        if s == s[::-1]:
            return True
        return False

def main():
    solution = Solution()
    test_variable = "A man, a plan, a canal: Panama"
    test_variable2 = "0,,:,,P"
    print(solution.isPalindrome(test_variable2))

if __name__ == "__main__":
    main()