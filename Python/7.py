class Solution:
    def reverse(self, x: int) -> int:
        stringx = str(x)
        stringx = stringx[::-1]
        print(stringx)
        
        if "-" in stringx:
            stringx = stringx.replace("-", "")
            stringx = "-" + stringx
            
        print(stringx)
        
        num = int(stringx)
        print(f"Final: {num}")
        
        # This is incase you want the number to stay within a 32 bit boundary
        # if num < -2147483648:
        #     num += 2147483647
        # elif num > 2147483647:
        #     num += -2147483648
        
        if num < -2147483648 or num > 2147483647:
            num = 0
        return num
        
def main():
    inputs = [
        123,
        -123,
        120,
    ]
    
    outputs = [
        321,
        -321,
        21,
    ]
    
    s = Solution()
    
    for i in range(0, len(inputs)):
        assert(s.reverse(inputs[i]) == outputs[i])
        
if __name__ == "__main__":
    main()