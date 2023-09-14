# Helpful imports
# List
from typing import List  # Import the List type hint

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """return true if ransomNote can be constructed 
        by using the letters from magazine and false otherwise"""
        rn = ransomNote
        m = magazine
        letters_in_ransomNote = 0
        letter_string = ""
        # Check if letters exist in ransomNote, replace letters as they are used
        for i in range(0, len(rn)):
            
            # J traverses magazine to see all letters
            for j in range(0, len(m)):
                if rn[i] == m[j]:
                    # print(f"ransomNote[i] == magazine[j]\n{ransomNote[i]} == {magazine[j]}")
                    letter_string += m[j]
                    letters_in_ransomNote += 1
                    
                    print(m[j])
                    break
            
                
        print(f"{rn}")
        print(f"{m}")
          
        print(f"letters_in_ransomNote {letters_in_ransomNote}\nlen(ransomNote) {len(ransomNote)}")
        return True  


def main():
    solution = Solution()
    test_variable_1 = "and" #ransomNote
    test_variable_2 = "landon" #magazine
    solution.canConstruct(test_variable_1, test_variable_2)
    

if __name__ == "__main__":
    main()

