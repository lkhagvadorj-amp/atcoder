s = input()

result = -1

for i in range(len(s)):
    if 'a' in s[i]:
        result = i+1  

print(result)
