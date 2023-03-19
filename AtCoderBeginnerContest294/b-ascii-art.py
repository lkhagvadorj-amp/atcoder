def numToLetter (num):
    alphabet = ['.', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return alphabet[num]

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

S = [''] * (H)

for i in range (H):
    for j in range(W):
        S[i] = S[i] + numToLetter(A[i][j])

print("\n".join(S))