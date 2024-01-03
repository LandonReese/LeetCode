class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        def alphaIndex(string: str) -> int:
            for i in range(0, len(alphabet)):
                if string == alphabet[i]:
                    return i
        
        def alphaLetter(index: int) -> str:
            return alphabet[index]
        
        longest = 0

        for letter in s:
            print(f"{letter} {alphaIndex(letter)}")
            substring = letter
            index = alphaIndex(letter)
            
            while substring in alphabet:
                index += 1
                substring+= alphaLetter(index)
                print(substring)
        
        return longest
                

def main():
    solution = Solution()
    inputs = ["abcdefghijklmnopq"]
    
    outputs = [0]
    
    for i in range(0, len(inputs)):
        assert(solution.lengthOfLongestSubstring(inputs[i]) == outputs[i])

if __name__ == "__main__":
    main()