class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        maxCandies = -1
        for i in range(0, len(candies)):
            if maxCandies < candies[i]:
                maxCandies = candies[i]

        print(maxCandies)
        trueValue = maxCandies - extraCandies
        print(trueValue)

        for i in range(0, len(candies)):
            if candies[i] >= trueValue:
                ret.append(True)
            else:
                ret.append(False)

        return ret