# An n-bit gray code sequence is a sequence of 2n integers where:

# Every integer is in the inclusive range [0, 2n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.

from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        binary = {
            0: "0000",  #0: 1,2,4,8
            1: "0001",  #1: 0,2,3,5,
            2: "0010",
            3: "0011",
            4: "0100",
            5: "0101",
            6: "0110",
            7: "0111",
            8: "1000",
            9: "1001",
            10: "1010",
            11: "1011",
            12: "1100",
            13: "1101",
            14: "1110",
            15: "1111",
        }

        pairs = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: [],
            13: [],
            14: [],
            15: [],
        }


        numlist = []

        def differ(s1: str, s2: str)-> bool:
            count = 0
            for i in range(0, len(s1)):
                if s1[i] == s2[i]:
                    count += 1
            
            if count >= 3:
                return True
            return False
        
        print(numlist)
        for i in range(0, 16):
             print(f"Comparing binary[{i}]: {binary[i]}")
             for j in range(0, 16):
                 if j == i:
                     continue
                 print(f"{binary[i]},{binary[j]} {differ(binary[i], binary[j])}")
                 if differ(binary[i], binary[j]):
                     pairs[i].append(j)
                     
        print(binary)
        print(pairs)
        
        return numlist

def main():
    inputs = [
        1,
        2,
        3,
    ]

    outputs = [
        [0,1],
        [0,1,3,2],
        [],
    ]

    s = Solution()

    for i in range(0, len(inputs)):
        print(f"Test {i + 1}: {s.grayCode(inputs[i]) == outputs[i]}")

if __name__ == "__main__":
    main()