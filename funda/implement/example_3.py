import sys

input = sys.stdin.readline

P = input()

x = "abcdefgh"
y = "12345678"

length = len(x)

pos = (x.find(P[0]), y.find(P[1]))  # (0,0) ~ (length-1,length-1)

direction = {
    "left-up": (-2, -1),
    "left-down": (-2, 1),
    "right-up": (2, -1),
    "right-down": (2, 1),
    "up-right": (1, -2),
    "up-left": (-1, -2),
    "down-right": (1, 2),
    "down-left": (-1, 2),
}

cnt = 0
for k, v in direction.items():
    dx = pos[0] + v[0]
    dy = pos[1] + v[1]

    if not (dx < 0 or dy < 0 or dx >= length or dy >= length):
        cnt += 1

print("움직일 수 있는 경우의 수 : {}".format(cnt), file=sys.stdout)

