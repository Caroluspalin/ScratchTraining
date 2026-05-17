def two_sumn(target, nums):
    seen = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in seen:
            return [seen[need], i]
        seen[nums[i]] = i


Test = two_sumn(7, [1,4,8,6,4,5,6,2,1,3,4])
print(Test)