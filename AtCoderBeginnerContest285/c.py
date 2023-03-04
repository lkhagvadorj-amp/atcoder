s = input()
ans = 0
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in s:
  ans *= 26
  ans += 1+alphabets.index(i)
print(ans)