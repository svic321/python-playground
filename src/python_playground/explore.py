# %%

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        my_list = [i for i in nums if i != val]
        return len(my_list)

nums = [3,2,2,3]
val = 3

print(Solution().removeElement(nums,val))
# %%
