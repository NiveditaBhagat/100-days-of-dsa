class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_element=max(candies)
        result=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies<max_element:
                result.append(False)
            else:
                result.append(True)
        
        return result
        
