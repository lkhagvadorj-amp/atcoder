def combine_two_string(x1: str, x2: str) -> str:
    answer = ""
    for i in range(len(x1) + len(x2)):
        if i % 2 == 0:
            answer += x1[i // 2]
        else:
            answer += x2[i // 2]
    return answer

if __name__ == '__main__':
    o = input()
    e = input()
    ans = combine_two_string(x1=o, x2=e)
    print(''.join(ans))