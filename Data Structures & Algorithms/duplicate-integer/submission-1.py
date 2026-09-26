class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force approach
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        """
        
        # set is implemented as a hash table
        # loop thru all the elements in nums
        # check if current element has alr been seen, ret true
        nums_seen = set()
        for i in range(len(nums)):
            if nums[i] in nums_seen:
                return True
            nums_seen.add(nums[i])
        return False