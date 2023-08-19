class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 1
        index = 0
        while index<len(nums):
            if nums[index] == val:
                nums.pop(index)
                index-=1

            else:
                j +=1

            index += 1

        return j