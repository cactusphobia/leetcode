nums01 = [1, 2, 3, 4]
nums02 = [1, 1, 1, 1, 1]
nums03 = [3, 1, 2, 10,1]

def tinhtong(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
    return nums
print(tinhtong(nums01))


# hhihihih