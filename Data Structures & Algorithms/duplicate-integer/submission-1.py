class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bucket={}
        for i in range(len(nums)):
            bucket[nums[i]] = bucket.get(nums[i], 0) + 1

        for key in bucket:
            if (bucket[key]>1):
                return True 
        return False