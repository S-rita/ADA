class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=int, reverse=True)
        return str(nums[k-1])
