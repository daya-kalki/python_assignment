def searchRange(nums, target):
    left = binarySearch(nums, target, True)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    right = binarySearch(nums, target, False) - 1
    return [left, right]

def binarySearch(nums, target, leftmost):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] > target or (leftmost and nums[mid] == target):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo if leftmost else hi + 1
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = searchRange(nums, target)
print(result)  
