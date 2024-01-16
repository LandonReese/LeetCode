class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        
        if "-" in s:
            negative = True
            s = s.replace("-", "")

        while s[0] == " ":
            s = s.replace(" ", "", 1)
            print(s)

        print(s)
        
        string = ""

        for i in range(0, len(s)):
            try:
                if int(s[i]):
                    string += str(s[i])
            except:
                string = "0"
                break

        print(string)

        
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
        assert( s.myAtoi(inputs[i]) == outputs[i])
    
    
    print("hi")

if __name__ == "__main__":
    main()