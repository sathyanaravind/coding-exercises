class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
    
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
        
            # pick
            subset.append(nums[i])
            dfs(i+1)

            # not pick
            subset.remove(nums[i])
            dfs(i+1)

        dfs(0)
        return res
