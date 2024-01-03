from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1
        for i in range(0, len(nums2)):
            nums.append(nums2[i])
            
        nums = sorted(nums)
        print(nums)
        
        if len(nums) % 2 == 0:
            print((nums[int((len(nums) / 2) - 1)] + nums[int((len(nums) / 2))]) / 2)
            return (nums[int((len(nums) / 2) - 1)] + nums[int((len(nums) / 2))]) / 2
        else:
            print(nums[int((len(nums) / 2))])
            return nums[int((len(nums) / 2))]
    
def main():
    s = Solution()
    
    inputs = [
        [[1,3], [2]],
        [[1,2], [3,4]],
        [],
        
    ]
    
    outputs = [
        2.00000,
        2.50000,
        0,
    ]
    
    for i in range(0, len(inputs)):
        if inputs[i] != []:
            nums1, nums2 = inputs[i]
        
        assert(s.findMedianSortedArrays(nums1, nums2) == outputs[i])
        
if __name__ == "__main__":
    main()