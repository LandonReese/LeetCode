from typing import List  # Import the List type hint

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        if nums1 in nums2:
            print(f"nums1 in nums2")
        if nums2 in nums1:
            print(f"nums2 in nums1")
        
        return intersection

def main():
    solution = Solution()
    test_variable_1 = [1,2,2,1]
    test_variable_2 = [1]
    result = solution.intersection(test_variable_1, test_variable_2)
    print(f"Result = {result}")

if __name__ == "__main__":
    main()

# If the partitions of one list are in the other list
# or the other list "reversed" (Thus [9, 5] would become [5, 9])
# Then return the partitioned list