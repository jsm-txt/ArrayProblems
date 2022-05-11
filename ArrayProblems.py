def twoSum(self, nums: List[int], target: int) -> List[int]:
  result =[]
  nums_list = {}
  for i, num in enumerate(nums):
    newTarget = target - num
    if newTarget in nums_list:
      result.append([nums_list[newTarget], i])
    nums_list[num] = i


def largest(list_nums, nums):
  list_nums.sort()
  return list_nums[len(list_nums)-nums:len(list_nums)]
