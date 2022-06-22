# 문제에서는 모든 칸을 방문하도록 조건을 제시하지 않았다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # map size. width(N) X height(M)
cur_y, cur_x, cur_d = map(
    int, input().split()
)  # current position and current direction

game = [input().split() for _ in range(N)]  # map at the beginning
game[cur_y][cur_x] = "2"
cnt = 1

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def turn_left(cur_direction: int) -> int:
    return cur_direction - 1 if cur_direction != 0 else 3


def play_game():
    global cur_y
    global cur_x
    global cur_d
    global cnt

    # find the direction where can go
    left_on_me = cur_d
    for _ in range(4):
        left_on_me = turn_left(left_on_me)
        dy = cur_y + move[left_on_me][0]
        dx = cur_x + move[left_on_me][1]

        if game[dy][dx] == "0":
            print(
                "이동 {y},{x} => {dy},{dx}".format(x=cur_x, y=cur_y, dx=dx, dy=dy),
                file=sys.stdout,
            )
            cur_y = dy
            cur_x = dx
            cur_d = left_on_me
            cnt += 1

            game[dy][dx] = "2"

            return True

    opposite_dir = turn_left(turn_left(cur_d))
    dy = cur_y + move[opposite_dir][0]
    dx = cur_x + move[opposite_dir][1]

    if game[dy][dx] == "1":
        print(
            "현 위치와 방향 {dy},{dx} - {dir}".format(dy=cur_y, dx=cur_x, dir=cur_d),
            file=sys.stdout,
        )
        return False

    elif game[dy][dx] == "2":
        print(
            "뒤로 이동 {y},{x} => {dy},{dx}".format(x=cur_x, y=cur_y, dx=dx, dy=dy),
            file=sys.stdout,
        )
        cur_y = dy
        cur_x = dx

        return True


while play_game():
    pass

print("방문한 칸의 수 : {}".format(cnt), file=sys.stdout)

