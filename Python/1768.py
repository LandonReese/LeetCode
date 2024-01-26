class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        print(word1, word2)
        
        finalstr = ""

        for i in range(0, len(word1)):
            finalstr += word1[i]
            if word2 != "":
                finalstr += word2[0]
                word2 = word2[1::]
                print(word2)
                
        if word2 != "":
            finalstr += word2
        
        return finalstr
    
def main():
    inputs = [
        ["abc","pqr"],
        ["ab","pqrs"],
        ["abcd","pq"],
    ]

    outputs = [
        "apbqcr",
        "apbqrs",
        "apbqcd",
    ]

    s = Solution()

    for i in range(0, len(inputs)):
        word1, word2 = inputs[i]
        assert(s.mergeAlternately(word1, word2) == outputs[i])

if __name__ == "__main__":
    main()