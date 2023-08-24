class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        is_isomorphic = False
        letter_list_a = [] # Stores list of characters in s
        letter_list_b = [] # Stores list of characters in t
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        for i in range(0, len(s)):
            letter_list_a.append(ord(s[i]))
            
        for i in range(0, len(t)):
            letter_list_b.append(ord(t[i]))
        
        print(f"Letters in s {letter_list_a}:")
        print(f"Letters in t {letter_list_b}")
        
        return is_isomorphic
        
def main():
    # solution = Solution()
    # test_alphabet = "abcdefghijklmnopqrstuvwxyz"
    # test_variable_a = "0123456789abcdABCD"
    # test_variable_b = "banana"
    # solution.isIsomorphic(test_variable_a, test_variable_b)
    print(ord('a')-97)
    
if __name__ == "__main__":
    main()


characters_in_s[26] = [0,0,0,0,0,0,0,0,0,0]
s = "tablet"
characters_in_s[ord(s[i])-97] += 1
characters_in_s[] = [0,0,1,2,0,0,5]
characters_in_t[26] 


tab
sad

# So the idea is: 
# 1 - We convert two strings given first into fully lowercase(to account for capital letters incase we encounter it). 
# Example of what it looks like - s[i] = lower(s[i])
# 2 - We create a function to go through a string and create a two dimensional map of letters in that string
# 3 - We run both strings through that function to get a list of lists (now referring as lols) for the letters and position of those letters in that string
# Example of what it looks like - s = "abbdeb" -> s = [[0], [1,2,5], [], [3], [4], [], [], ..., []]
# 4 - We can sort the two lols in ascending order of lists and compare the two lols to see if they are the same
# Example of what it looks like - s = [[0], [1,2,5], [], [3], [4], [], [], ..., []] -> s = [[], [], [], ..., [], [], [0], [3], [4], [1,2,5]] (we can remove empty lists from a list too, there is a small code in python or a function that does that as I recall, to make it more easy to compare, not that it matters when it comes to comparison as long as both lols are sorted)
# 5 - Ez dub

# characters_in_s[26][] = [[]*26]
# characters

# map [   [T,[0,2]],
#         [I,[1]],
#         [L,[3]],
#         [E,[4]]     ]

# map [   [P,[0,2]],
#         [A,[1]],
#         [E,[3]],
#         [R,[4]]     ]