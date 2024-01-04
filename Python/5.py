class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ""
        for i in range(0, len(s)):
            palindrome = ""
            
            for j in range(i, len(s)):
                palindrome += s[j]
                    
                if palindrome == palindrome[::-1] and len(palindrome) > len(substring):
                    substring = palindrome
                    # print("New substring:", substring)

        # print(substring)
        return substring


def main():
    s = Solution()
    
    inputs = [
        "babad",
        "cbbd",
        "",
        
    ]
    
    outputs = [
        "bab",
        "bb",
        "",
    ]

    for i in range(0, len(inputs)):
        print("inputs ", inputs[i])
        answer = s.longestPalindrome(inputs[i])
        assert(answer == outputs[i])
        
if __name__ == "__main__":
    main()