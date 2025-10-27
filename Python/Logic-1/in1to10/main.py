def in1to10(n, outside_mode):
  if (n >= 1 and n <= 10 and outside_mode == False):
    return True
  elif (outside_mode == True):
    if (n <= 1 or n >= 10):
      return True
    else:
      return False
  else:
    return False
