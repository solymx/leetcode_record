# basic binary search problem
# python3 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # init 
        length = len(nums)
        large = nums[length-1]
        high = length - 1
        low = 0
        small = nums[0]
        mid = length // 2 # no float just int
        # three cases can just give the answer
        if target in nums: 
            return nums.index(target)
        elif target > large:
            return length
        elif target < small:
            return 0
        # use binary search 
        while(high - low > 1):
            mid = (high + low) // 2
            if(target > nums[mid]):
                low = mid
            else:
                high = mid
        return high

        
