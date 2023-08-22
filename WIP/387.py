class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Data Types
        current_char = ""
        current_index = 0
        
        
        # if string length is too short, return index
        if(len(s) <= 1):
            print("s is", len(s), s)
            return 0
        
        # if character, check all for repeating
        while(current_index < len(s)):
            # Set current character
            current_char = s[current_index]
            
            
            # Check for duplicates from the next letter, to the end of the string
            for i in range(current_index + 1, len(s)):
                
                # if there is a duplicate, increment current_index
                if(s[i] == current_char):
                    current_index += 1
                    
                else:
                    return current_index
                
        
        
solution = Solution()
test_string = "aabbcdefg"
print("Answer", solution.firstUniqChar(test_string))