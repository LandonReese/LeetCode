from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        while i:
            if i in nums:
                i += 1
            else:
                print(i)
                return i
        print("end")
        return 1

            
def main():
    solution = Solution()
    test_variable = [2,6,4,3,1]
    solution.firstMissingPositive(test_variable)

if __name__ == "__main__":
    main()