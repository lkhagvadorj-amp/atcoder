s = input()

if '00' in s:
  rep_s = s.replace('00', '0')
else:
  rep_s = s

print(len(rep_s))
