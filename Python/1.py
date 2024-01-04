from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]




def main():
    s = Solution()
    
    inputs = [
        [[2,7,11,15], 9],
        [[3,2,4], 6],
        [[3,3], 6],
        
        
    ]
    
    outputs = [
        [0,1],
        [1,2],
        [0,1],
    ]
    
    for i in range(0, len(inputs)):
        if inputs[i] != []:
            nums, target = inputs[i]
        
        assert(s.twoSum(nums, target) == outputs[i])
        
if __name__ == "__main__":
    main()