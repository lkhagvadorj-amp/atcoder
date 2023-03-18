S = list(input())
n = len(S)
answer = ''
    
for i in range(n//2):
    answer = answer + S[2*i+1] + S[2*i]
    
print(answer)
