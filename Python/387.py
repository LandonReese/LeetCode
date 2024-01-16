class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_dict = {}
        for letter in s:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1

        for i in range(0, len(s)):
            if letter_dict[s[i]] == 1:
                return i
        
        return -1
    
def main():
    inputs = [
        "leetcode",
        "loveleetcode",
        "aabb",
    ]
    
    outputs = [
        0,
        2,
        -1,
    ]
    
    s = Solution()
    
    for i in range(0, len(inputs)):
        assert(s.firstUniqChar(inputs[i]) == outputs[i])
        
if __name__ == "__main__":
    main()