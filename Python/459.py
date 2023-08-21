class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        string_length = len(s)
        string_subset = ""
        i = 0
        while(i < string_length/2):
            # Reset final string
            final_string = ""
            #print()
            
            # Add one letter (index of i) at a time to string_subset
            string_subset += s[i]
            #print(string_subset)
            #print("start", i)
            
            # Duplicate subset until length matches final
            while(len(final_string) < string_length):
                final_string += string_subset
            
            # if repeated string equals original string, return true
            if final_string == s:
                #print("Repeated String", final_string)
                return True
            
            i+=1
            #print("end  ", i)
        
        return False
    
solution = Solution()
test_String = "abab"
print("Final Solution", solution.repeatedSubstringPattern(test_String))