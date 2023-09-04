class Solution:
    def isHappy(self, n: int) -> bool:
        count = 1
        times = 20
        while n != 0 and count < times:
            n = self.breakAndMultiply(n)
            count += 1
        
        if n == 0 or n == 1:
            return True
        return False
    
    def breakAndMultiply(self, n: int) -> int:
        nums = []
        while n > 0:
            if n%10 != 0:
                nums.append(n%10)
            
            n //= 10
            
        print(f"final n%10 {n%10}")
        if n!= 0:
            nums.append(n%10)
            
        nums = nums[::-1]
        print(f"nums | {nums}")
        
        sum = 0
        for i in range(0, len(nums)):
            nums[i] = pow(nums[i], 2)
            sum += nums[i]
        
        print(f"\nnums | {nums}")
        print(f"sum  | {sum}")
        return sum

def main():
    solution = Solution()
    test_variable = 101
    print(solution.isHappy(test_variable))

if __name__ == "__main__":
    main()