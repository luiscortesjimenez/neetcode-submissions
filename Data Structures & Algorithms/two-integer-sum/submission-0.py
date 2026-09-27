class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force approach
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        """
        # make a hash map to store nums seen w idx
        differenceMap = {}
        # loop thru, calc dif, check if we have seen dif before, 
        # if so ret dif fisrt since that means it was seen first and i
        # else add current num and idx since it may be a future nums dif
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in differenceMap:
                return [differenceMap[dif], i]
            else:
                differenceMap[nums[i]] = i
            