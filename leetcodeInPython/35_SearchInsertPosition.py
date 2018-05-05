class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return [target]
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                if nums[i] > target:
                    return i
        else:
            return len(nums)

        
        #return len([x for x in nums if x<target])


        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = left + (right - left) / 2
        #     if nums[mid] >= target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1

        # return left