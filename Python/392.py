class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sIndex = 0
        tIndex = 0
        
        finished = False

        if s == "":
            return True

        if len(s) > len(t):
            return False

        while not finished:
            if s[sIndex] == t[tIndex]:
                sIndex += 1
                tIndex += 1
            else:
                tIndex += 1
            if sIndex == len(s):
                return True
            if tIndex >= len(t):
                finished = True
        
        return False
          

def main():
    print(True)
    inputs = [
        ["abc","ahbbgdc"],
        ["axc","ahbgdc"],
        ["abc","abbc"],
        ["","ahbgdc"]
    ]
    
    outputs = [
        True,
        False,
        True,
        True,
    ]
    
    s = Solution()
    
    for i in range(0, len(inputs)):
        string1, string2 = inputs[i]
        print(i)
        assert(s.isSubsequence(string1, string2) == outputs[i])
        
if __name__ == "__main__":
    main()