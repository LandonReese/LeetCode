from typing import List  # Import the List type hint

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        print(f"OG Digits | {digits}")
        digits = digits[::-1]
        print(f"reversed | {digits}")

        digits[0] += 1

        if len(digits) == 1 and digits[0] == 10:
            return [1, 0]
        # If digits end in 9, increment and update next number
        if digits[0] == 10:
            digits[0] = 0
            for i in range(1, len(digits)):
                if(digits[i] == 9):
                    digits[i] = 0
                    if i == len(digits) - 1:
                        digits.append(1)


                else:
                    digits[i] += 1
                    break


        
        digits = digits[::-1]
        print(f"normal    | {digits}")
        return digits

def main():
    solution = Solution()
    test_variable = [9]
    solution.plusOne(test_variable)

if __name__ == "__main__":
    main()