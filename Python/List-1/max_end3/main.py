def max_end3(nums):
  if (nums[0] >= nums[len(nums)-1]):
    # make all nums0
    nums = [nums[0], nums[0],nums[0]]
  if (nums[0] <= nums[len(nums)-1]):
    # make all last element
    nums = [nums[len(nums)-1],nums[len(nums)-1],nums[len(nums)-1]]
  return nums;
