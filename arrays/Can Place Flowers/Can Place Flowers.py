class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                if i==0:
                    left=0
                else:
                    left=flowerbed[i-1]

                if i==len(flowerbed)-1:
                    right=0
                
                else:
                    right=flowerbed[i+1]
                
                if left==0 and right==0:
                    flowerbed[i]=1
                    n-=1
        
        return n<=0
