class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sulla={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in sulla:
                return [sulla[diff],i]

            sulla[n]=i


       
        