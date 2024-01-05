class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        string = ""
        for i in range(0, len(s)):
            try:
                if s[i] == "-":
                    negative = True
                elif int(s[i]):
                    string += str(s[i])
            except:
                print("Not a number")

        
        string = int(string)

        if negative:
            string = string * -1

        print(string)
        return string

def main():
    inputs = [
        "42",
        "   -42",
        "4193 with words",
        "something something 422     -",
    ]
    
    outputs = [
        42,
        -42,
        4193,
        0,
    ]
    
    s = Solution()

    for i in range(0, len(inputs)):
        assert(s.myAtoi(inputs[i]) == outputs[i])
    
    
    print("hi")

if __name__ == "__main__":
    main()