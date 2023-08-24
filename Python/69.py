# Helpful imports
# List
import math
from typing import List  # Import the List type hint

class Solution:
    def mySqrt(self, x: int) -> int:
        print(f"\nSquare root of {x}")
        i = 1
        number = 0

        if x == 0 or x == 1:
            #print(f"Returning: {x}")
            return x

        while number <= x:
            number = i * i
            #print(f"\n")
            #print(f"Num {number} | i {i}")

            #print(f"{number} > {x}?")
            if number > x:
                print(f"Final return val: | Expected answer:")
                print(f"{i - 1} = {int(math.sqrt(x))}")
                return i - 1
            else:
                #print(f"i+=1")
                i += 1

            
            

            



def main():
    solution = Solution()
    test_variable = [3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(0, len(test_variable)):
        solution.mySqrt(test_variable[i])

if __name__ == "__main__":
    main()