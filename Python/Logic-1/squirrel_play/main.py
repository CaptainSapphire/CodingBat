def squirrel_play(temp, is_summer):
  if (is_summer == True and temp <= 100 and temp >= 60):
    return True
  elif (temp >= 60 and temp <= 90):
    if (is_summer == False):
        return True
    else:
        return False
  else:
    return False
