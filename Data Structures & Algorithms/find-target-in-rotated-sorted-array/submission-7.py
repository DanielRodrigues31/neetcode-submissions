class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            # calculate m
            m = (l + r) // 2

            # return when target found
            if nums[m] == target:
                return m

            # left side sorted
            elif nums[l] <= nums[m]:
                # target between sorted l and m then enter search space
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                
                # enter unsorted search space (right side)
                else:
                    l = m + 1

            # right side sorted
            else:
                # target between sorted m and r then enter search space
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                
                # enter unsorted search space (left side)
                else:
                    r = m - 1
        return -1




        