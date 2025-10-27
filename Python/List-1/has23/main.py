def has23(nums):
  # check first spot
  if (nums[0] == 2 or nums[0] == 3):
    return True
  # check second spot
  if (nums[1] == 2 or nums[1] == 3):
    return True
  else:
    return False;
