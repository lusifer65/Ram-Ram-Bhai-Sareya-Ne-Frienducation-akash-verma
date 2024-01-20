class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, result):
            if target == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue  
                if target < candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path, result)
                path.pop()

        candidates.sort()
        result = []
        backtrack(0, target, [], result)
        return result

