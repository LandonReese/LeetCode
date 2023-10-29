from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        """Takes a list of numbers, and returns the average of all even nums divisible by 3

        Args:
            nums (List[int]): A list of integers between 1 and 1000

        Returns:
            int: The average of all evens that are divisible by 3 (Rounded down if necessary)
        """
        divisible_nums = []
        
        for num in nums:
            if num % 6 == 0:
                divisible_nums.append(num)
                
        sum = 0
        for num in divisible_nums:
            sum += num
        
        if nums == [] or sum == 0:
            return 0
        
        sum = sum / len(divisible_nums)
        
        return int(sum)
        
def main():
    solution = Solution()
    test_variable = [1, 2, 3, 4, 5, 7, 12, 18, 24, 36, 37, 92, 93, 94, 95, 96, 97, 98]
    answer = solution.averageValue(test_variable)
    print(answer)
    

if __name__ == "__main__":
    main()