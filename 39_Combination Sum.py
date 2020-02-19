'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def DFS(candidates, target, result, temp, index):
            if target == 0:
                result.append(temp[:])
                return
            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    break
                temp.append(candidates[i])
                DFS(candidates, target - candidates[i], result, temp, i)
                temp.pop()
        
        candidates.sort()
        result = []
        if not candidates:
            return result
        temp = []
        DFS(candidates, target, result, temp, 0)
        
        return result