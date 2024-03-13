class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(start, target, subset):
            if target == 0:
                res.append(subset.copy())
                return

            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                subset.append(candidates[i])
                dfs(i+1, target-candidates[i],subset)
                subset.remove(candidates[i])
            
        dfs(0, target, subset)
        return res

        
