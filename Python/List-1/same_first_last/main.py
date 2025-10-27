def same_first_last(nums):
  if len(nums) >= 1:
    # if first and last are equal
    if (nums[0] == nums[len(nums)-1]):
      return True;
    else:
      return False; 
  else:
    return False;
