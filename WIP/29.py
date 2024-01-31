class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        flag1 = False
        flag2 = False
        

        ret = int(dividend/divisor)

        if dividend < 0:
            dividend = -dividend
            flag1 = True

        if divisor < 0:
            divisor = -divisor
            flag2 = True
        
        num = divisor

        print(dividend, divisor)

        while divisor < dividend:
            print(f"dv: {divisor}\ndd: {dividend}")
            divisor = divisor + num
            count += 1
           
        print(count, ret)
        
        if flag1 and not flag2 or flag2 and not flag1:
            return -count
        return count
            
    
def main():
    inputs = [
        [10,3],
        [7,-3],
        [-2147483648,-1]
    ]

    outputs = [
        3,
        -2,
        
    ]

    s = Solution()

    for i in range(0, len(inputs)):
        dvend, dvisor = inputs[i]
        assert(s.divide(dvend, dvisor) == outputs[i])

if __name__ == "__main__":
    main()