class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        res = []
        for index in range(size-2):  # no need to iter all nums
            if nums[index] > 0:  # there is no valid result after
                break
            # ignore same result
            if index > 0 and nums[index] == nums[index-1]:
                continue
            r, l = index + 1, size - 1
            while r < l:
                s = nums[index] + nums[l] + nums[r]
                if s < 0:
                    r += 1
                    # ignore same result
                    while r < l and nums[r] == nums[r-1]:
                        r += 1
                elif s > 0:
                    l -= 1
                    # ignore same result
                    while r < l and nums[l] == nums[l+1]:
                        l -= 1
                else:
                    res.append([nums[index], nums[r], nums[l]])
                    r += 1
                    l -= 1
                    while r < l and nums[r] == nums[r-1]:
                        r += 1
                    while r < l and nums[l] == nums[l+1]:
                        l -= 1
        return res

