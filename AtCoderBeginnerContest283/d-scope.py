def check(S):
    box = set()
    for si in S:
        if si in "abcdefghijklmnopqrstuvwxyz":
            if si in box:
                return False
            box.add(si)
        elif si == ")":
            box.clear()
    return True
  
s = input()
if check(s):
  print("Yes")
else:
  print("No")
