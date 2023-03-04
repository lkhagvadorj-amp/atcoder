n=int(input())
s=input()
ch=[[] for i in range(26)]
ans=[n-i-1 for i in range(n-1)]
for i in range(n):
  if ch[ord(s[i])-97]:
    for j in ch[ord(s[i])-97]:
      ans[i-j-1]=min(j,ans[i-j-1])
  ch[ord(s[i])-97].append(i)
for i in range(n-1):
  print(ans[i])