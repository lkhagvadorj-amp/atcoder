from enum import Enum

class BeautifulResult(Enum):
    YES = 'YES'
    NO = 'NO'

def is_beautiful_pole(x1: int, x2: int, x3: int) -> BeautifulResult:
    return BeautifulResult.YES.value if x2 - x1 == x3 - x2 else BeautifulResult.NO.value


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    answer = is_beautiful_pole(x1=a, x2=b, x3=c)
    print(answer)