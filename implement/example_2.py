import sys

input = sys.stdin.readline

N = int(input())


def get_count_in_time(n: int):
    cnt = 0

    for i in range(N + 1):
        if str(i).find("3") >= 0:
            cnt += 3600
            continue
        for j in range(60):
            if str(j).find("3") >= 0:
                cnt += 60
                continue
            for k in range(60):
                if str(k).find("3") >= 0:
                    cnt += 1
    return cnt


def get_count_in_time_ref(n: int):  # 교재 풀이
    cnt = 0

    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                if "3" in "".join([str(i), str(j), str(k)]):
                    cnt += 1
    return cnt


import time

start = time.time()
print(
    "3이 들어간 조합의 갯수 : {count} - {time}".format(
        count=get_count_in_time(N), time=time.time() - start
    ),
    file=sys.stdout,
)
start = time.time()
print(
    "3이 들어간 조합의 갯수 : {count} - {time}".format(
        count=get_count_in_time_ref(N), time=time.time() - start
    ),
    file=sys.stdout,
)

