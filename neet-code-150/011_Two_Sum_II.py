class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers)-1

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r = r-1
            elif currSum < target:
                l = l+1
            else: 
                return [l+1, r+1]
