class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums=[]
        for num in nums:
            new_nums.append(num)
        for num in nums:
            new_nums.append(num)
        return new_nums
        