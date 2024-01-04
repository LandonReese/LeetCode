class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        data = []
        
        col = 0
        row = 0
        zig = False
        
        return_string = ""
        
        print(f"s[i] | col, row")
        for i in range(0, len(s)):
            print(f"{s[i]} | {col}, {row}")
            location = []
            location.append(s[i])
            location.append(col)
            location.append(row)
            
            if row == 0:
                zig = False
                
            if row == numRows - 1:
                zig = True
            
            if zig:
                row -= 1
                col += 1
            else:
                row += 1
                
            data.append(location)
                
        print(data)
            
        
        # 3     Col Col Col
        # Row   P       A       H       N
        # Row   A   P   L   S   I   I   G
        # Row   Y       I       R
        
        # 4     Col Col Col
        # Row   P           I           N
        # Row   A       L   S       I   G
        # Row   Y   A       H   R
        # Row   P           I
        
        for i in range(0, numRows):
            for item in data:
                if item[2] == i:
                    return_string += item[0]
        
        print(return_string)
        return return_string
    
def main():
    inputs = [
        ["PAYPALISHIRING", 3],
        ["PAYPALISHIRING", 4],
        ["", 0],
        ["AB", 1]
    ]
    
    outputs = [
        "PAHNAPLSIIGYIR",
        "PINALSIGYAHRPI",
        "",
        "AB"
    ]
    
    solution = Solution()
    
    for i in range(0, len(inputs)):
        s, numRows = inputs[i]
        assert(solution.convert(s, numRows) == outputs[i])
    
if __name__ == "__main__":
    main()