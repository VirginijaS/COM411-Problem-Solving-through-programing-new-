def interests():
  print("Enter your interest, one after the other, and enter \"stop\" when finished ") 
  set1 = set()
  activity = ""
  while(activity != "stop"):
    activity = input()
    set1.add(activity)
  return set1 

def tinderTheSecond():
  print("First person:")
  P1set = interests()
  print("Second person:")
  P2set = interests()
  common = P1set.intersection(P2set)
  if len(common) >  4:
    print(f"Yay - you are a match! you have {len(common)} ineterest in common")
  else:
    print(f"Well, I don't think it will work out :( You only have {len(common)}interest in common")

tinderTheSecond()