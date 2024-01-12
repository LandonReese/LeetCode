# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = ""
        ret_list = []
        left_count, right_count = n, n

        print(left_count, right_count)

        def left(s: str)-> str:
            s = s + "("
            return s
        
        def right(s: str)-> str:
            s = s + ")"
            return s
        
        for i in range(0, n):
            parentheses = left(parentheses)
            for j in range(n, 0, -1):
                parentheses = right(parentheses)
            
            
        ret_list.append(parentheses)
        parentheses = ""

        print(ret_list)

        return(ret_list)


def main():
    inputs = [
        1,
        2,
        3,

    ]

    outputs = [
        ["()"],
        ["(())", "()()"],
        ["((()))","(()())","(())()","()(())","()()()"],

    ]

    s = Solution()

    for i in range(0, len(inputs)):
        print(f"Test {i + 1}")
        assert(s.generateParenthesis(inputs[i]) == outputs[i])

if __name__ == "__main__":
    main()