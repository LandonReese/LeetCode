class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        test_list = ""
        return_index = -1

        print(f"Length | Haystack {len(haystack)} | Needle {len(needle)}")
        if len(needle) > len(haystack):
            return -1
        
        print(f"i in range(0, {(len(haystack) - len(needle) + 1)}) | needle[0] {needle[0]}")
        for i in range(0, (len(haystack) - len(needle) + 1)):
            test_list = ""

            if(haystack[i] == needle[0]):
                for j in range(0, len(needle)):
                    test_list += haystack[j + i]

                if test_list == needle:
                    return_index = i
                    break

        return return_index
        
def main():
    solution = Solution()
    haystack = "landonbutlandon"
    needle = "landon"
    print(f"Needle length {len(needle)} Haystack Length {len(haystack)}")
    print(f"Index of needle: {solution.strStr(haystack, needle)}")

if __name__ == "__main__":
    main()