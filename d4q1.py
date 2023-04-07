def permuteUnique(nums):
    results = []
    n = len(nums)
    nums.sort() 
    visited = [False] * n 

    def backtrack(path):
        if len(path) == n:
            results.append(path[:]) 
        else:
            for i in range(n):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue 
                visited[i] = True
                path.append(nums[i])
                backtrack(path)
                visited[i] = False
                path.pop()

    backtrack([])
    return results

nums = [1, 1, 2]
print(permuteUnique(nums))
