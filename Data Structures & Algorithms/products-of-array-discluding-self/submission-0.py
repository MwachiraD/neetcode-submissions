class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        leftproduct = 1
        for i in range(n):

            result[i] = leftproduct
            leftproduct *= nums[i]
        rightproduct = 1 
        for i in range(n -1,-1,-1):
            result[i] *= rightproduct 
            rightproduct *= nums[i]
        return result
    
    

        