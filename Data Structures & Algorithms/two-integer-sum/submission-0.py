class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        set={}

        for i,n in enumerate(nums):
            final=target-n
            if final in set:
                return [set[final],i]

            set[n]=i

        