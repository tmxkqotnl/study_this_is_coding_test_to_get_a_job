import sys
from typing import Union

input = sys.stdin.readline

N = int(input())
M = input().split()

DIRECTION = {
    "R": {"x": 1, "y": 0},
    "L": {"x": -1, "y": 0},
    "U": {"x": 0, "y": -1},
    "D": {"x": 0, "y": 1},
}


def get_position(n: int, m: list[str]) -> Union[tuple[int, int], str]:
    global DIRECTION
    x, y = 1, 1

    for i in m:
        try:
            dx = x + DIRECTION[i]["x"]
            dy = y + DIRECTION[i]["y"]
            if dx < 1 or dx > n or dy < 1 or dy > n:
                print("좌표 밖입니다. 무시합니다.", file=sys.stdout)
            else:
                x, y = dx, dy
        except KeyError:
            return "존재하지 않는 방향입니다."

    if x < 1 or x > n or y < 1 or y > n:
        return "좌표가 지도를 벗어났습니다."

    return (y, x)


print("최종 위치 : {}".format(get_position(N, M)), file=sys.stdout)

